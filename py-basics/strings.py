# Basic String Functions

myStr = "Welcome to - my github"

# Finding LENGTH of the string
length =  len(myStr)
# as length is integer, hence we have to use str()
# to convert it into string
print ("Length is: " + str(length))

# Use FIND function to look for substring
subStr = "to"
lookfor = myStr.find(subStr)
print ("Substring found at: " + str(lookfor))

# Use REPLACE to change a part of string
print (myStr.replace("to", "all"))
# Use SPLIT to break the string
myNewStr = myStr.split('-')
# all the parts are saved
print (myNewStr[0])
print (myNewStr[1])

tcsStr = "Python Test Project"
print(tcsStr.split("Python")[1][1:5])