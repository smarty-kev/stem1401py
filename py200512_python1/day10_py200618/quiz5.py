mytools = [
    "pencil",
    "pen",
    "glue",
    "eraser",
    "scissors",
    "sharpener"
]

print(mytools[0])
print(mytools[5])

mytools[3] = 999

fruits = (
    "watermelon",
    "pear",
    "apple",
    "lemon",
    "orange",
    "strawberry"
)

print(fruits[0])
print(fruits[5])

# 6.5 Can you change the value of items in a tuple : b) No


set1 = {1,1,2,2,3,3}
# answer = 1, 2, 3,     or     2, 1, 3 or 3, 1, 2,      or      2, 3, 1,      or      3, 2, 1,     or     1, 3, 2

dict1 = {
    "Math" : "Mathematics",
    "ECR"  : "Éthique et Culture Religieuse"
}
print(dict1["Math"])
print(dict1["ECR"])