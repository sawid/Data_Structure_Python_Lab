n = float(input(" *** Wind classification ***\nEnter wind speed (km/h) : "))
print("Wind classification is " ,end="")
if n >= 209:
    print("Super Typhoon.")
elif n <= 208.99 and n >= 102.00:
    print("Typhoon.")
elif n <= 101.99 and n >= 56.00:
    print("Tropical Storm.")
elif n <= 55.99 and n >= 52.00:
    print("Depression.")
else:
    print("Breeze.")
