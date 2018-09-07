# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].



class Solution:
    def twoSum(self, nums, target):
        length=len(nums)
        data={nums[0]:0,}
        for i in range(1,length):
            numj=target-nums[i]
            if numj in data:
                return data[numj],i
            data[nums[i]]=i


if __name__ == '__main__':
    a = Solution()
    a = a.twoSum([3,2,3,4],6)
    print(a)
