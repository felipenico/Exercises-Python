def suma(n1=None,n2=None):
    if (n1 is not None and n2 is not None):
        if (type(n1).__name__ != str and type(n2).__name__ != str):
            try:
                suma = n1 + n2
            except TypeError:
                print("Error: Tipo de dato No Valido...")
                print("Digite de nuevo los datos.")
            else:
                return suma
        else:
            print("Error: Tipo de dato No Valido...")
            print("Digite de nuevo los datos.")
    else:
        print("No Digito un numero")
        print("Intente de nuevo..")

def resta(n1=None,n2=None):
    if (n1 is not None and n2 is not None):
        try:
            resta = n1 - n2
        except TypeError:
            print("Error: Tipo de dato No Valido...")
            print("Digite de nuevo los datos.")
        else:
            return resta
    else:
        print("No Digito un numero")
        print("Intente de nuevo..")

def producto(n1=None,n2=None):
    if (n1 is not None and n2 is not None):
        if (type(n1).__name__ != str and type(n2).__name__ != str):
            try:
                producto = n1 * n2
            except:
                print("Error: Tipo de dato No Valido...")
                print("Digite de nuevo los datos.")
            else:
                return producto
        else:
            print("Error: Tipo de dato No Valido...")
            print("Digite de nuevo los datos.")
    else:
        print("No Digito un numero")
        print("Intente de nuevo..")

def division(n1=None,n2=None):
    if (n1 is not None and n2 is not None):
        try:
            division = n1 / n2
        except TypeError:
            print("Error: Tipo de dato No Valido...")
            print("Digite de nuevo los datos.")
        except ZeroDivisionError:
            print("Error: No se puede dividir por cero")
            print("Digite de nuevo los datos.")
        else:
            return division
    else:
        print("No Digito un numero")
        print("Intente de nuevo..")


