# Q1. Check whether a number is even or odd while using a function and returing true or false.
n=int(input("Enter a number: "))
def check_even_odd(n):
    if n % 2 == 0:
        return True #true mean even number
    else:
        return False #false mean odd number
print(check_even_odd(n))

#Q2. To find the maximum of list of numbers using a function and returning the maximum number.
def find_maximum(numbers):
    if not numbers:
        return None  # Return None for empty list
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
print(find_maximum([3, 5, 2, 8, 1]))  # Output: 8
print(find_maximum([]))  # Output: None
print(find_maximum([-10, -5, -20, -1]))  # Output: -1

#Q3.To reverse a list of numbers using a function and returning the reversed list.
def reverse_list(numbers):
    return numbers[::-1]
print(reverse_list([1, 2, 3, 4, 5]))

#Q4. To remove the duplicates from a list of numbers using a function and returning the unique numbers.
def remove_duplicates(numbers):
    return list(set(numbers))
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))

#Q5.To check word frequency in a string using a function and returning the frequency of each word.
def word_frequency(string):
    words=string.split()
    frequency={}
    for word in words:
        frequency[word]=frequency.get(word,0)+1
    return frequency
print(word_frequency("the quick brown fox jumps over the lazy dog"))
print(word_frequency("hello world hello kutte kamine suar kutte kamine"))

#Q6.To find the square of numbers in a list using lambda function and returning the squared numbers.
numbers = [1, 2, 3, 4, 5]
squared_numbers=list(map(lambda x: x**2,numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

#Q7.To sort by length of words in a list using lambda function and returning the sorted list.
words = ["apple", "banana", "cherry", "date"]
sorted_words=sorted(words,key=lambda x: len(x))
print(sorted_words)  # Output: ['date', 'apple', 'banana', 'cherry']

#Q8.To find the common elements in two lists using set and intersection and returning the common elements.
l1=[1, 2, 3, 4, 5]
l2=[4, 5, 6, 7, 8]
common_elements=list(set(l1) & set(l2))
print(common_elements)  # Output: [4, 5]

#Q9.Tuple unpacking: To unpack a tuple of numbers into separate variables using tuple unpacking in function and returning the unpacked variables.
def unpack_tuple(t):
    minimum,maximum,average=t
    return minimum,maximum,average
print(unpack_tuple((1, 10, 5.5)))  # Output: (1, 10, 5.5)

#Q10. Dictionary inversion: To invert a dictionary (swap keys and values) using a function and returning the inverted dictionary.
def invert_dictionary(d):
    return {v: k for k, v in d.items()}

print(invert_dictionary({"a": 1, "b": 2, "c": 3}))  # Output: {1: "a", 2: "b", 3: "c"}

#Q11(DSA).to find the second largest number in a list of numbers using a function and returning the second largest number without using sort function.
def second_largest(numbers):
    if len(numbers)<2:
        return None  # Not enough elements for second largest
    unique_numbers=list(set(numbers))  # Remove duplicates
    if len(unique_numbers)<2:
        return None  # Not enough unique elements for second largest
    largest=None
    second_largest=None
    for num in unique_numbers:
        if largest is None or num>largest:
            second_largest=largest
            largest=num
        elif second_largest is None or num>second_largest:
            second_largest=num
    return second_largest
print(second_largest([3, 5, 2, 8, 1])) 

