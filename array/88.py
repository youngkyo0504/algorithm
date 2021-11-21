
def merge(nums1, m, nums2, n):
        if(n ==0 ):
            return nums1
        for i in range(len(nums1)-1,-1,-1):
            if (nums1[m-1] >= nums2[n-1] or n-1 < 0) and m > 0:
                nums1[m-1], nums1[i] = nums1[i], nums1[m-1]
                m-=1
            else:
                nums2[n-1],nums1[i] =nums1[i] ,nums2[n-1]
                n-=1
        return nums1

nums = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n=3

print(merge(nums,m,nums2,n))
