"""
Inheritance type : hybrid inheritance
Description
Human(hair_color, eye_color, metabolism, diseases, height)
Mother(mothers_behaviour()) # genes of mom
Father(fathers_behaviour()) # genes of dad
Child(childs_behaviour())  # genes of child
both mother and father are humans
Mother and Father have different genes, but the Child has genes from the Mom and the Dad
"""


class Human:
    def __init__(self, hair_color, eye_color, metabolism, diseases, height):
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.metabolism = metabolism
        self.diseases = diseases
        self.height = height

    def eat(self):
        print("miam")

    def sleep(self):
        print("ZZZZZZZZZZ")


class Mother(Human):
    def __init__(self, hair_color, eye_color, metabolism, diseases, height):
        super().__init__(hair_color, eye_color, metabolism, diseases, height)

    def mothers_behaviour(self):
        print("Behaviours of Mom")

    def behaviour(self):
        print("Personality 1")  # example likes to run


class Father(Human):
    def __init__(self, hair_color, eye_color, metabolism, diseases, height):
        super().__init__(hair_color, eye_color, metabolism, diseases, height)

    def fathers_behaviour(self):
        print("Behaviours of Dad")

    def behaviour(self):
        print("Personality 2")  # example likes to jump


class Child(Mother, Father):
    def __init__(self, hair_color, eye_color, metabolism, diseases, height):
        super().__init__(hair_color, eye_color, metabolism, diseases, height)

    def childs_behaviours(self):
        print("Behaviours of Child")


class Child2(Father, Mother):
    def __init__(self, hair_color, eye_color, metabolism, diseases, height):
        super().__init__(hair_color, eye_color, metabolism, diseases, height)

    def childs_behaviours(self):
        print("Behaviours of Child")


# family
mom = Mother("brown", "blue", "high", "none", "170cm")
dad = Father("black", "black", "mid", "none", "182cm")
child = Child("black", "blue", "mid", "none", "176cm")
child2 = Child2("brown", "blue", "high", "none", "174cm")

# main program
print("Common behaviours:")
mom.eat(); dad.eat()
child.eat(); child2.eat()
print("=====\nParent's behaviours.")

mom.mothers_behaviour()
mom.behaviour()
dad.fathers_behaviour()
dad.behaviour()
print("=======\nChild 1")

child.fathers_behaviour()
child.mothers_behaviour()
child.behaviour()
child.childs_behaviours()
print("=======\nChild 2")

child2.fathers_behaviour()
child2.mothers_behaviour()
child2.behaviour()
child2.childs_behaviours()
