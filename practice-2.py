# student_eligible= True
#
# name=input("What is your name?\n")
# age=int(input("How old are you?\n "))
# score= int(input("what is your total assessment score? "))
#
# if 17 == age >= 21 and score >= 80:
#     print("You are eligible for the student loan, congrats!")
# else:
#     print("Not eligible")
#

#user=input("Type a text\n")


# if user != user.isalpha():
#     print("Please type alphabets only")
# elif user == user.lower():
#     print("Your text is lowercase")
# elif user==user.upper():
#     print("Your text is uppercase")
#
# else:
#     print("Type correctly please")


# try:
#     user = input("Enter a number: ")
#     user_input = int(user)
#     power = input("Enter the power: ")
#     power_num = int(power)
#     result = user_input ** power_num
#     print(result)
#
#     if result % 2 == 0:
#         print("This is an even number")
#
#     elif result % 2 != 0:
#         print("This is an odd number")
#
# except Exception:
#     print("Error")


   #
   # else:
   #  print("Hey you, please enter a valid number")




try:
    hours = int(input("Enter the hours worked:"))
    rate = float(input("Enter your daily pay rate: "))
    currency="£"
except:
    print("Error")
    quit()
if hours > 40:
    pay = (hours - 40 )* rate * 1.5 + (40 * rate)
    print(f"Your pay is  {pay}")

else:
    pay = hours * rate
    print(f"Your pay is {currency} {pay} ")