def findIt (a, e):
    for i in range (len(a)):
        if (a[i] == e):
            return i
    return -1

# ************MAIN******************

a = ["asphalt", "assignment", "asterisk", "attorneys", "audible"]

e = input("Enter the word you're looking for: ")
print(findIt(a,e))