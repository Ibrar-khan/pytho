

'''num = 12;
if num > 18:
    print("you are adult");
elif num >= 10:
    print("you are teenager");
else:
    print("you are child")

#data types in python
#integer
x = 5;
y = -5;
print(type(y))
#float
z = 1.5;
print(type(z))
#complex numbers
c = 3 + 4j;
print(type(c))
#string
name = "Alice"
print(type(name))
#string operation
text = "Python"
print(text[0])
print(text[1:4])
print(text.upper())
#list
fruits = ["apple", "Mango", "Banana", "Strawberry", "cherry"]
fruits.append("orange");
print(fruits);
#tuple
colors = ("red", "green", "Blue");
print(colors)
print(type(colors))

#range
r = range(5)
print(list(r))

#set data type
numbers = {1, 2, 3, 4, 5, 6}
print(numbers)


#mapping data types
person = {"name": "Alice", "age":27, "job":"Softwarer Engineer"}
print(person)

#boolean
is_raining = True;
is_sunny = False;
print(type(is_raining))

#type conversion

x = "123"
y = 34;
z = int(x)+y #explicit type conversion
print(z)

#implicit conversion
x = 10;
y = 34.5;
z = x+y+1;
print(z)'''

#loops in python

word = "Hello";
for letter in word:
    print(letter)

fruits = ["banana","apple", "cherry"]
for fruit in fruits:
    print(fruit);

#iterating over a dictionary
person = {"name": "Alice", "age":25, "job":"Software Engineer"}
for key,value in person.items():
    print(f"{key}: {value}")

#while loop
count =1;
while count<=5:
    print(count)
    count +=1;

#operator in python
#mathematical operators in python
a=30
b=5;
c= 3;
print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b);
print("floor division:", b//c)
print("Modulus:", a%b)
print("Exponantiation:", a**b)

#relational or  comparison operator
x = 200;
y = 20;
print("Equal to:", x==y)
print("Not equal to:", x!=y)
print("Greater than", x>y)
print("Greater or equal to:", x>=y)
print("Less than or equal to:", x<=y)

#logical operators
p = 20
q = 10
print("AND:", (p>q) and (q<p))
print("OR:", (p< 10) or ( p>10))
print("NOT:", not(p>q))

#assigment operator

a = 5;
a +=3; # a = a+3
print(a)
a -=3;
print(a)
a *=3; # a = a*3
print(a)