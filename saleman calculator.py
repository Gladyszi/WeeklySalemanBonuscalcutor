
print("WELCOME TO ZI WEEKLY SALESMAN BONUS CALCULATOR.")

name = input("What is your name? ")

# The try and except block will catch any error that will disrupt the flow of the program.

try:
    sales_num = int(input("Enter your number of sales: "))
    normal_sales = 10
    bonus_sales_count = 11
    weekly_pay = 1000
    bonus = 250


    if sales_num <= 10:
        sales_short = bonus_sales_count - sales_num
        print(f"You need {sales_short} sale(s) more, to earn a bonus.")
        print(f"Your total weekly pay is: £{weekly_pay}.")

    elif sales_num > 10:
        total_bonus= (sales_num - normal_sales) * bonus
        total_weekly_pay = total_bonus + 1000
        print(f"Congratulations! You have a bonus of: £{total_bonus:}")
        print(f"Your total weekly pay is: £{total_weekly_pay}.")

except ValueError:
    print("Please enter a valid input")

except Exception:
    print("An error occurred, try again with a valid input")