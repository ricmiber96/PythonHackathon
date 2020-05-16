

precio = 3.4
descuento = 1 - 0.6
precio_con_descuento = precio * descuento 

numero_de_barras = input("Introduce el numero de barras vendidas:")
numero_de_barras = int(numero_de_barras)

print("Precio habitual: "+ str(precio))
print("Descuento: "+ str(precio_con_descuento))
print("Conste final:" + str(numero_de_barras * precio_con_descuento))