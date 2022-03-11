"""

"""


class GrandParent:
    # not accessed in this case
    def __init__(self):
        print("GrandParent __init__() called.")


class Son(GrandParent):
    def __init__(self):
        print("Son __init__() called.")


class GrandSon(Son):
    pass


# main
gs1 = GrandSon()
