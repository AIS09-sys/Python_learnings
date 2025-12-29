#nested if else
age=int(input("enter a age"))
if age >= 18:
  if age >= 60:
     print("Senior")
  else:
    print("Adult")
else:
  print("minor")