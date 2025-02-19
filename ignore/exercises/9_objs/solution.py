#TASK: make a simple class method

class ur_class:
    def __init__(self, name="harlee"):
        self.name = name

    #try adding a class method named "change_name" that changes the name here
    def change_name(self, new_name):
        self.name = new_name 

fancy_class = ur_class()

fancy_class.change_name(new_name="put anything here");

tester.checker_9(fancy_class.name)
