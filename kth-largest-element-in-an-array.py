class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def sortArray(nums: List[int]) -> List[int]:
            def mergeSort(left, right, arr):
                if left == right:
                    return [arr[left]]
                mid = left + (right - left) // 2
                left_half = mergeSort(left, mid, arr)
                right_half = mergeSort(mid + 1, right, arr)
    
                return merge(left_half, right_half)

            def merge(left_half, right_half):
                idx1 = 0
                idx2 = 0
                merged = []
                while idx1 < len(left_half) and idx2 < len(right_half):
                    if left_half[idx1] < right_half[idx2]:
                        merged.append(left_half[idx1])
                        idx1 += 1
                    else:
                        merged.append(right_half[idx2])
                        idx2 += 1

                if idx1 < len(left_half):
                    merged += left_half[idx1:]

                if idx2 < len(right_half):
                    merged += right_half[idx2:]

                return merged

            return mergeSort(0, len(nums)-1, nums)
        nums = sortArray(nums)
        return nums[-k]