#6/13/2022 Weekly Coding Challenge
##########################################################################
nums1 = [1,3]
nums2 = [2]
#nums1 = [1,2]
#nums2 = [3,4]
def MedSortArrays(nums1, nums2):
    mergedArray = nums1+nums2
    mergedLength = len(mergedArray)
    sortedArray = sorted(mergedArray)
    halfway = (mergedLength -1) // 2
    if(mergedLength % 2 == 1):
        return print(sortedArray[halfway])
    else:
        return print((sortedArray[halfway] + sortedArray[halfway + 1])/2.0)
##########################################################################
lists = [[1,4,5],[1,3,4],[2,6]]
#lists = []
#lists = [[]]
def MergedSortedLists(lists):
    mergedLists = []
    if lists:
        for i in range(len(lists)):
            mergedLists += lists[i]
        return print(sorted(mergedLists))

    else: #empty list
        return print([])
##########################################################################
def main():
    print("Finding median of two sorted arrays")
    MedSortArrays(nums1, nums2)
    print("Creating one sorted list from multiple")
    MergedSortedLists(lists)
