#14. Write a Python script to check if a given key already exists in a dictionary.
A={1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'e', 6: 'F',7:"G"}
B=int(input("enter the number: "))
if B in A :
    print("present")
else:
    print("Not Present")
