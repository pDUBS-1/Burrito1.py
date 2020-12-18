#Copy your Burrito class from the last exercise. Now,
#write a getter and a setter method for each attribute. 
#Each setter should accept a value as an argument. If the 
#value is a valid value, it should set the corresponding 
#attribute to the given value. Otherwise, it should set the 
#attribute to False.
#
#Edit the constructor to use these new setters and getters.
#In other words, if we were to call:
#
# new_burrito = Burrito("spaghetti", True, True, False)
#
#new_burrito.meat would be False because "spaghetti" is not
#one of the valid options. Note that you should NOT try to
#check if the new value is valid in both the constructor and
#the setter: instead, just call the setter from the
#constructor using something like self.set_meat(meat).
#
#Valid values for each setter are as follows:
#
# - set_meat: "chicken", "pork", "steak", "tofu", False
# - set_to_go: True, False
# - set_rice: "brown", "white", False
# - set_beans: "black", "pinto", False
# - set_extra_meat: True, False
# - set_guacamole: True, False
# - set_cheese: True, False
# - set_pico: True, False
# - set_corn: True, False
#
#Make sure you name each setter with the format: 
#"set_some_attribute" and "get_some_attribute"
#
#For example, the getter for meat would be get_meat. The
#getter for to_go would be get_to_go.
#
#Hint: Your code is going to end up *very* long. This
#will be the longest program you've written so far, but
#it isn't the most complex. Complexity and length are
#often very different!
#
#Hint 2: Checking for valid values will be much easier
#if you make a list of valid values for each attribute
#and check the new value against that.


#Write your code here!
class Burrito:
    def __init__(self, meat, to_go, rice, beans, extra_meat=False, guacamole=False, cheese=False, pico=False,corn=False):
        self.meat = Meat(meat)
        self.to_go = To_go(to_go)
        self.rice = Rice(rice)
        self.beans = Beans(beans)
        self.extra_meat = Extra_meat(extra_meat)
        self.guacamole = Guacamole(guacamole)
        self.cheese = Cheese(cheese)
        self.pico = Pico(pico)
        self.corn = Corn(corn)

class Meat:
    def __init__(self, value=False):
        self.set_meat(value)    

    def set_meat(self, value):
        if value in ["chicken", "pork", "steak", "tofu"]:
            self.value = value

        else:
            self.value = False

    def get_meat(self):
        return self.value

class To_go:
    def __init__(self, value):
        self.set_to_go(value)   
    
    def set_to_go(self, value):
        if value == True:
            self.value = value
        else:
            self.value = False

    def get_to_go(self):
        return self.value

class Rice:
    def __init__(self, value):
        self.set_rice(value)    
    
    def set_rice(self, value):
        if value in ["brown", "white"]:
            self.value = value
        else:
            self.value = False

    def get_rice(self):
        return self.value
    
class Beans:
    def __init__(self, value):
        self.set_beans(value)    
    
    def set_beans(self, value):
        if value in ["black", "pinto"]:
            self.value = value
        else:
            self.value = False

    def get_beans(self):
        return self.value

class Extra_meat:
    def __init__(self, value):
        self.set_extra_meat(value)    
    
    def set_extra_meat(self, value):
        if value == True:
            self.value = value
        else:
            self.value = False

    def get_extra_meat(self):
        return self.value

class Guacamole:
    def __init__(self, value):
        self.set_guacamole(value)   
    
    def set_guacamole(self, value):
        if value == True:
            self.value = value
        else:
            self.value = False

    def get_guacamole(self):
        return self.value
    
class Cheese:
    def __init__(self, value):
        self.set_cheese(value)    
    
    def set_cheese(self, value):
        if value == True:
            self.value = value
        else:
            self.value = False

    def get_cheese(self):
        return self.value

class Pico:
    def __init__(self, value):
        self.set_pico(value)   
    
    def set_pico(self, value):
        if value == True:
            self.value = value
        else:
            self.value = False

    def get_pico(self):
        return self.value
    
class Corn:
    def __init__(self, value):
        self.set_corn(value)    
    
    def set_corn(self, value):
        if value == True:
            self.value = value
        else:
            self.value = False

    def get_corn(self):
        return self.value
#Feel free to add code below to test out the class that
#you've written. It won't be used for grading.

burrito_1 = Burrito("tofu", True, "white", "black")
