def calcular_salario_neto(salario_bruto, porcentaje_impuestos):
    descuento = salario_bruto * (porcentaje_impuestos / 100)
    salario_final = salario_bruto - descuento
    return salario_final


salario_bruto = float(input("Ingrese su salario bruto: "))
porcentaje_impuestos = float(input("Ingrese el porcentaje de impuestos: "))
salario_neto = calcular_salario_neto(salario_bruto, porcentaje_impuestos)
print(f"Su salario neto es: {salario_neto}")
