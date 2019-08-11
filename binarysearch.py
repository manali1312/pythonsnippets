sampleList = [12,34,65,78,98,109,234,543,789]
def reccursiveBinSearch(sampleList,start,end,reqnum):
    while (start <= end):
        mid = int((start+end)/2)
        if(sampleList[mid]==reqnum):
            return True
        elif(sampleList[mid]>reqnum):
            return reccursiveBinSearch(sampleList,start,mid-1,reqnum)
        else:
            return reccursiveBinSearch(sampleList,mid+1,end,reqnum)
    return False
print(reccursiveBinSearch(sampleList,0,len(sampleList)-1,109))
'''
def binarySearch(sampleList,reqnum):
    sampleList.sort()
    start = 0
    end = len(sampleList)
    
    while start <= end:
        mid = int((start + end) / 2)
        print(start," ",mid," ",end)
        
        if(sampleList[mid] == reqnum):
            return True
        elif(reqnum < sampleList[mid]):
            end = mid-1
        else:
            start =  mid+1
    return False
    
    
print(binarySearch(sampleList,107))
'''