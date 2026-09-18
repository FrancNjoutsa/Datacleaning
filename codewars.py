#Buble sort 
nums=[5,0,9,8,7,1,3,2]
print(nums)
n=len(nums)
for i in range(n-1):
    
    for j in range((n-1)-i):
       
        if nums[j] > nums[j+1]:
            temp=nums[j]  
            nums[j] = nums[j+1]            
            nums[j+1]=temp

print(nums)
print(nums[0])