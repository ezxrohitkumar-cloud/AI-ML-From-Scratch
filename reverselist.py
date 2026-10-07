n=int(input("Enter the number of elements in the list: "))
num=[]

for i in range(n):
    element=int(input(f"Enter element {i+1}: "))
    num.append(element)
print(f"original list is: {num}")
left=0
right=len(num)-1
while left<right:
    num[left],num[right]=num[right],num[left]
    left+=1
    right-=1
print(f"Reversed list is: {num}")