from numeros import *

def principal():
    turnos = {
        "1":turno_farmacia(),
        "2":turno_cosmetica(),
        "3":turno_perfumeria()
    }

    while True:
        print("Elige el area:\n"
              "1. Farmacia\n"
              "2. Cosmetica\n"
              "3. Perfumeria")
        eleccion = (input("Elige un area:"))

        if eleccion not in turnos:
            print("El area no existe")
            continue
        next(turnos[eleccion])
        seguir = input("Quiere sacar un nuevo turno S/N:")
        if seguir == "N":
            break


if __name__ == "__main__":
    principal()


