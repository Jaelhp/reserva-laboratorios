def laboratorio_disponible(reservas, laboratorio, fecha, hora):
    for reserva in reservas:
        if (
            reserva["laboratorio"] == laboratorio
            and reserva["fecha"] == fecha
            and reserva["hora"] == hora
            and reserva["estado"] == "confirmada"
        ):
            return False

    return True


reservas = [
    {
        "laboratorio": "Lab 01",
        "fecha": "2026-10-01",
        "hora": "10:00",
        "estado": "confirmada"
    }
]

print(laboratorio_disponible(
    reservas,
    "Lab 01",
    "2026-10-01",
    "10:00"
))
