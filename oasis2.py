def cal_bmi(w, h):
    bmi = w / h ** 2
    return bmi

def my_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal weight"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    try:
        w = float(input("Enter your weight in kilograms: "))
        h = float(input("Enter your height in meters: "))

        if w <= 0 or h <= 0:
            print("Invalid input! Try Again.")
        else:
            bmi = cal_bmi(w, h)
            category = my_bmi(bmi)

            print(f"Your BMI is: {bmi:.2f}")
            print("Category:", category)

    except ValueError:
        print("Invalid input!")

if __name__ == "__main__":
    main()