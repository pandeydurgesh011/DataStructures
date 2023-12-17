def twoSum_bruteforce(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == target:
                print(i,j)

#Optimised Solution - Time Complexity O(n)
def twoSum_optimised(arr,target):
    d = {}
    for i in range(len(arr)):
        temp = target-arr[i]
        if temp in d:
            print(d[temp],i)
        else:
            d[arr[i]] = i

if __name__ == "__main__":
    arr = [2,7,11,15,12,10,5]
    target = 15
    twoSum_bruteforce(arr,target)
    twoSum_optimised(arr,target)