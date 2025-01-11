
# import emoji # type: ignore
# print("Hello World")

# print("*"*10)



# # Using emoji shortcodes
# print(emoji.emojize(":grinning_face:"))  # 😀
# print(emoji.emojize(":red_heart:"))      # ❤️
# print("😀")
# print("Hello ❤️ World!")


# # # Disabling the emoji if not supported
# # print(emoji.emojize(":grinning_face:", use_aliases=True))

# x =float(5)
# y = (10)
# z = x+y
# print(type(z))
# print("Additon of x+y is", z) 
# firstName = "Ibrar "
# lastName = "Hussain"
# fullName = firstName + lastName
# print("Welcome to ",fullName)

# #global variables
# x = "Awesome"
# def myfunc():
#     print("Python is "+x)
    
# myfunc()
# print(type(x))

#Data types

# lst = ["Apple", "Mango", "Grapes", "Banana", "Orange", "Cherry"]
# # print(lst[1])
# # for item in lst:
# #     print(item)
# # for index, item in enumerate(lst):
# #     print(f"Index {index}:{item}")
# # print("Length of list is:",len(lst))

# lst.append("Berry")
# for item in lst:
#     print(item)
    
# numbers = [1, 2, 3, 4, 5, 6]
# numbers.insert(2, 7)
# for num in  numbers:
#     print(num)
    
# #Add element from another list

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list1.extend(list2)
# print(list1)

# #Remove elements
# animals = ["Cat", "Dog", "Lion"]
# animals.remove("Dog")
# print(animals)

# #Remove element by index

# remove_animal = animals.pop(1)
# print(remove_animal)
# print(animals)

# index = numbers.index(7)
# print(index)

# item = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 2, 3, 7,]
# count = item.count(5)
# print(count)

# letters = ["Abrar", "Hussain", "C", "D"]
# letters.reverse()
# print(letters)

# #sort the list method Ascending
# item.sort()
# print(item)
# #Descending
# item.sort(reverse=True)
# print(item)


numbers = [4,1,5,3,2,7,6]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

#create copy of a list
original = [1,3,4,5]
copied = original.copy()
copied.append(2)
print(copied)
print(original)

#Remove All elements from a list
numbers.clear()
print(numbers) # output: []

#length of a list

print(len(numbers)) #output: 0

#calculate of the elements

num = [12,12,12]
print(sum(num))

#find the smallest and the largest value
num1= [12, 34, 56, 78,]
print(max(num1))
print(min(num1))