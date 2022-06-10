
def tips_calculator() -> None:
    print("Welcome to  the Tips calculator program!")
    total = input("What is the total  bill? $")
    people = input("How many people at the table? ")
    percentage = input("What percentage tip would you like to give?  10, 12, or 15? ")
    money =  (float(total) *  (1 + float(percentage) / 100)) / int(people)
    print(f"Each person should pay: ${money:.2f}")
    


def BMI_calculator() -> None:
    height = input("enter your height in m: ")
    weight = input("enter your weight in kg: ")
    BMI = float(weight) / (float(height)  ** 2)
    print(int(BMI))
    
if __name__ == "__main__": 
    tips_calculator()
    # BMI_calculator()
