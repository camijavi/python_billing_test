from components import clearConsole

def readProductCount():
    productCount = int(input("¿Cuántos productos desea ingresar?: "))
    return productCount

def calculateSubtotal(qty, price):
    return qty * price

def calculateTotalProducts(totalProducts, subtotal):
    return totalProducts + subtotal

def calculateParticipationPercentage(subtotal, totalProducts):
    if totalProducts > 0:
        return (subtotal / totalProducts) * 100
    return 0.0

def calculateDiscount(totalProducts, percentage):
    discRate = percentage / 100 if percetage > 1 else percentage
    return totalProducts * discRate

def calculateTotal (totalProducts, percetage, tax):
    discount = calculateDiscount(totalProducts, percentage)
    vat = calculateVAT(totalProducts - discount, tax)
    total = totalProducts - discount + vat
    return discount, vat, total

def readSalesData(message):
    print(message)
    print("+"*50)
    clientName = input("Nombre del cliente: ")

    productCount = readProductCount()

    #variables acumuladoras 
    totalProducts = 0.0
    productsTextBuffer = "" 

    for i in range (1, productCount + 1):
        print(f"\n--- Producto #{i} de {productCount} ---")
        name = input("Nombre del producto: ")
        q = int(input("Cantidad: "))
        p = float(input("Precio unitario: "))

        sub = calculateSubtotal(q, p)
        totalProducts = calculateTotalProducts(totalProducts, sub)

        productsTextBuffer += f"{name};{q};{p:.2f};{sub:.2f}\n"

    return clientName, productCount, productsTextBuffer, totalProducts

def showBill(clientName, productCount, products_text_buffer, totalProducts, percentage, discount, tax, vat, total):
    """
    Módulo para mostrar la factura procesando el texto sin usar listas [].
    """
    print("\n" + "=" * 65)
    print("                 FACTURA DE VENTA                 ")
    print("=" * 65)
    print(f"Cliente: {clientName}")
    print("-" * 65)
    print(f"{'Producto':<20} {'Cant.':<8} {'Precio':<10} {'Subtotal':<10} {'Part. (%)':<8}")
    print("-" * 65)
    
    # Procesamos la cadena de texto línea por línea sin listas ni .split()
    line = ""
    for char in products_text_buffer:
        if char == "\n":
            if line:
                # Extraemos los campos buscando el delimitador ';'
                p1 = line.find(";")
                p2 = line.find(";", p1 + 1)
                p3 = line.find(";", p2 + 1)
                
                p_name = line[:p1]
                p_qty = int(line[p1+1:p2])
                p_price = float(line[p2+1:p3])
                p_sub = float(line[p3+1:])
                
                part_pct = calcular_porcentaje_participacion(p_sub, totalProducts)
                print(f"{p_name:<20} {p_qty:<8} ${p_price:<9.2f} ${p_sub:<9.2f} {part_pct:<7.2f}%")
                line = ""
        else:
            line += char

    print("-" * 65)
    print(f"Subtotal general (totalProducts):  ${totalProducts:.2f}")
    print(f"Descuento ({percentage}%):             -${discount:.2f}")
    print(f"IVA ({int(tax * 100)}%):                    +${vat:.2f}")
    print("=" * 65)
    print(f"TOTAL A PAGAR:                      ${total:.2f}")
    print("=" * 65)

def main():
    clearConsole()
    message = "BIENVENIDO A SU SISTEMA DE FACTURACIÓN"
    tax = 0.15

    # 1. Módulo readSalesData()
    clientName, productCount, products_text_buffer, totalProducts = readSalesData(message)

    # Porcentaje de descuento global
    percentage = float(input("\nIngrese el porcentaje de descuento (%): "))

    # 2. Módulo calculateTotal()
    discount, vat, total = calculateTotal(totalProducts, percentage, tax)

    # 3. Módulo showBill()
    showBill(
        clientName, productCount, products_text_buffer,
        totalProducts, percentage, discount, tax, vat, total
    )

if __name__ == "__main__":
    main()