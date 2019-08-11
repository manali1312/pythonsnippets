def isPalindrome(text):
    fullLen = len(text)
    halfLen = len(text)/2  
    print(halfLen)

    for i in range(0,int(halfLen)):
        lChar = text[i]
        rChar = text[fullLen -i -1]
        if (lChar!=rChar):
            #print("Not a palindrome")
            return False
    else:
        #print("Yay...!!!it's a palindrome")
        return True

print(isPalindrome("ABSDGDTH"))
print(isPalindrome("123321"))
print(isPalindrome("zxcvcxz"))
