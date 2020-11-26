class Author:

    def __init__(self,name,email,gender):
        self.name=name
        self.email=email
        self.gender=gender

        if self.gender.lower() != "m" or "f":
            raise TypeError("M or F")

    
    def getName(self):
        return self.name
    

    def getEmail(self):
        return self.email
    

    def setEmail(self,email):
        self.email=email
    

    def getGender(self):
        return self.gender
    

    def toString(self):
        return f"Author[{self.getName()},{self.getEmail()},{self.getGender()}"
    

class Book(Author):
    def __init__(self,name,author,price,qty=0):
        self.name=name
        self.author=author
        self.price=price
        self.qty=qty
    

    def getName(self):
        return self.name
    

    def getAuthor(self):
        return self.author
    

    def getPrice(self):
        return self.price
    

    def setPrice(self,price):
        self.price=price
    

    def getQty(self):
        return self.qty
    

    def setQty(self,qty):
        self.qty=qty
    

    def toString(self,name,email,gender):
        super().__init__(name,email,gender)
        return f"Book={self.getName()}, Author[name={self.name},"
        
print("hello")
print("hello")

