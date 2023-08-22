class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set()
        set2 = set()
        answer = []
        arr1 = []
        arr2 = []
        for i in nums1:
            set1.add(i)
        for i in nums2:
            set2.add(i)
        for i in range(len(nums1)):
            if nums1[i] not in set2 and nums1[i] not in arr1:
                arr1.append(nums1[i])
        for i in range(len(nums2)):
            if nums2[i] not in set1 and nums2[i] not in arr2:
                arr2.append(nums2[i])
        answer.append(arr1)
        answer.append(arr2)
        return answer