"""
index()

listname.index() - Return the index of the first matched item
"""

my_list = ['p','r','o','b','l','e','m']

index_o = my_list.index('o')
print(index_o)

index_e = my_list.index('e')
print(index_e)

# how to find the index of the second occurrence of item
my_list = ['p','r','o','b','l','e','m','o']
index_o = my_list.index('o')
print(index_o)


last_o = index_o
next_o = my_list.index('o', last_o+1)
print(next_o)