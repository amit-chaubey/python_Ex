###Q1 

n = 5

fact = 1
for i in range(1, n+1):
    fact *=i
print(fact)

###Q2

s = "madam"

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

###Q4

nums = [4,5,6,7,0,1,2]

max_num = nums[0]
for i in range(1, len(nums)):
    if nums[i] > max_num:
        max_num = nums[i]

print(max_num)