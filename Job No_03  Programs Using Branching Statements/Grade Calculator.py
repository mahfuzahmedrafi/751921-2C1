score = float(input("Enter the student's score: "))

if score >= 80:
    grade = 'A+'
elif 70 <= score < 80:
    grade = 'A'
elif 60 <= score < 70:
    grade = 'B'
elif 50 <= score < 60:
    grade = 'C'
elif 40 <= score < 50:
    grade = 'D'
else:
    grade = 'F'

print(f"The student's grade is: {grade}")
