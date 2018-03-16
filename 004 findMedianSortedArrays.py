class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1 and not nums2:
            return 0.0

        i = j = 0
        nums3 = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                nums3.append(nums1[i])
                i = i + 1
            else :
                nums3.append(nums2[j])
                j = j + 1

        if(i < len(nums1)):
            for k in range(i, len(nums1)):
                nums3.append(nums1[k])

        if(j < len(nums2)):
            for k in range(j, len(nums2)):
                nums3.append(nums2[k])

        return (nums3[~len(nums3)//2] + nums3[len(nums3)//2])/2


    def findMedianSortedArrays2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length = len(nums1) + len(nums2)

        if length == 0:
            return 0.0
        else:
            mid_1 = mid_2 = (length-1)//2
            if length % 2 == 0:
                mid_2 = mid_2 + 1


        i = j = 0
        nums3 = []

        while (i < len(nums1) or j < len(nums2)) and len(nums3) <= mid_2:
            if j >= len(nums2) or (i < len(nums1) and nums1[i] <= nums2[j]):
                nums3.append(nums1[i])
                i = i + 1
            else:
                nums3.append(nums2[j])
                j = j + 1
        return (nums3[mid_1] + nums3[mid_2])/2


    def findMedianSortedArrays3(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1 and not nums2:
            return 0.0

        i = j = 0
        nums3 = nums1 + nums2
        nums3.sort()

        return (nums3[~len(nums3)//2] + nums3[len(nums3)//2])/2



if __name__ == '__main__':
    solution = Solution()
    nums1 = [1,2]
    nums2 = [3,4]
    
    result = solution.findMedianSortedArrays3(nums1, nums2)

    print(result)