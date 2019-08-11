

marks=[('MandarP',[23,65,70]),('Manali',[22,56,98]),('Charu',[26,78,85])]

def getMarks(record):
    summation = 0
    for num in record[1]:
        summation += num
    return summation
marks.sort(key=getMarks)


print(marks)