class Tool:
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1


tool1 = Tool("hammer")
print(f"{tool1.count} tool(s) is(are) created.")
print()

tool1.count = 99
print("The instance tool1 has extra property: count")
print(f"{tool1.count} tools are created")
print()

print("Now instance property has nothing to do with class property: count")
print(f"{Tool.count} tool is created")

tool2 = Tool("drill")
print(f"{Tool.count} tool is created")

tool3 = Tool("screwdriver")
print(f"{tool3.__class__.count} tool is created")
