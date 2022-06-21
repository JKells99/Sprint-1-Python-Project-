import math
import datetime
import matplotlib
import FormatValues as FV

# Authors: Cameron D'Amico and Jordan Kelloway
# Date Completed:
# Date Due: June 26, 2022
# Constants
CurDate = datetime.datetime.now()
OWN_CAR_RATE = 85.00
MILEAGE_RATE = 0.17
RENT_CAR_RATE = 65.00
HST_RATE = 0.15

# Functions


def DateConverter(StartDate):
    DateDSP = StartDate.strftime("%B,%d %Y")
    return DateDSP

def EmpTravClaim():
    while True:
        while True:                                                       # Loop For Employee Number
            EmpNumber = input("Enter The Employee Number: (ex 00000)")
            while not EmpNumber.isdigit():
                print("Employee Number Cannot Contain Letters! Please Try Again!")
                EmpNumber = input("Enter The Employee Number: (ex 00000)")
            if len(EmpNumber) < 5:
                print("Employee Number Must Be Exactly 5 Numbers")
            elif len(EmpNumber) > 5:
                print("Employee Number Must Be Exactly 5 Numbers")
            elif EmpNumber == "":
                print("Employee Number Cannont Be Blank")
            else:
                break
        while True:                                                           # Loop For First Name
            EmpFirstName = input("Enter Employee's First Name:").title()
            while not EmpFirstName.isalpha():
                print("Employee Name Can Not Have A Number! Please Try Again")
                EmpFirstName = input("Enter Employee's First Name:").title()
            else:
                break
        while True:                                                             #Loop For Last Name
            EmpLastName = input("Enter Employee's Last Name:").title()
            while not EmpLastName.isalpha():
                print("Employee Last Name Can Not Have A Number! Please Try Again")
                EmpLastName = input("Enter Employee's First Name:").title()
            else:
                break
        while True:                                                            #Loop For Location
            Location = input("Enter The Location Of The Trip:").title()
            while not Location.isalpha():
                print("Location should not contain numbers")
                Location = input("Enter The Location Of The Trip:")
            else:
                break
        while True:                                                           #Loop For Start Date
            try:
                StartDate = input("Enter The Start Date (yyyy-mm-dd):")
                StartDate = datetime.datetime.strptime(StartDate, "%Y-%m-%d")
                break
            except:
                print("Invalid date format please try again (yyyy-mm-dd)")
        while True:                                                  # End Date Loop
            try:
                EndDate = input("Enter The End Date (yyyy-mm-dd):")
                EndDate = datetime.datetime.strptime(EndDate, "%Y-%m-%d")
                if EndDate < StartDate:
                    print("Start Date Cannont Be After The End Date Try Again")
                else:
                    break
            except:
                print("Invalid date format please try again (yyyy-mm-dd)")
        while True:                                                # Loop For Number Of days
            NumDays = (EndDate - StartDate).days
            if NumDays > 7:
                print("Error Input End Date Again. Days Stayed Can Not Exceed 7!")
                EndDate = input("Enter The End Date (yyyy-mm-dd):")
                EndDate = datetime.datetime.strptime(EndDate, "%Y-%m-%d")
            elif NumDays < 7:
                break
            elif NumDays <1:
                print("Error ")

        while True:                                             #Loop For Rent Or Own Validation
            RentOwnVal = input("Did the employee rent or own the vechicle? Enter (O) for Owned or (R) for Rented ").upper()
            if RentOwnVal == "O" or RentOwnVal == "R":
                break
            else:
                print("error")

        while True:                                               #Total Kms travelled loop/validation/decision
            if RentOwnVal == "O":
                TotalKms = int(input("Enter The total Kilomenters travelled "))
                if TotalKms > 2000:
                    print("error try again")
                else:
                    break
            else:
                TotalKms = 0
                break
        while True:                                                        #Claim Type Validation Loop
            ClaimType = input("enter the claim type (S or E)  (S)-Standard or (E)-Executive: ").upper()
            if ClaimType == "S" or ClaimType == "E":
                break
            else:
                print("Error claim type must be S or E ")
    # Calculations Start Here
        DailyAmount = 0
        MileageAmount = TotalKms * MILEAGE_RATE

        if RentOwnVal == "O":    #Daily Amout Calculation
            DailyAmount = (NumDays * OWN_CAR_RATE) + MileageAmount
        elif RentOwnVal == "R":
            MileageAmount = 0
            DailyAmount = NumDays * RENT_CAR_RATE + MileageAmount

        PerdiemAmt = DailyAmount - MileageAmount

        Bonus = 0
        Bonus = BonusCalc(NumDays,TotalKms,ClaimType,StartDate,RentOwnVal)  #Bonus Calculation Using A Function


        if RentOwnVal == "R":                     # Coverting The Single Character To a whole word
            RentMSG = "Rented"
        else:
            RentMSG = "Ownned"
        if ClaimType == "S":
            ClaimMSG = "Standard"
        else:
            ClaimMSG = "Executive"


        HST = HST_RATE * (DailyAmount - MileageAmount)
        ClaimAmt = DailyAmount + Bonus
        TotalClaimAmt = ClaimAmt + HST


        print(HST,DailyAmount,MileageAmount,ClaimMSG,RentMSG,ClaimAmt,TotalClaimAmt,Bonus)
        print()
        print()
        print("The Employees First Name Is {:>}".format(EmpFirstName))
        print()
        print("The Employees Last Name Is  {:>}".format(EmpLastName))
        print()
        print("The Trip Took Place In      {:>}".format(Location))
        print(f"The Trip Stated {DateConverter(StartDate):>}")
        print(f"The Trip Ended  {DateConverter(EndDate):>}")
        print("The Trip Was {:>} Days Long".format(NumDays))
        print("The Employee {:>} The Car ".format(RentMSG))
        print("The Total kilometers travelled are {:>}".format(TotalKms))
        print("The Claim type is                  {:>}".format(ClaimMSG))
        print()
        print(f"The per diem amount is  {FV.FDollar2(PerdiemAmt):>}")
        print(f"The mileage amount is   {FV.FDollar2(MileageAmount):>}")
        print(f"The Bonus is            {FV.FDollar2(BonusCalc(NumDays,TotalKms,ClaimType,StartDate,RentOwnVal)):>}")
        print(f"The Claim Amount Is     {FV.FDollar2(ClaimAmt):>}")
        print(f"The Hst Is              {FV.FDollar2(HST):>}")
        print(f"The Claim Total Is      {FV.FDollar2(TotalClaimAmt):>}")
        print()
        CNT = input("Do you wish to continue? Y/N").upper()
        if CNT == "Y":
            continue
        else:
            break



