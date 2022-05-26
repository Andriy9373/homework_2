# 2. Create two classes: Person, Cell Phone, one for composition, another one for aggregation.
# a.
class Person:
    """
    Make the class with composition.
    """
    def __init__(self, name, left_arm_info, right_arm_info):
        self.name = name
        self.left_arm = Arm(left_arm_info)
        self.right_arm = Arm(right_arm_info)

    def info_about_arms(self):
        print(f"Left arm: {self.left_arm}. Right arm: {self.right_arm}")

class Arm:
    """
    Make the class with composition.
    """
    def __init__(self, info):
        self.info = info

    def __repr__(self):
        return self.info

# b.
class CellPhone:
    """
    Make the class with aggregation
    """
    def __init__(self, model):
        self.model = model

    def info_model(self):
        print(self.model)

class Screen:
    """
    Make the class with aggregation
    """
    def __init__(self, screen):
        self.screen = screen

    def info_screen(self):
        print(self.screen)

person1 = Person('Jack', 'i have a watch', 'i have a tattoo')
person2 = Person('John', 'i have a clear arm', 'i have a watch')
person1.info_about_arms()
person2.info_about_arms()

cell_phone = CellPhone('IPhone XS')
cell_phone.info_model()
screen = Screen('1440 x 2560')
screen.info_screen()