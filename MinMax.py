import random
numbers = []
for i in range(0,100):
  numbers.append(random.randint(10,1000))

maximum = numbers[0]
minimum = numbers[0]
ans = 0
for j in range(0,100):
  ans = ans + numbers[j]
  if (maximum < numbers[j]):
    maximum = numbers[j]
    maxindex = j
  elif (minimum > numbers[j]):
    minimum = numbers[j]
    minindex = j

mean = ans/len(numbers)

print("Min=", str(minimum), "at",str(minindex),"\nMax=", str(maximum),"at", str(maxindex))
print("Sum= ", str(ans))
print("Mean= ", str(mean))