def BonusCalc(NumDays,TotalKms,ClaimType,StartDate,RentOwnVal):                     # This Function Calculates the bonus value and returns it to the program
    if NumDays > 3:
        Bonus1 = 100
    else:
        Bonus1 = 0
    if TotalKms > 1000 and RentOwnVal == "O":
        Bonus2 = TotalKms * 0.04
    else:
        Bonus2 = 0
    if ClaimType == "E":
        Bonus3 = 45 * NumDays
    else:
        Bonus3 = 0
    if StartDate.month == 12 and StartDate.day >= 15 and StartDate.day <= 22:
        Bonus4 = 50 * NumDays
    else:
        Bonus4 = 0
    Bonus = Bonus1 + Bonus2 + Bonus3 + Bonus4
    return Bonus
def FunIntQues():
    for FizzBuzz in range(1, 101):
        if FizzBuzz % 5 == 0 and FizzBuzz % 8 == 0:
            print("FizzBuzz")
        elif FizzBuzz % 8 == 0:
            print("Buzz")
        elif FizzBuzz % 5 == 0:
            print("Fizz")
        else:
            print(FizzBuzz)
    FizzBuzzMsg = input("Press any key to continue... ")

def StrDates():
     while True:
            EmpFirstName = "Jordan"
            EmpLastName = "Kelloway"
            PhoneNum = "709-596-1234"
            EmpStartDate  = "2022-12-22"
            EmpBDay = "1999-09-09"
            EmpRefNum = (f"{EmpFirstName[0]}{EmpLastName[0]}{PhoneNum[10:12]}{EmpStartDate[5:7]}{EmpBDay[2:4]}")
            print(f"This Is The Employee Reference Number {EmpRefNum}")
            Continue = input("Do you wish to continue? Y/N ( (Y)-to enter another form (N)-to return to main menu").upper()
            print()
            if Continue == "Y":
                continue
            elif Continue =="N":
                break

def GraphMonClaim():
    import matplotlib.pyplot as plt
    import numpy as np
    x = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"]
    y = []
    for months in range(1,13):
        MonthSales = input("Enter Month Sales For " + x[months - 1] + ":")
        y.append(MonthSales)
    plt.title("Monthly Sales Over The Past 12 Months ")
    plt.grid(True)
    plt.plot(x,y)
    plt.xlabel("Months")
    plt.ylabel("Sales Amount")

    print(y)


    plt.show()

while True:
    # Menu for user
    print("NL Chocolate Company")
    print("Travel Claims Processing System")
    print()
    print("1. Enter an Employee Travel Claim.")
    print("2. Fun Interview Question.")
    print("3. Cool Stuff with Strings and Dates.")
    print("4. Graph Monthly Claim Totals.")
    print("5. Quit Program.")
    print()
    while True:
        try:
            Choice = int(input("   Enter choice (1-5): "))
        except:
            print("Choice must be between 1-5 - Please re-enter.")
        else:
            if Choice < 1 or Choice > 5:
                print("Choice must be between 1-5 - Please re-enter.")
            else:
                break
    if Choice == 1:
        EmpTravClaim()
    elif Choice == 2:
        FunIntQues()
    elif Choice == 3:
        StrDates()
    elif Choice == 4:
        GraphMonClaim()
    else:
        break
