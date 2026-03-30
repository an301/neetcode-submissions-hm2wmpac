class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = len(nums1) - 1
        p1 = m - 1
        p2 = n - 1

        while m > 0 and n > 0:
            if nums1[p1] >= nums2[p2]:
                nums1[last] = nums1[p1]
                p1 -= 1
                m -= 1
            else:
                nums1[last] = nums2[p2]
                p2 -= 1
                n -= 1
            last -= 1
        
        if m > 0:
            while m > 0:
                nums1[last] = nums1[p1]
                p1 -= 1
                m -= 1
                last -= 1
        elif n > 0:
            while n > 0:
                nums1[last] = nums2[p2]
                p2 -= 1
                n -= 1
                last -= 1

        print(nums1)