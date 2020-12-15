arr = [0,5,5,0.1,54,0.6,6,0.11,0.1,100]
arr2 = [1,2,3,4,5,6,7,8,9,10,11]
times = 0

def rec(arr):
    global times
    times+=1
    thiscombo = arr[:2]
    if(len(arr)>2):
        nextcombo = rec(arr[1:])
    else:
        nextcombo = [0,0]
    if(thiscombo[0]+thiscombo[1]>nextcombo[0]+nextcombo[1]):
        return thiscombo
    else:
        return nextcombo
print(rec(arr))
print(times)
