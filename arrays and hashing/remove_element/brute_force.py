class Rem:
    def remove( nums  , val ): #define function
        num1 = [] #define new array
        for x in nums: #iterate old array
            if  x != val : #if x isnt equal to val add it to new array
                num1.append(x)
        return len(num1), num1  # return k (number of elements remaining) and new array      
                
    nums = [2,3,2,4,5,3,1]
    val = 3
    k, arr = remove(nums, val)
    print(k)    
    print(arr)
