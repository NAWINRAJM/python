#13. Write a Python script to concatenate following dictionaries to create a new one.
#Sample Dictionary: dic1= {1:10, 2:20}dic1= {1:10, 2:20} dic3= {5:50,6:60}
#Expected Result: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dic1= {1:"A", 2:"B"}
dic2= {3:"C", 4:"D"} 
dic3= {5:"E",6:"F"}
dic4={}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)

