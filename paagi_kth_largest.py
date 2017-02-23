import random


def k_large(nums,k,start,end):
    idx = random.randint(start,end)
    #idx  = 5
    print("pivot idx initially",nums[idx])
    pivot = nums[idx]
    i = 0
    j = 0

    while j < len(nums):

        if nums[j] >= pivot:
            j += 1
        else:
            if nums[idx] == nums[i]:
                idx = j
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
    nums[idx], nums[i] = nums[i], nums[idx]
    print(nums,i)
    if i == len(nums)-k:
        return nums[i]
    else:
        if i > len(nums)-k:
            return k_large(nums,k,start,i-1)
        else:
            return k_large(nums,k,i+1,end)

nums = [10,1,9,5,6,7, 2]
k = 1
print(k_large(nums,k, 0 ,len(nums)-1))
