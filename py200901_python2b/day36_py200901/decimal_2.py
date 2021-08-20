"""

"""

from decimal import Decimal as D

# import decimal

print(D(1.1)+ D(2.2))

print(D('1.1')+ D('2.2'))

result = (D('1.1')+ D('2.2'))
print("The result is {}, and the data type is {}".format(result, type(result)))

# example 1
res = D("1.2")*D('2.50')
print(res)

res = D("1.2")*D('2.5')
print(res)

res = D("1.2")*D('2.500')
print(res)


