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
    def __init__(self):
        print("GrandSon __init__() called.")


# main
gs1 = GrandSon()
