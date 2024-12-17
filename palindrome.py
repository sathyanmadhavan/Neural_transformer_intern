a = input("Enter the string: ")

b = ""

for i in a:

    b = i + b
    
if b == a:

    print("Palindrome")
    
else: 
    
    print("Not a Palindrome")