"""
multiple inheritance
"""


class ParentA:
    def sleep(self):
        print("short sleep behaviour")


class ParentB:
    def sleep(self):
        print("long sleep behaviour")


class Child(ParentA, ParentB):
    pass


class Child2(ParentB, ParentA):
    pass


peter = Child()
peter.sleep()

jack = Child2()
jack.sleep()
