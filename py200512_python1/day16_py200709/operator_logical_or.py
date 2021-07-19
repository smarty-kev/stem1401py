"""
operator
Logical operator

and
or
not

"""

"""
AND

Switch 1. True or False
Switch 2. True or False
Light     True or False

Truth table of AND

S1      S2      L
_________________

T      F      T  (case1)
F      T      T  (case2)
F      F      F  (case3)
T      T      T  (case4)
"""


# case 1
s1 = True
s2 = False
light = s1 or s2
print(light)

# case 2
s1 = False
s2 = True
light = s1 or s2
print(light)

# case 3
s1 = False
s2 = False
light = s1 or s2
print(light)

# case 4
s1 = True
s2 = True
light = s1 or s2
print(light)


# whether I would go out to play?
# condition 1. if I have pocket money; I would go out
# condition 2. if it is sunny; I would go out
# and
hasMoney = True
isSunny = False
go_out_or_not = hasMoney or isSunny
print("I have money? {} and Is it sunny today?{}; My decision is to go out for play? {}".format(hasMoney,isSunny,go_out_or_not))
