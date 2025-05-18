import re

def get_user_input(prompt, transform=None, valid_options=None):

    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("La entrada no puede estar vacía. Inténtelo nuevamente.")
            continue

        if transform:
            user_input = transform(user_input)

        if valid_options and user_input not in valid_options:
            print(f"Opción no válida. Las opciones válidas son: {', '.join(valid_options)}")
            continue

        return user_input


def formatear_patente(patente):
    patente = patente.strip().upper()

    if re.fullmatch(r"[A-Z]{3}[0-9]{3}", patente):
        return f"{patente[:3]}-{patente[3:]}"

    if re.fullmatch(r"[A-Z]{2}[0-9]{3}[A-Z]{2}", patente):
        return f"{patente[:2]}-{patente[2:5]}-{patente[5:]}"

    return patente
