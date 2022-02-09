s1 = input("Enter first string:")
s2 = input("Enter second string:")
print("Output: ",end='')

if(sorted(s1.lower())==sorted(s2.lower())):
      print("Yes")
else:
      print("No")
