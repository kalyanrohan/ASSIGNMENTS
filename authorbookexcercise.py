class Author:

    def __init__(self,name,email,gender):
        self.name=name
        self.email=email
        self.gender=gender

        if self.gender != "m" and self.gender != "f":
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
    

    def toString(self):
        return f"Book={self.getName()},{self.author.toString()},price={self.price},qty={self.qty}"
    

    def getAuthorName(self):
        return self.author.getName()

    def getAuthorEmail(self):
        return self.author.getEmail()

    def getAuthorGender(self):
        return self.author.getGender()

b1=Author("rohan","123@gmail.com","m")
b2=Book("geronimo stilton","shepard","20",2)

print(b1.toString())
print(b2.toString())
