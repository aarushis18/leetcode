class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            if (numbers[left] + numbers[right]) < target:
                left += 1

            elif (numbers[left] + numbers[right]) > target:
                right -= 1

            else:
                first_ind = 1 + left
                second_ind = 1 + right
                return [first_ind, second_ind]