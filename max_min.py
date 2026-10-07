n=int(input("Enter the number of elements in the list: "))
num=[]
if n<=0:
    print("Please enter a positive integer for the number of elements.")
else:
    for i in range(n):
        element=int(input(f"Enter element {i+1}: "))
        num.append(element)
    max_num = num[0]
    min_num = num[0]
    for i in range(len(num)):
        if num[i]<min_num:
            min_num=num[i]
        if num[i]>max_num:
            max_num=num[i]
    print(f"The maximum number in the list is: {max_num}")        
    print(f"The minimum number in the list is: {min_num}") 