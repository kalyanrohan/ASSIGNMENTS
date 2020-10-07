

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
five=[]
for x in odd and even:
    if x%5==0:
        five.append(x)

print(f"divisible by 4: {four}")
print(f"divisible by 6: {six}")
print(f"divisible by 8: {eight}")
print(f"divisible by 10: {ten}")
print(f"divisble by 5: {five}")


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

