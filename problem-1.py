# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 & 9. 
# The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.



nums = list(range(1000))
#print(nums[::3])
#print(nums[::5])



def find_multiples(m):
    multiples = nums[::3]
    #print("mult " + str(multiples))
    for num in nums[::5]:
        #print("num " + str(num))
        if num not in nums[::3]:
            #num += multiples
            multiples.append(num)
            #print("mult2 " + str(multiples))
    print(sum(multiples))
        
find_multiples(nums)