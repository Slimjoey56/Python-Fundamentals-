#Backwards Slicing Techniques:
# Using Negative Steps to Reverse Python Strings
letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]
print(backwards)

#mini challenge : using the letters
# from the video, add some code to create the following slices
#1.Create a slice that produces the character qpo
print(letters[16:-13:-1])
#or
print(letters[16:13:-1])
#slice string to produce edcba
print(letters[4:-27:-1])
#or
print(letters[4::-1])
#slice  the string to produce the last 8 characters , in reverse order
print(letters[25:-9:-1])
#or
print(letters[-1:17:-1])
#or
print(letters[-1:-9:-1])

print(letters[-4:])
print(letters[-1:])
print(letters[:1])
print(letters[0])
