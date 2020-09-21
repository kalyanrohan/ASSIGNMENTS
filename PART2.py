#QUESTION 1
"""Write a small program that assigns an angle in degrees to a variable called degrees. The program converts
this angle to radians and assigns it to a variable called radians. To convert from degrees to radians, use the
formula radians = degrees * 3.14 / 180 (where we are using 3:14 to approximate pi). Print the angle in both
degrees and radians."""

Degrees= float(input("enter an angle: "))
Radians= Degrees*3.14/180
print(Degrees)
print(Radians)

#QUESTION 2
"""Write a program that calculates the average score on an exam. Assume we have a small class of only three
students. Assign each student’s score to variables called student1, student2, and student3 and then use
these variables to find the average score. Assign the average to a variable called average. Print the student
scores and the average score."""

student1= float(input("enter student1's score: "))
student2= float(input("enter student2's score: "))
student3= float(input("enter student3's score: "))
average= (student1+student2+student3)/3
print(student1)
print(student2)
print(student3)
print(average)

#alternatively we can make a list first and divide the sum of the items in the list with the length of the list

scores=[student1,student2,student3]
Average= sum(scores)/len(scores)
print(Average)

#QUESTION 3

"""
Imagine that you teach three classes. These classes have 32, 45, and 51 students. You want to divide the
students in these classes into groups with the same number of students in each group, but you recognize
that there may be some “left over” students. Assume that you would like there to be 5 groups in the first
class (of 32 students), 7 groups in the second class (of 45 students), and 6 groups in the third class (of 51
students). Write a program to calculate the number of students in each group (where each group has the
same number of students). Print this number for each class and also print the number of students that will
be “leftover” (i.e., the number of students short of a full group). Use
simultaneous assignment to assign the number in each group and the “leftover” to variables.
The following demonstrates the program’s output:
Number of students in each group:
Class 1: 6
Class 2: 6
Class 3: 8
Number of students leftover:
Class 1: 2
Class 2: 3
Class 3: 3
"""

Class_1=32
Class_2=45
Class_3=51
Number_of_students_in_each_class= {"Class 1":int(Class_1/5),"Class 2":int(Class_2/7),"Class 3":int(Class_3/6)}
Remainder={"Class 1":int(Class_1%5),"Class 2":int(Class_2%7),"Class 3":int(Class_3%6)}
print(Remainder)

