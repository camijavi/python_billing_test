import os

def main():
    mensaje = "Bienvenido a Comercial VAle Todo!"
    nombre = None
    cantidad = 0
    precio = subtotal = descuento = iva = total = 0.0
    impuesto = 0.15

    #Invocar a leer_cliente()
    nombre = leer_cliente(mensaje)

    #Invacar a calcular_total()
    calcular_total(cantidad, precio, porcentaje, impuesto)
    cantidad= int(input("Digite la cantidad comprada: "))
    porcentaje = float(input("Digite el porcentaje de descuento: "))
    total, subtotal, descuento, iva = calcular_total(cantidad, precio, porcentaje, impuesto)

def calcular_total(cantidad, precio, porcentaje, impuesto):
    subtotal = calcular_subtotal(cantidad, precio)
    descuento = calcular_descuento(subtotal, porcentaje)
    iva = calcular_iva(subtotal, impuesto)
    total = subtotal - descuento + iva

def calcular_subtotal (cantidad, precio):
    subtotal = cantidad * precio 
    return subtotal

def calcular_descuento(subtotal, porcentaje):
    descuento = subtotal * porcentaje
    return descuento

def calcular_iva(subtotal, impuesto):
    iva = subtotal + impuesto 
    return iva

def leer_cliente(msj):
    print(msj)
    print("*"*40)
    nombre = input("Digite el nombre del cliente: ")
    return nombre

main()