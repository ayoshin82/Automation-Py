
class User:


    def __init__(self, first_name, last_name):
        print(" А вот и я!")
               
        self.first_name = first_name
        self.last_name = last_name
        
    def sayName(self):
        print("Моё имя", self.first_name)

    def surName(self):
        print("Моя фамилия", self.last_name) 

    def fullName(self):
        print("А теперь вместе!!!", self.first_name, self.last_name)