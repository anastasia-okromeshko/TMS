guests = int(input("Enter the number of guests:"))
if guests > 50:
    print("restaurant")
elif 20 <= guests <= 50:
    print("cafe")
elif guests < 20:
    print("house")
