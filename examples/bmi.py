# BMI calculator
# formula: BMI = weight / height^2

# Conditions
"""
1. BMI < 18.5: Underweight
2. 18.5 <= BMI < 25: Normal weight
3. 25 <= BMI < 30: Overweight
4. BMI >= 30: Obesity
"""
# Question: Prompt user to enter weight and height (cm), calculate BMI and print the category

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))

# Convert height from cm to meters
height_in_meters = height / 100

# Calculate BMI
bmi = weight / (height_in_meters ** 2)

# Print BMI value
print(f"Your BMI is: {round(bmi, 2)}")

# Conditional Statements (IF....ELSE)
if bmi < 18.5:
    print("You are underweight.")
    
if bmi >= 18.5 and bmi < 25:
    print("You have a normal weight.")
    
if bmi >= 25 and bmi < 30:
    print("You are overweight.")
    
if bmi > 30:
    print("You are obese.")
    
    # ((4 + 7) * (5 ** 6) / 9) - (12 % (3 // 6))