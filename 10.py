# Capturar mensaje de error original
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print(f"Ocurrió un error matematico {e}. ")
