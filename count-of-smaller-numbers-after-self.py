class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        indexes = list(range(n))

        def merge_sort(start, end):
            if start < end:
                mid = (start + end) // 2
                merge_sort(start, mid)
                merge_sort(mid + 1, end)
                merge(start, mid, end)

        def merge(start, mid, end):
            merged = []
            i, j = start, mid + 1
            smaller_count = 0

            while i <= mid and j <= end:
                if nums[indexes[i]] <= nums[indexes[j]]:
                    result[indexes[i]] += smaller_count
                    merged.append(indexes[i])
                    i += 1
                else:
                    smaller_count += 1
                    merged.append(indexes[j])
                    j += 1

            while i <= mid:
                result[indexes[i]] += smaller_count
                merged.append(indexes[i])
                i += 1

            while j <= end:
                merged.append(indexes[j])
                j += 1

            indexes[start:end+1] = merged

        merge_sort(0, n - 1)
        return result