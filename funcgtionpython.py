#funtions in python
def calculateGmean(a , b):
     mean = (a*b)/(a+b)
     print(mean)

a = 9
b = 8
calculateGmean(a , b)
c = 8
d = 7
calculateGmean(c , d)

#mutliple values like marks, roll number, address, etc
marks = [20, 13, 24]
print(marks)
print(type(marks))

print(marks[0])
print(marks[1])
print(marks[2])

l = [45, 11, 2, 2, 7, 6]
print(l.count(2))
l.sort(reverse=True)
print(l)

