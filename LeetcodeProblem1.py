
class Solution:
    def containsDuplicate(nums):
        output = None
        checkList = []
        for number in nums:
            if number in checkList:
                output = True
                break
            else:
                checkList.append(number)
        if output == None:
            output = False
        print(output)

numberList = [1,1,2,2,3,4,5]
Solution.containsDuplicate(numberList)
numberList2 = [1,2,3,4,5]
Solution.containsDuplicate(numberList2)
numberList3 = [1,1,1,1,1]
Solution.containsDuplicate(numberList3)
numberList4 = [1,2,3,4,5,5]
Solution.containsDuplicate(numberList4)