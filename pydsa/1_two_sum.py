class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_index = {}
        for idx, num in enumerate(nums):
            diff = target - num

            # EAFP
            # try:
            #     return num_index[diff], idx
            # except KeyError:
            #     num_index[num] = idx

            # LBYL
            if diff in num_index:
                return num_index[diff], idx
            else:
                num_index[num] = idx


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
