from colorama import *
init(autoreset=True)

def choices(*arg):
    print("What will you do?")
    for _i, i in enumerate(arg):
        print(f"{_i}. {i}")
    print("\n")

print("You are Mario. You have arrived in the castle, years after Princess Peach's funeral, which you could not attend.")
print(f"It {Style.BRIGHT}has{Style.RESET_ALL} been so long since you last stepped foot in the castle... But you {Style.BRIGHT}must do it...")
while True:
    