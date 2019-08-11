#max_list1 = ["a","cncdh","eh","fle","dlop"]
#max_list = [12,35,578,243,79]
def max(i,j):
        if (i<j):
            return j
        return i

def maxNumInList(max_list):


    if len(max_list) != 0:

        max_tuples = [(1,5),(2,4),(8,5)]
        result = max_list[0]
    
        for num in max_list:
            result = max(num,result)
        return result
    else:
        return "empty list"
    
a = maxNumInList([12,65,987,57,87])
print(a)





