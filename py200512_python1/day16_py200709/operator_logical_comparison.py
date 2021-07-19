"""
combine boolean literals, comparison expression, logical comparison
"""

# case 1.
result = 5 > 12 and 5 < 3
print("5 > 12 and 5 < 3 is",result)

# case 2.
result = 5 > 12 or 5 > 3
print("5 > 12 or 5 > 3 is",result)

# case 3.
result = 5 < 12 or 5 > 3 and False
print("5 < 12 or 5 > 3 is False is",result)

result = 5 < 12 or (5 > 3 and False)
print("5 < 12 or 5 > 3 is False is",result)

result = (5 < 12 or 5 > 3) and False
print("5 < 12 or 5 > 3 is False is",result)


# game RTS
# cond. 1 eliminate all the enemies
# cond. 2 destroy all the constructions
# cond. 3 escort the specified characters


# difficulty level 1
"""
condition 1 or condition 2 or condition 3
"""

# difficulty level 2
"""
(condition 1 and condition 2) or condition 3
"""

# difficulty level 3
"""
condition 1 and condition 2 and condition 3
"""
