medications = ["Lisinopril", "Aspirin", "Metformin", "Atorvastatin"]
# print(medications)
name = "David"

numbers = [16, 72, 3, 49, 5, 11, 4, 1, 99]

# medications.append(name)
# print(medications)

# medications.remove("Metformin")

# print(medications)

# removed = medications.pop(1)
# print(medications)
# print(removed)

# medications.insert(1, "Hello")

numbers.sort(reverse=False)
# print(numbers)


# def custom_sorting(a, b):
#     c = a + b

#     return c


# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))


# result = custom_sorting(a, b)

# print(result - 2)


# print(medications[0])
# print(medications[1])
# print(medications[2])
# print(medications[3])

# For Loop

# for x in medications:
#     print(x)

# a = 5
# while a < 8:
#     print("Hello")
#     print(a)
#     a =  a + 1 # a += 1
#     print(a)



# print(list(range(100)))

numbers = [x for x in range(100) if x % 2 == 0]

print(numbers)