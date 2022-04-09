#
# try:
#     with open("test.txt") as file:
#         print(file.read())
#
# except AttributeError as e:
#     print(e)
#     print("Something went wrong")
#
# except FileNotFoundError as e:
#     print(e)
#     print("Please check your code")
#
# except Exception:
#     print("None")



text="\nCongrats!"

with open("new_file", "a")as file:
    file.write(text)
