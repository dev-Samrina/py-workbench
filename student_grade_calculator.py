print(input("Student Name: "))
first_subject=float(input("Your first subject marks: "))
second_subject=float(input("Your second subject marks: "))
third_subject=float(input("Your third subject marks: "))
total_marks = first_subject + second_subject + third_subject
print(f"Total marks: {total_marks}")
Average_marks=total_marks/3
print(f"Average marks: {Average_marks}")
if Average_marks >=80:
    print("Grade:A+")
elif Average_marks >=70:
    print("Grade:A")
elif Average_marks>=60:
     print("Grade:B")
elif Average_marks >=50:
     print("Grade:C")
else:
   
    print("Grade:F")

