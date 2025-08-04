age = int(input("What's your age: "))

if age >= 60:
    print("You are a senior") 

elif age >= 18:
    print("You are an adult")

elif age >= 13:
    print("You are teenage")

elif age >= 5:
    print("You are a child")

elif age >= 0:
    print("You are a baby")    

else:
    print("invalid age")