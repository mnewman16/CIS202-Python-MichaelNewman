purchase = input("Would you like to buy a muffin or a cupcake?").lower()
cupcake = 10
muffin = 10

while purchase != '0':
    if purchase == "muffin":
        muffin = muffin -1
        if purchase == "muffin" and  muffin <= 0:
            print("Muffins are out of stock")
            muffin = 0
    if purchase == "cupcake":
        cupcake = cupcake -1
        if purchase == "cupcake" and  cupcake <= 0:
            print("Cupcakes are out of stock")
            cupcake = 0
    purchase = input("Would you like to buy a muffin or a cupcake?").lower()
print("Muffins:", muffin, "Cupcakes:", cupcake)

