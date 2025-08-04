age = int(input("What's your baby's age: "))

if age <= 2:
    baby = input("is your baby is boy or girl?").lower()

    if baby == "boy":
        print("your baby should drink water")

    else:
        print("your baby should drink milk")
        
else:
  print("you have not a baby")



