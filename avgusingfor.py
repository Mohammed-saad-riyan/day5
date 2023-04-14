student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height

no_students = 0
for students in student_heights:
    no_students += 1
averg_height = total_height / no_students
print (round(averg_height))