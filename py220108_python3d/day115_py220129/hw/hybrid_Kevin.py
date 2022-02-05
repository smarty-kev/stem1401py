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


class Father(Human):
    def __init__(self, hair_color, eye_color, metabolism, diseases, height):
        super().__init__(hair_color, eye_color, metabolism, diseases, height)

    def fathers_behaviour(self):
        print("Behaviours of Dad")


class Child(Mother, Father):
    def __init__(self, hair_color, eye_color, metabolism, diseases, height):
        super().__init__(hair_color, eye_color, metabolism, diseases, height)

    def childs_behaviours(self):
        print("Behaviours of Child")


mom = Mother("brown", "blue", "high", "none", "170cm")
dad = Father("black", "black", "mid", "none", "182cm")
child = Child("black", "blue", "mid", "none", "176cm")

print('MOM:')
mom.mothers_behaviour()
mom.eat()
mom.sleep()
print("===")


print("DAD:")
dad.fathers_behaviour()
print("===")

print("CHILD:")
child.fathers_behaviour()
child.mothers_behaviour()
child.childs_behaviours()
child.eat()
child.sleep()


