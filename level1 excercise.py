#LEVEL 1
#1.Print all elements of a list using for loop.
lista=[1,2,3,4]
for x in lista:
    print(x)

#2.Take inputs from user to make a list. 
# Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.
listb= []
for x in range(10):
    listb.append(eval(input("Enter a number: ")))
listb.remove(eval(input("Remove a number: ")))
print(f"listb: {listb}")

#3.Print multiplication table of 14 from a list in which multiplication table of 12 is stored.
multiplication_table_of_12=[x*12 for x in range(1,21)]
print(f"table of 12: {multiplication_table_of_12}")
multiplication_table_of_14=[y for y in multiplication_table_of_12 if y%14==0]
print(f"table of 14: {multiplication_table_of_14}")

#4.You are given with a list of integer elements. Make a new list which will store square of elements of previous list.
a= [1,2,3,4,5,6,7,8,9,10]
b=[x**2 for x in a]
print(f"alist: {a}")
print(f"square numbers: {b}")

#5.Using range(1,101), make two list, one containing all even numbers and other containing all odd numbers.
even=[x for x in range(1,101) if x%2==0]
odd=[y for y in range(1,101) if y%2!=0]
print(f"even numbers: {even}")
print(f"odd numbers: {odd}")

#6.From the two list obtained in previous question, make new lists, containing only numbers which are divisible by 4, 6, 8, 10, 3, 5, 7 and 9 in separate lists.
four=[x for x in even if x%4==0]
six=[x for x in even if x%6==0]
eight=[x for x in even if x%8==0]
ten=[x for x in even if x%10==0]
five=[x for x in even and odd]
print(f"divisible by 4: {four}")
print(f"divisible by 6: {six}")
print(f"divisible by 8: {eight}")
print(f"divisible by 10: {ten}")

#7.From a list containing ints, strings and floats, make three lists to store them separately.
list1=[3.4,3,"fall",2,77,10.02,"sell","glory","10.3",3.7]
string=[]
integer=[]
floats=[]
for x in list1:
    if type(x)==str:
        string.append(x)
    elif type(x)==int:
        integer.append(x)
    else:
        floats.append(x)
print(string)
print(floats)
print(integer)


