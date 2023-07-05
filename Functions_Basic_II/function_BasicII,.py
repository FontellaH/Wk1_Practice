# Assignment: Functions Basic II



#Countdown - 
#1 Create a function that accepts a number as an input. 
#2 Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
    # 2a Example: countdown(5) should return [5,4,3,2,1,]


# 1
def countdown(num): 
# 2
    new_countdownList=[]
    for i in range(num,0,-1):
        new_countdownList.append(i)
    return new_countdownList

# 2a  // [5,4,3,2,1,]
print(countdown(5))







#1 Print and Return - Create a function that will receive a list with two numbers.
    # 2  Print the first value and return the second.
        # 2a Example: print_and_return([1,2]) should print 1 and return 2

def print_and_return(two_nums):
    # 2, 2a- should print 1 and return 2
    print(two_nums[0])
    return two_nums[1]

#  Remember to make a new var to stores the value
nums = print_and_return([1,2])
# Always to remember to call the function for result
print(nums)








#1 First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
    #2 Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

# 1
def first_plus_length(list):
# 2  should return 6 (first value: 1 + length: 5)
    return list[0]+len(list)

print(first_plus_length([1,2,3,4,5]))
    







#1 Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. 
# Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
    # Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
    # Example: values_greater_than_second([3]) should return False


# 1
def values_greater_than_second(list1):
    new_list=[]
    if len(list1)>1:
        for i in range(len(list1)):
            if list1[i]>list1[1]:
                new_list.append(list1[i])
        return new_list
    else:
        return False

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))







# This Length, That Value - Write a function that accepts two integers as parameters: size and value.
#  The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
    # Example: length_and_value(4,7) should return [7,7,7,7]
    # Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def length_and_value(size,value):
    length1=[]
    for i in range(size):
        length1.append(value)
    return length1 

print(length_and_value(4,7)) 
print(length_and_value(6,2))     