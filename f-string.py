#Exploring Python 3.6 f-strings: A Modern Approach to String Formatting
#different ways to write a string
from tkinter.font import names

age = 25
name = "DmonBowHunter"
print(age)

age_in_words = "2 years"
print(name + f" is {age} years old")

print(f"Pi is approximately {22/7:<12.50f}")
pi =  22/7
print(f"Pi is approximately {pi:12.50f}")
