class Person:
    def __init__(self,name,address):
        self._name=name
        self._address=address
    

    def getName(self):
        return self._name
    

    def getAddress(self):
        return self._address

    
    def setAddress(self,address):
        self._address=address
    
    
    def __str__(self):
        return(f'name= {self.getName()}, address= {self.getAddress}')
    

class Student(Person):
    def __init__(self,name,address,numCourses=0,courses=[],grades=[]):
        super().__init__(name,address)
        self._numCourses=numCourses
        self._courses=courses
        self._grades= grades
    
    def __str__(self):
        return (f"student= {self.getName()}, address= {self.getAddress()}")
    
    def addCourseGrade(self,course,grade):
        self._courses.append(course)
        self._grades.append(grade)
    

    def printGrades(self):
        print(self.__grades)

    
    def AverageGrade(self):
        return(sum(self.__grades)/len(self.__grades))

class Teacher(Person):

    def __init__(self,name,address,numCourses=0,courses=[]):
        super().__init__(name,address)
        self.numCourses=numCourses
        self.courses=courses
    
    
    def addCourse(self,course):
        for courses in self._courses:
            if course==courses:
                return False
        self._courses.append(course)
        return True
    

    def removeCourse(self, course):
        if course in self.__courses:
            self.__courses.remove(course)
            return True
        else:
            return False    


    def __str__(self):
        return (f"Teacher= {self.getName()}, address= {self.getAddress()}")
    

print("hello")
    
    




