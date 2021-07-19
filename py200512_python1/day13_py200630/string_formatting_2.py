"""
string formatting
"""

print("Hello {0}, your balance is {1}!".format('Adam', 230.2346))

# Lenght or space
print("Hello {0}, your balance is {1:9.3f}!".format('Adam', 230.2346))
print("Hello {0}, your balance is {1:10.3f}!".format('Adam', 230.2346))
print("Hello {0}, your balance is {1:11.3f}!".format('Adam', 230.2346))
print("Hello {0}, your balance is {1:12.3f}!".format('Adam', 230.2346))

print("Hello {0:10}, your balance is {1:12.3f}!".format('Adam', 230.2346))
print()

# decimal spaces to show
print("Hello {0}, your balance is {1:9.1f}!".format('Adam', 230.2346))
print("Hello {0}, your balance is {1:9.2f}!".format('Adam', 230.2346))
print("Hello {0}, your balance is {1:9.3f}!".format('Adam', 230.2346))

print("Hello {0}, your balance is {1:9.3f}!".format('Adam', 230.2344))
print("Hello {0}, your balance is {1:9.4f}!".format('Adam', 230.2346))
print("Hello {0}, your balance is {1:9.4f}!".format('Adam', 230.23467))

