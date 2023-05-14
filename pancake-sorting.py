class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = []

        def reverse(arr, end):
            start = 0
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        for target in range(n, 0, -1):
            target_index = arr.index(target)

            if target_index == target - 1:
                continue

            reverse(arr, target_index)
            result.append(target_index + 1)
            reverse(arr, target - 1)

            result.append(target)

        return result