def gcf2(a,b):
    while b!=0:
        a,b= b,a%b
    return a
def gcf(nums):
    if not nums:
        return 0
    currentgcf=nums[0]
    for num in nums[1:]:
        currentgcf=gcf2(currentgcf,num)
        if currentgcf==1:
            return 1
    return currentgcf
nums=input('Enter 2-10 numbers')
nums=nums.split()
numa=[int(num) for num in nums]

a=gcf(numa)
print(a)
