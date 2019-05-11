
name = input("Enter name of the student: ")
eng = int(input("Enter marks for English: "))
sindhi = int(input("Enter marks for Sindhi: "))
pst = int(input("Enter marks for PST: "))
chem = int(input("Enter marks for Chemistry: "))
bio = int(input("Enter marks for Biology: "))

print("For Student " + name + ":  Grade and average marks are as follows: ")
total = eng + sindhi + pst + chem + bio
avg = total/5
if avg >= 90:
  print("Grade: 'A'\nAverage Marks: " + str(avg))
elif avg >=80 and avg <90:
  print("Grade: 'B'\nAverage Marks: " + str(avg))
elif avg >= 70 and avg <80:
  print("Grade: 'C'\nAverage Marks: " + str(avg))
elif avg >=60 and avg <70:
  print("Grade: 'D'\nAverage Marks: " + str(avg))
elif avg >=50 and avg <60:
  print("Grade: 'E'\nAverage Marks: " + str(avg))
else:
  print("Grade: FAIL \nAverage Marks: " + str(avg))