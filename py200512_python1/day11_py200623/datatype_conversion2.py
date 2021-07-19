"""
implicit conversion
explicit conversion

Type Conversion is the conversion of object from one data type to another data type.
Implicit Type Conversion is automatically performed by the Python interpreter.
Python avoids the loss of data in Implicit Type Conversion.
Explicit Type Conversion is also called Type Casting, the data types of object are converted using predefined function by user.
In Type Casting loss of data may occur as we enforce the object to specific data type.
"""

# case 1
result = 1 + 1.2
print(result, type(result))


# case 2
# result = '1' + 1.2
result = float('1') + 1.2
print(result)


# case 3
# float -> int
result = int(1.23)
print(result)

# int -> float
result = float(1)
print(result)