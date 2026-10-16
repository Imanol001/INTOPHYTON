tickets = [105, 102, 108, 101]
print("Estado inicial de la cola: ", tickets)

# Ticket de emergencia
tickets.insert(0, 999)
print("Tras recibir emergencia: ", tickets)

# Ticket cancelado
tickets.remove(108)
print("Tras cancelacion de ticket 108: ", tickets)

# Ordenados de mayor a menor
tickets.sort(reverse=True)
print("Cola ordenada por prioridad: ", tickets)

# Extraer y mostrar primer elemento
primer_ticket = tickets.pop(0)
print("\n---Atencion---")
print("Atendiendo ticket ID: ", primer_ticket)
print("Cola pendiente actualizada: ", tickets)
