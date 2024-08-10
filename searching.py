from typing import List
#problem 1
def second_largest(number:List[int])-> int :
    if (len(number)<2) :
        return 
    
    n = len(number)
    for i in range(n-1):
        min_index=i
        for j in range (i+1,n):
            if number[j]<number[min_index]:
                min_index=j
        number[i],number[min_index],=number[min_index],number[i]
    return number[-2]    
      
# number = [4,8,2,5]
# result = second_largest(number)
# print(result)

#problem 2
def missing_number(number:List[int])->int:
    n=len(number)+1    
    result= (n*(n+1))//2
    sum = 0
    for i in range (len(number)):
        sum = sum + number[i]
    return(result-sum)

# nums = [1,2,4,5]
# resultt=missing_number(nums)
# print(resultt)

#problem 3
def numbers_of_occur(numbers:List[int],target:int)->int:
    count=0
    first=-1
    last=-1
    for i in range (len(numbers)):
        if numbers[i]==target:
            count+=1
            if first==-1:
               first=i
            last=i 

    return count , first , last


# nums= [1,1,1,1]
# print(numbers_of_occur(nums,1))

#problem 4
def rotated_sorted_array(numbers:List[int])->int:
    for i in range(len(numbers)-1):
        if(numbers[i+1]>numbers[i]):
            continue
        else:
            return(i+1)
    return 0
            
        
# numbers=[3,4,1,2]   
# print(rotated_sorted_array(numbers))     

def rotated_bonus(numbers:List[int])->int:
    l=0
    r=len(numbers)-1
    while l<r:
        m=(l+r)//2
        if numbers[m]>numbers[l]:
            l=m
        else:
            r=m
    return l+1

numbers=[3,4,1,2]   
print(rotated_bonus(numbers))    










































































