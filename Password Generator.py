
str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12,3456789!@#$%^&*"
import random


def pass_generator():
    list = ""
    n = int(input("How many characters do you wish your password to be ?: "))
    for i in range(1,n+1):
        a = random.choice(str)
        list += a
    print("Your password generated is :",list)

pass_generator()


