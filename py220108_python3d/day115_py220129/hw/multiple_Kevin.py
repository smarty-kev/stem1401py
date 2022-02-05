"""
Inheritance type : multiple inheritance
Description
Mother(hair_color, eye_color, metabolism, diseases, height, mothers_behaviour()) # genes of mom
Father(hair_color, eye_color, metabolism, diseases, height, fathers_behaviour()) # genes of dad
Child(childs_behaviour())  # genes of child
Mother and Father have different genes, but the Child has genes from the Mom and the Dad
"""


class Mother:
    def __init__(self, hair_color, eye_color, metabolism, diseases, height):
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.metabolism = metabolism
        self.diseases = diseases
        self.height = height

    def mothers_behaviour(self):
        print("Behaviours of Mom")


class Father:
    def __init__(self, hair_color, eye_color, metabolism, diseases, height):
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.metabolism = metabolism
        self.diseases = diseases
        self.height = height

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

mom.mothers_behaviour()
dad.fathers_behaviour()

child.fathers_behaviour()
child.mothers_behaviour()
child.childs_behaviours()


