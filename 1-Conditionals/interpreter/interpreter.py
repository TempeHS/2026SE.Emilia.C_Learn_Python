IP = (input("Problem? "))

if "+" in IP:
    x, y, z = IP.split( )
    print(float(x) + float(z))
elif "-" in IP:
    x, y, z = IP.split( )
    print(float(x) - float(z))
elif "/" in IP:
    x, y, z = IP.split( )
    print(float(x) / float(z))
elif "*" in IP:
    x, y, z = IP.split( )
    print(float(x) * float(z))