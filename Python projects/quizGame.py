print('¡Bienvenido a la trivia!')

jugando = input('¿Quieres responder la trivia?: ')

if jugando.lower() != 'si':
    quit()

print('Vale, entonces empecemos...')
puntaje = 0

pregunta = input('¿Que criptomoneda representa las siglas BTC?: ')
if pregunta.lower() == 'bitcoin':
    print('¡Correcto! :)')
    puntaje += 1
else:
    print('¡Incorrecto!')

pregunta = input('¿Que criptomoneda representa las siglas ETH?: ')
if pregunta.lower() == 'ethereum':
    print('¡Correcto! :)')
    puntaje += 1
else:
    print('¡Incorrecto!')

pregunta = input('¿Que criptomoneda representa las siglas ADA?: ')
if pregunta.lower() == 'cardano':
    print('¡Correcto! :)')
    puntaje += 1
else:
    print('¡Incorrecto!')

pregunta = input('¿Que criptomoneda representa las siglas DOT?: ')
if pregunta.lower() == 'polkadot':
    print('¡Correcto! :)')
    puntaje += 1
else:
    print('¡Incorrecto!')

pregunta = input('¿Que criptomoneda representa las siglas SOL?: ')
if pregunta.lower() == 'solana':
    print('¡Correcto! :)')
    puntaje += 1
else:
    print('¡Incorrecto!')

print('Su puntaje total es de ', puntaje, ' puntos')