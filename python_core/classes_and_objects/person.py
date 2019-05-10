class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    """ Multiple constructors are not possible """
    # def __init__(self):
    #    pass

    def print(self):
        print(self.name + ' is ' + str(self.age) + ' old!')
