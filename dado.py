"""Lazaro Marin 27870547"""
import random

dinero = 100
intentos = 0

while dinero > 0 and intentos < 1000:
    intentos += 1
    
    print(f"Intento #{intentos}")
    print(f"Dinero actual: {dinero}")
    dado = random.randint(1, 6)
    print(f"El dado ha caído en {dado}")
    if dado % 2 == 0:
        dinero += 100
        print("¡Ganaste 100!")
    else:
        dinero -= 100
        print("Perdiste 100")
    print("")
    
print(f"Fin del juego. Intentos: {intentos}, Dinero final: {dinero}")