n = int(input("enter a number: "))
temp = n
count = 0

for i in range(1, temp + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print(f"{temp} is a prime number")
else:
    print(f"{temp} is not a prime number")
