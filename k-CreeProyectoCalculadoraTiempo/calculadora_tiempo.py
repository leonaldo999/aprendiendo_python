"""
Cree un proyecto de calculadora de tiempo
"""


def add_time(start, duration, day_of_week=None):
    # Días de la semana para manejar el día opcional
    days_of_week_list = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    # 1. Parsear la hora de inicio (start)

    # Separar la hora/minuto del AM/PM
    time_part, period = start.split()
    start_hour, start_minute = map(int, time_part.split(":"))

    # Convertir a formato de 24 horas
    if period == "PM" and start_hour != 12:
        start_hour += 12
    elif period == "AM" and start_hour == 12:
        start_hour = 0  # 12:xx AM es 0:xx en formato 24h

    # Convertir la hora de inicio total a minutos
    start_total_minutes = start_hour * 60 + start_minute

    # 2. Parsear la duración (duration)

    duration_hour, duration_minute = map(int, duration.split(":"))
    duration_total_minutes = duration_hour * 60 + duration_minute

    # 3. Calcular el nuevo tiempo

    new_total_minutes = start_total_minutes + duration_total_minutes

    # Calcular los días después (days_later)

    # Los minutos en un día son 24 * 60 = 1440
    minutes_in_a_day = 1440

    days_later = new_total_minutes // minutes_in_a_day

    # Minutos restantes en el último día (el nuevo tiempo)
    new_time_minutes_of_day = new_total_minutes % minutes_in_a_day

    # Calcular la nueva hora y minutos

    new_hour = new_time_minutes_of_day // 60
    new_minute = new_time_minutes_of_day % 60

    # 4. Convertir la nueva hora de vuelta a formato de 12 horas y determinar el periodo (AM/PM)

    new_period = "AM"
    display_hour = new_hour

    if new_hour >= 12:
        new_period = "PM"
        if new_hour > 12:
            display_hour = new_hour - 12

    if new_hour == 0:
        display_hour = 12
        new_period = "AM"

    # Formatear el nuevo tiempo (minutos siempre con 2 dígitos)
    new_time = f"{display_hour}:{str(new_minute).zfill(2)} {new_period}"

    # 5. Manejar el día de la semana opcional

    if day_of_week:
        # Normalizar la entrada a formato Título (primera letra mayúscula)
        day_of_week = day_of_week.capitalize()

        # Encontrar el índice del día de inicio
        try:
            start_day_index = days_of_week_list.index(day_of_week)
        except ValueError:
            # En caso de que el día opcional sea inválido, aunque el prompt asume validez
            return "Error: Invalid day of the week provided."

        # Calcular el índice del nuevo día (la suma de días mod 7)
        new_day_index = (start_day_index + days_later) % 7
        new_day_of_week = days_of_week_list[new_day_index]

        # Añadir el día de la semana a la salida
        new_time += f", {new_day_of_week}"

    # 6. Manejar el indicador de días después

    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time
