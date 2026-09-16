from components import clearConsole

def main():
    clearConsole()
    message = "BIENVENIDO A SU SISTEMA DE FACTURACIÓN!"
    clientName = None
    qty = 0
    price = subtotal = discount = vat = total = 0.0
    tax = 0.15

    # Invoke readSalesData()
    clientName = readSalesData(message)

    qty = int(input("Digite la cantidad comprada: "))
    percentage = float(input("Digite el porcentaje de descuento: "))

    # Invoke calculateTotal()
    subtotal, discount, vat, total = calculateTotal(qty, price, percentage, tax)

def calculateTotal(qty, price, percentage, tax):
    subtotal = calculateSubtotal(qty, price)
    discount = calculateDiscount(subtotal, percentage)
    vat = calculateVAT(subtotal, tax)
    total = subtotal - discount + vat
    return subtotal, discount, vat, total

def calculateSubtotal(qty, price):
    subtotal = qty * price 
    return subtotal

def calculateDiscount(subtotal, percentage):
    discount = subtotal * percentage
    return discount

def calculateVAT(subtotal, tax):
    vat = subtotal * tax 
    return vat

def readSalesData(message):
    print(message)
    print("*" * 40)
    clientName = input("Digite el nombre del cliente: ")
    return clientName

main()