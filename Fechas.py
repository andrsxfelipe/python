#1. Importar el módulo
from datetime import datetime, date, time, timedelta

#2. Crear fechas y horas
hoy = date.today()
ahora = datetime.now()
mi_fecha = date(2023, 12, 25)  # (año, mes, día)
mi_hora = time(14, 30, 0)  # (hora, minuto, segundo)
evento = datetime(2025, 5, 7, 10, 45)  # (año, mes, día, hora, minuto)

#3. Formatear fechas
ahora = datetime.now()
print(ahora.strftime("%d/%m/%Y"))        # '07/05/2025'
print(ahora.strftime("%A, %d %B %Y"))    # 'Wednesday, 07 May 2025'

"""
| Código | Significado      | Ejemplo   |
| ------ | ---------------- | --------- |
| `%Y`   | Año completo     | 2025      |
| `%y`   | Año 2 dígitos    | 25        |
| `%m`   | Mes (01-12)      | 05        |
| `%B`   | Nombre del mes   | May       |
| `%d`   | Día (01-31)      | 07        |
| `%A`   | Día de la semana | Wednesday |
| `%H`   | Hora (00-23)     | 15        |
| `%M`   | Minuto (00-59)   | 32        |
| `%S`   | Segundo (00-59)  | 11        |"""

#4. Convertir string a fecha
fecha_str = "07/05/2025"
fecha_obj = datetime.strptime(fecha_str, "%d/%m/%Y") # 2025-05-07 00:00:00

#5. Operaciones con fechas
##Suma o resta de días
mañana = hoy + timedelta(days=1)
ayer = hoy - timedelta(days=1)
##Diferencia de dias
inicio = date(2025, 5, 1)
fin = date(2025, 5, 7)
diferencia = fin - inicio
print(diferencia.days)  # 6

#6. Extraer partes especificas
ahora = datetime.now()
print(ahora.year)   # 2025
print(ahora.month)  # 5
print(ahora.day)    # 7
print(ahora.hour)   # hora actual
