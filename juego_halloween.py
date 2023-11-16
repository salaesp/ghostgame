#
 # Este es un reto especial por Halloween.
 # Te encuentras explorando una mansión abandonada llena de habitaciones.
 # En cada habitación tendrás que resolver un acertijo para poder avanzar a la siguiente.
 # Tu misión es encontrar la habitación de los dulces.
 #
 # Se trata de implementar un juego interactivo de preguntas y respuestas por terminal.
 # (Tienes total libertad para ser creativo con los textos)
 #
 # - 🏰 Casa: La mansión se corresponde con una estructura cuadrada 4 x 4
 #   que deberás modelar. Las habitaciones de puerta y dulces no tienen enigma.
 #   (16 habitaciones, siendo una de entrada y otra donde están los dulces)
 #   Esta podría ser una representación:
 #   🚪⬜️⬜️⬜️
 #   ⬜️👻⬜️⬜️
 #   ⬜️⬜️⬜️👻
 #   ⬜️⬜️🍭⬜️
 # - ❓ Enigmas: Cada habitación propone un enigma aleatorio que deberás responder con texto.
 #   Si no lo aciertas no podrás desplazarte.
 # - 🧭 Movimiento: Si resuelves el enigma se te preguntará a donde quieres desplazarte.
 #   (Ejemplo: norte/sur/este/oeste. Sólo deben proporcionarse las opciones posibles)
 # - 🍭 Salida: Sales de la casa si encuentras la habitación de los dulces.
 # - 👻 (Bonus) Fantasmas: Existe un 10% de que en una habitación aparezca un fantasma y
 #   tengas que responder dos preguntas para salir de ella.
 #


import random
    
door = "🚪"
empty_room = "⬜"
candy = "🍬"
ghost = "👻"
def create_house() -> (list, list):
    
    def generate_candy(door: list) -> list:
        candy = [random.randint(0,3), random.randint(0,3)]
        if candy[0] == door[0] and candy[1] == door[1]:
            return generate_candy(door)
        return candy

    def generate_ghost(door: list) -> list:
        candy = [random.randint(0,3), random.randint(0,3)]
        if candy[0] == door[0] and candy[1] == door[1]:
            return generate_candy(door)
        return candy

    house = [list([empty_room] # 4) for _ in range(4)]
    
    if random.choice([True, False]):
        door_pos = [random.randint(0,3), random.choice([0,3])]
    else:
        door_pos = [random.choice([0,3]), random.randint(0,3)]
    
    house[door_pos[0]][door_pos[1]] = door
    candy_pos = generate_candy(door_pos)
    house[candy_pos[0]][candy_pos[1]] = candy

    
    return house, door_pos

def print_house(house):
    for row in house:
        print("".join(map(str,row)))
    

def move(position: list) -> list:
    row, col = position[0], position[1]

    available_movements = ["n","s","e","o"]
    if row == 0: available_movements.remove("n")
    if row == 3: available_movements.remove("s")
    if col == 0: available_movements.remove("e")
    if col == 3: available_movements.remove("o")

    direction = input(f"¿Hacia donde te quieres desplazar? [{available_movements }]: ").lower()
    
    if direction not in available_movements:
        print("Movimiento inválido")
        return move(position)
    
    if direction == "n": position = [row - 1, col]
    elif direction == "s": position = [row + 1 , col]
    elif direction == "e": position = [row, col - 1]
    elif direction == "o": position = [row, col + 1]
    
    return position

def riddle_me_this():
    riddles = [
        ("¿Cuántos lados tiene un triángulo?", 3),
        ("¿Cuál es el resultado de sumar 5 y 7?", 12),
        ("¿Cuántos dedos tiene una mano?", 5),
        ("¿Cuál es el doble de 9?", 18),
        ("¿Cuántos minutos hay en una hora?", 60),
        ("¿Cuántos meses tiene un año?", 12),
        ("¿Cuál es el resultado de restar 15 a 25?", 10),
        ("¿Cuántos lados tiene un cuadrado?", 4),
        ("¿Cuánto es la raíz cuadrada de 16?", 4),
        ("¿Cuál es el número después de 20?", 21),
        ("¿Cuántas patas tiene un gato?", 4),
        ("¿Cuál es el resultado de multiplicar 6 por 8?", 48),
        ("¿Cuántos lados tiene un pentágono?", 5),
        ("¿Cuánto es la mitad de 14?", 7),
        ("¿Cuántos jugadores hay en un equipo de fútbol?", 11),
        ("¿Cuál es el número anterior a 30?", 29),
        ("¿Cuántas horas hay en un día?", 24),
        ("¿Cuál es el resultado de sumar 3 más 4?", 7),
        ("¿Cuántos colores tiene un arco iris?", 7),
        ("¿Cuántos dígitos tiene el número cien?", 3)
    ]
    current_riddle = riddles[random.randint(0, len(riddles) - 1)]
    answer = input(f"{current_riddle[0]}: ")
    while(answer != str(current_riddle[1])):
        print("Respuesta incorrecta \n")
        answer = input(f"{current_riddle[0]}: ")
    print("Respuesta correcta \n")




house, door = create_house()
print_house(house)
position = door
house_room = house[position[0]][position[1]]
while(house_room != candy):
    position = move(position)
    house_room = house[position[0]][position[1]]
    house[position[0]][position[1]] = "🚶"
    print_house(house)
    house[position[0]][position[1]] = house_room

    if house_room == empty_room: 
        hasGhost = random.randint(1,10) == 1
        if hasGhost:
            print(f"{ghost}ENCONTRASTE UN FANTASMA, tendras que contestar 2 preguntas")
            riddle_me_this()
        riddle_me_this()


print("GANASTE!")
