class Tool:
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1


tool1 = Tool("screwdriver")
print(f"{tool1.count} tool(s) is(are) created.")

tool2 = Tool("drill")
print(f"{tool2.count} tool(s) is(are) created.")

tool3 = Tool("saw")
print(f"{tool3.count} tool(s) is(are) created.")
