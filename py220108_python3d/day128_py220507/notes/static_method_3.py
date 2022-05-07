"""
example of static method
"""


class Dog:
    @staticmethod
    def run():
        # no need to use 'self'
        print("A dog runs.")


Dog.run()
Dog.run()
