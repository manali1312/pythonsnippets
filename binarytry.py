sampleList = [12,34,65,78,98,109,234,543,789]
def binarytry(sampleList,num):
    sampleList.sort()
    start = 0
    end = len(sampleList)

    while(start<=end):
        mid = int((start+end)/2)
        print(start," ",mid," ",end)
        if(sampleList[mid]==num):
            return True
        elif (num<sampleList[mid]):
            end = mid
        else:
            start = mid

    return False

print(binarytry(sampleList,9))
        

