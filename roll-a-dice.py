import random

yesOrno = input("Press y to roll again and n to exit")
response = str("y")
no = random.randint(1, 6)


while response == "y":
    print(no, end = '\r')
    
print(yesOrno, end = '\r')