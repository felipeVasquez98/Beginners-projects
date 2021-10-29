import random

num_juegos = input('Ingrese cuantos juegos quiere jugar: ')

if num_juegos.isdigit():
    num_juegos = int(num_juegos)

    if num_juegos%2 != 0:
        if num_juegos <= 0:
            print('Por favor escribe un número mayor a 0 la próxima vez...')
            quit()
    
    else:
        print('Por favor escribe un número impar la próxima vez')
        quit()

else:
    print('Por favor digite un número la próxima vez...')
    quit()

vict_usuario = 0
vict_maquina = 0
empates = 0
turnos_jugados = 0

opciones = ['piedra', 'papel', 'tijera']

while turnos_jugados < num_juegos:
    turnos_jugados += 1
    opcion_usuario = input('Escriba Piedra/Papel/Tijera o Q para salir: ').lower()
    if opcion_usuario == 'q':
        break

    if opcion_usuario not in opciones:
        continue

    #Se considera 0 = piedra, 1 = papel, 2 = tijera
    r_number = random.randint(0,2)

    opcion_maquina = opciones[r_number]

    if opcion_usuario == 'piedra' and opcion_maquina == 'tijera':
        print('Ganaste :)')
        vict_usuario += 1
    
    elif opcion_usuario == 'papel' and opcion_maquina == 'piedra':
        print('Ganaste :)')
        vict_usuario += 1
    
    elif opcion_usuario == 'tijera' and opcion_maquina == 'papel':
        print('Ganaste :)')
        vict_usuario += 1

    elif opcion_usuario == 'piedra' and opcion_maquina == 'piedra':
        print('Empataste')
        empates += 1
    
    elif opcion_usuario == 'papel' and opcion_maquina == 'papel':
        print('Empataste')
        empates += 1
    
    elif opcion_usuario == 'tijera' and opcion_maquina == 'tijera':
        print('Empataste')
        empates += 1
    
    else:
        print('Perdiste :(')
        vict_maquina += 1


print('Obtuviste', vict_usuario, 'victorias en total en ', turnos_jugados, 'turnos jugados')
print('La máquina obtuvo ', vict_maquina, 'victorias en total en ', turnos_jugados, 'turnos jugados')
print('Usted y la máquina obtuvieron ', empates, 'empates en total en ', turnos_jugados, 'turnos jugados')

if vict_usuario > vict_maquina:
    print('Usted ganó el juego :)')
else:
    print('Usted perdió el juego :(')

print('Hasta luego')

