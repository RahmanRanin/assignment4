def grading(score):
        if score < 0 or score > 100:
            print("Error, please enter numeric input between 0 and 100")
        elif score >= 90:
            return "Your grade is A"
        elif score >= 80:
            return "Your grade is B"
        elif score >= 70:
            return "Your grade is C"
        elif score >= 60:
            return "Your grade is D"
        else: 
            return "Your grade is F"

try:
    score = float(input("Please enter your score: "))
    grade = grading(score)
    print(grade)
except ValueError:
    print("Error, please enter numeric input between 0 and 100.")