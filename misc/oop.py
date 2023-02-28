class Human:
    
    
    is_sharam = True
    
    def __init__(self, name="Insaan", age="Unknown", is_alive=False):
            self.name = name
            self.age = age
            self.is_alive = is_alive
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_is_alive(self):
        print(Human.is_sharam)
        return self.is_alive
    
    
# hammad = Human(age=20, name="Hammad", is_alive=True)
# jawad = Human(age=16, name="Jawad", is_alive=True)
# hammad.is_sharam = False
# print(jawad.is_sharam)
# print(hammad.is_sharam)


# class User():
    
    
#     def __init__(self, email):
#         self.email = email
        
#     def sign_in(self):
#         print("U'r signed in")
    
    
# user1 = User('a')
# print(str(user1))
# print(user1.__str__())
# user2 = str(user1)
# print(type(user1))
# print(type(user2))
    
# class Wizard(User):
    
    
#     def __init__(self, name, power, email):
#         super().__init__(email)
#         self.name = name
#         self.power = power
        
#     def attack(self):
#         print(f'Attack Done by \"Wizard\" {self.name} having an email of  with power {self.power}')
        
# wizard1 = Wizard("Hammad", 100, 'm.hammadsaani@gmail.com')
# print(wizard1.email)

# print(dir(Wizard))



class A():
    num = 1
    
    
class B(A):
    pass

class C(A):
    num = 5
    
class D(B, C):
    pass

print(B.num)