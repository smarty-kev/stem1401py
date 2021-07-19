"""
exercise
"""

# 1
score = float(input("Score of the student: "))

if score >= 90:
    print("The student got A")
elif score < 90 and score >= 80:
    print("The student got B")
elif score < 80 and score >= 70:
    print("The student got C.")
else:
    print("The student got D")



