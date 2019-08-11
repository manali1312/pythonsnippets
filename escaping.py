print("\"Hello\"")
print("\n")

testString="""You can vote only if your name appears in the Voter List 
(also known as Electoral Roll). Voters can also 
find information on Polling Booths, Contesting candidates, 
Election Dates & Timings, Identity cards and EVM."""


for letter in testString:
    if(letter=="\n"):
        print("\\n")
    else:
        print(letter,end="")