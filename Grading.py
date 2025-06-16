grade1 = float(input("Enter your 1st grade: "))
grade2 = float(input("Enter your 2nd grade: "))
grade3 = float(input("Enter your 3rd grade: "))
grade4 = float(input("Enter your 4th grade: "))

averageGrade = ((grade1 + grade2 + grade3 + grade4) / 4)
if averageGrade >= 90:
    yourGrade = "A"
elif averageGrade >= 80:
    yourGrade = "B"
elif averageGrade >= 70:
    yourGrade = "C"
elif averageGrade >= 60:
    yourGrade = "D"
else:
    yourGrade = "F"

print("Your average grade is ", averageGrade)
print("Your grade letter is ", yourGrade)

