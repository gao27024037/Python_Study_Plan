import tensorflow as tf


def build_input(self):
    with tf.name_scope('input'):
        self.inputs = tf.placeholder(tf.int32, shape=(self.num_seqs, self.num_steps), name='inputs')
        self.targets = tf.placeholder(tf.int32, shape=(self.num_seqs, self.num_steps), name='target')
        self.keep_prob = tf.placeholder(tf.float32, name='keep_prob')

        # use embedding layer for Chinese
        # do not use embedding layer for English

        if self.use_embeeding is False:
            self.lstm_inputs = tf.one_hot(self.inputs, self.num_classes)
        else:
            with tf.device('/cpu:0'):
                embedding = tf.get_variable('embedding', [self.num_classes, self.embedding_size])
                self.lstm_inputs = tf.nn.embedding_lookup(embedding, self.inputs)


def build_lstm(self):
    # 创建单个cell并堆叠多层
    def get_a_cell(lstm_size, keep_prob):
        lstm = tf.contrib.nn.run_cell.BasicLSTMCell(lstm_size)
        drop = tf.contrib.nn.rnn_cell.DropoutWrapper(lstm, output_keep_prob=keep_prob)
        return drop

    with tf.name_scope('lstm'):
        cell = tf.nn.rnn_cell.MultiRNNCell([get_a_cell(self.lstm_size, self.keep_prob) for _ in range(self.num_layers)])
        self.initial_state = cell.zero_state(self.num_seqs, tf.float32)  # 初始隐藏状态 h0?

    # 通过dynamic_rnn对cell展开时间维度
    self.lstm_outputs, self.final_state = tf.contrib.nn.dynamic_rnn(cell, self.lstm_inputs,
                                                                    initial_state=self.initial_state) # 多层LSTM的隐层h
    # 通过lstm_output得到概率
    seq_output = tf.concat(self.lstm_outputs, 1)
    x = tf.reshape(seq_output, [-1, self.lstm_size])

    with tf.variable_scope('softmax'):
        softmax_w = tf.Variable(tf.truncated_normal([self.lstm_size, self.num_classes], stddev=0.1))
        softmax_b = tf.Variable(tf.zeros(self.num_classes))

    self.logits = tf.matmul(x, softmax_w) + softmax_b
    self.proba_prediction = tf.nn.softmax(self.logits, name='predictions')

def build_loss(self):
    with tf.name_scope('loss'):
        y_one_hot = tf.one_hot(self.targets,self.num_classes)
        y_reshaped = tf.reshape(y_one_hot,self.logits.get_shape())
        loss = tf.nn.softmax_cross_entropy_with_logits(logits=self.logits,labels=y_reshaped)
    self.loss = tf.reduce_mean(loss)

