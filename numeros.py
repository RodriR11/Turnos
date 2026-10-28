from functools import wraps


def decorador_numeros(funcion):
    @wraps(funcion)
    def inicio(*args, **kwargs):
        for turno in funcion(*args, **kwargs):
            print(f"Su turno es {turno}")
            print("Sera atendido en breve")
            yield turno
    return inicio



@decorador_numeros
def turno_farmacia():
    n = 1
    while True:
        yield f"Turno F:0{n}"
        n += 1



@decorador_numeros
def turno_cosmetica():
    n = 1
    while True:
        yield f"Turno C:0{n}"
        n += 1



@decorador_numeros
def turno_perfumeria():
    n = 1
    while True:
        yield f"Turno P:0{n}"
        n += 1










