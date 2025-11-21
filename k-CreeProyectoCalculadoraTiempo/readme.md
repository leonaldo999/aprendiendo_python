# Cree un proyecto de calculadora de tiempo

Cree un proyecto de calculadora de tiempo
Escriba una función llamada `add_time` que tome dos parámetros obligatorios y uno opcional:

- una hora de inicio en formato de 12 horas (terminando en AM o PM)
- una duración que indique el número de horas y minutos
- (opcional) un día de inicio de la semana, sin distinción entre mayúsculas y minúsculas

La función debe sumar la duración a la hora de inicio y devolver el resultado.

Si el resultado es el día siguiente, debe mostrar `(next day)` después de la hora. Si el resultado es más de un día después, debe mostrar `(n days later)` después de la hora, donde «n» es el número de días después.

Si a la función se le proporciona el parámetro opcional del día de inicio de la semana, la salida debe mostrar el día de la semana del resultado. El día de la semana en la salida debe aparecer después de la hora y antes del número de días posteriores.

*A continuación se muestran algunos ejemplos de diferentes casos que la función debe manejar. Preste mucha atención al espaciado y la puntuación de los resultados.*

- **Codigo Ejemplo**

  ```py
  add_time('3:00 PM', '3:10')
  # Returns: 6:10 PM

  add_time('11:30 AM', '2:32', 'Monday')
  # Returns: 2:02 PM, Monday

  add_time('11:43 AM', '00:20')
  # Returns: 12:03 PM

  add_time('10:10 PM', '3:30')
  # Returns: 1:40 AM (next day)

  add_time('11:43 PM', '24:20', 'tueSday')
  # Returns: 12:03 AM, Thursday (2 days later)

  add_time('6:30 PM', '205:12')
  # Returns: 7:42 AM (9 days later)
  ```

---

No importe ninguna biblioteca de Python. Suponga que las horas de inicio son válidas. Los minutos de la duración serán un número entero inferior a 60, pero la hora puede ser cualquier número entero.

> Nota: abra la consola del navegador con F12 para ver un resultado más detallado de las pruebas.

- **Codigo**

  ```py
  def add_time(start, duration, day_of_week=None):
      # Días de la semana para manejar el día opcional
      days_of_week_list = [
        "Monday",
        "Tuesday", 
        "Wednesday", 
        "Thursday", 
        "Friday", 
        "Saturday", 
        "Sunday"
      ]

      # 1. Parsear la hora de inicio (start)
      
      # Separar la hora/minuto del AM/PM
      time_part, period = start.split()
      start_hour, start_minute = map(int, time_part.split(':'))
  
      # Convertir a formato de 24 horas
      if period == 'PM' and start_hour != 12:
          start_hour += 12
      elif period == 'AM' and start_hour == 12:
          start_hour = 0  # 12:xx AM es 0:xx en formato 24h
  
      # Convertir la hora de inicio total a minutos
      start_total_minutes = start_hour * 60 + start_minute
  
      # 2. Parsear la duración (duration)
  
      duration_hour, duration_minute = map(int, duration.split(':'))
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
  ```

---
