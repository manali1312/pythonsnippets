records = [("manali",25),("devang",21),("utkarsha",29),("sohini",14)]
def takesecond(marks):
        return marks[0]
records.sort(key=records[0][1], reverse = True)
print(records)

print(records[0][1])