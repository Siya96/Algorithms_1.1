
def maxSubArr(array):
    if len(array) == 2:

        return (array, (array[0]*array[1]))
    
    leftA = maxSubArr(array[:len(array)//2])
    rightA = maxSubArr(array[len(array)//2:])

    productLeft = (leftA[0] * leftA[1])
    productRight = (rightA[0] * rightA[1])

    if abs(productLeft) > 1:
        bestProductLeft = productLeft
    if abs(productRight) > 1:
        bestProductRight = productRight
    
    highestProduct = max(bestProductLeft, bestProductRight)

    return highestProduct





#Incremental O(n)
def findMax(arr):
    if len(arr) == 2:
        max_at = arr[0]
        min_at = arr[0]
        mini = min(arr[0], arr[1])
        maxi = max(arr[0], arr[1])
        penta = calculate(arr, max_at, max_at, min_at, arr.index(mini), arr.index(maxi))
        return (penta)
    

    last = arr[-1]
    
    pentaCal = findMax(arr[:-1])


    pentaCal[0].append(last)
    

    maxSave = pentaCal[1]
    currMax = pentaCal[2]
    currMin = pentaCal[3]
    minIsave = pentaCal[4]
    maxIsave = pentaCal[5]

    cal = calculate(pentaCal[0], pentaCal[1], pentaCal[2], pentaCal[3], minIsave, maxIsave)
    

    return (cal) 

def calculate(arr, totMax, currMax, currMin, minI, maxI):

    prev_max_at = currMax
    prev_min_at = currMin
    maxVal = totMax
    max_at = max(arr[-1], arr[-1] * prev_min_at, arr[-1] * prev_max_at)
    min_at = min(arr[-1], arr[-1] * prev_min_at, arr[-1] * prev_max_at)
    maxVal = max(maxVal, max_at)



    if max_at == arr[-1]:
        minI = arr.index(arr[-1])
        maxI = arr.index(arr[-1])
    if max_at == arr[-1] * prev_min_at:

        
    if max_at == arr[-1] * prev_max_at:
        pass

    return (arr, maxVal, max_at, min_at)

a = [-2, 0.3, -1, 4, 5, -6, 0.5, 4]
print(findMax(a))