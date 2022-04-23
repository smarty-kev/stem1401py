class Tool:
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1


tool1 = Tool("screwdriver")
print(f"{Tool.count} tool(s) is(are) created.")

tool2 = Tool("drill")
print(f"{Tool.count} tool(s) is(are) created.")
