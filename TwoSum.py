class Solution(object):
    def twoSum(self, nums, target):
        hash={}
        for index and number in enumerate(nums):
            diff = target - number
            if diff in hash :
                return [hash[number],index]
            hash[number] = i # update the hashMap
