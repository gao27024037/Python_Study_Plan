import xlwt


if __name__ == '__main__':
    result=[["选手名字","出生日期","最好成绩","第二名成绩","第三名成绩","最差成绩"]]
    for line in open("score_data.txt"):
        data=line.strip().split(",")
        person=[]
        person.append(data[0])
        person.append(data[1])
        if len(data)>3:

            score=[str(i//60)+":"+str(i%60) for i in sorted([int(i[-2:])+int(i[:-3])*60 for i in data[2:]])]
            person.append(score[0])
            person.append(score[1] if len(score)>=2 else score[0])
            person.append(score[2] if len(score)>=3 else (score[1] if len(score)>=2 else score[0]))
            person.append(score[-1])
        result.append(person)

    book = xlwt.Workbook()  # 新建一个excel
    sheet = book.add_sheet('case1_sheet')  # 添加一个sheet页
    row = 0  # 控制行
    for line in result:
        col = 0  # 控制列
        for s in line:  # 再循环里面list的值，每一列
            sheet.write(row, col, s)
            col += 1
        row += 1
    book.save('taojian.xls')  # 保存到当前目录下


