# Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
# de un lugar ficticio al pasar un número concreto de días según estas reglas:
# - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
# - Cada día que pasa:
#   - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
#   - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día 
#     siguiente aumenta en un 20%.
#   - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día 
#     siguiente disminuye en un 20%.
#   - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
# - La función recibe el número de días de la predicción y muestra la temperatura
#   y si llueve durante todos esos días.
# - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.

import random

def weather_sim(initial_temp: int, rain_chance: int, days: int):
    current_day_temp = initial_temp
    current_day_rain_change = rain_chance

    for day in range(1, days + 1):
        print(f"Día {day}: {current_day_temp} grados y {current_day_rain_change}% de probabilidad de lluvia")

        ##   - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
        if random.randint(1,10) == 1:
            current_day_temp += 2 if random.randint(1, 2) == 1 else -2

        #   - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día 
        #     siguiente aumenta en un 20%.
        if current_day_temp > 25: 
            current_day_rain_change += 20
            current_day_rain_change = 100 if current_day_rain_change > 100 else current_day_rain_change

        #   - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día 
        #     siguiente disminuye en un 20%.
        if current_day_temp < 5:
            current_day_rain_change -= 20  
            current_day_rain_change = 0 if current_day_rain_change < 0 else current_day_rain_change
        
        #   - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
        if current_day_rain_change == 100:
            current_day_temp -= 1


initial_temp = int(input("Por favor ingrese la temperatura inicial: "))
rain_chance = int(input("Por favor ingrese la probabilidad de lluvia inicial: "))
days = int(input("Por favor ingrese la cantidad de días a calcular: "))

weather_sim(initial_temp, rain_chance, days)
