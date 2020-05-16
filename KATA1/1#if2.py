
edad_usuario = input("Introduce tu edad: ")
edad_usuario = int(edad_usuario)

if edad_usuario < 4:
    print("Entrada gratis")
elif 4 <= edad_usuario <=18:
    print("El precio es de 5€")
    
else: print("El precio es de 10€")