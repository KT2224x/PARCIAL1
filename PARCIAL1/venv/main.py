from UI import atencion

def principal():
    while True:
        atencion()
        respuesta = input("¿Quiere volver a hacer otra consulta? (s/n): ")
        if respuesta.lower() != 's':
            break

if __name__ == '__main__':
    principal()
