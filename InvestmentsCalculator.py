# Jack Criscione - Investments Calculator v1 - February 23rd, 2025 - Personal Project

# introduction
print("This calculator will calculate the amount of money to invest in certain ETFs based on your weekly income.")

# Income

rate = float(input("Enter your hourly pay: "))

hours = float(input("Enter the number of hours you worked: "))

net_pay = rate * hours * (1-0.25-0.14) # estimated tax deduction and 25% 401k contribution
net_pay = round(net_pay, 2)
print("------------------------------------------")
print("Here is your net pay for the week: ", net_pay)
print("     (after tax deductions and your 401k contribution)")

# Investment amount based on income
print("----------------------------------------------")
print("How much money do you want to invest?")
print("Enter 1 to invest a set amount of your income. ")
print("Enter 2 to invest a percent of your income.    ")
print("----------------------------------------------")

loop = 0
x = 0
choice = 0

# loop to test for your choice
while loop == 0:
    choice = input("Enter your choice here: ")

    if choice == "1" or choice == "one" or choice == "One":
        choice = 1
        x = float(input("How much money do you want to invest in dollars? "))
        loop = 1

    elif choice == "2" or choice == "two" or choice == "Two":
        choice = 2
        x = float(input("What percent of your income do you want to invest? "))
        loop = 1

    else:
        print("Invalid input. Please try again.")

if choice == 2: x = net_pay * (x/100) # math if based on percent of income

# Calculation for the amount of money to invest in the VOO, VTI, VT, and VGT ETFs
VOO = round(x * 0.40, 2) # 40 percent in VOO
VTI = round(x * 0.30, 2) # 30 percent in VTI
VT = round(x * 0.20, 2) # 20 percent in VT
VGT = round(x * 0.10,2) # 10 percent in VGT

# more output
print("------------------------------------------------------------------")
print("Invest your money into the following ETFs for this week:")
print("40% - VOO - Vanguard S&P 500 ETF - $", VOO)
print("30% - VTI - Vanguard Total Stock Market Index Fund ETF - $", VTI)
print("20% - VT - Vanguard Total World Stock Index Fund ETF - $", VT)
print("10% - VGT - Vanguard Information Technology Index Fund ETF - $", VGT)
print("------------------------------------------------------------------")

# money left over
x = round(x, 2)
print("Total money invested: ", x)
leftovers = net_pay - x
print("Your money left over is: ", leftovers)