#3. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
#Sample: list1 = [‘aba’,’121’,’kgf’,’abc’]
lista=["eye","dead","1221","abc","aaa"]
y=0
for i in lista:
    if len(i)>2:
        if i[0]==i[len(i)-1]:
            y=y+1
print(y)