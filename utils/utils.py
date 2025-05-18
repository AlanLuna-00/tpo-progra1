def get_user_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("La entrada no puede estar vacía. Inténtelo nuevamente.")
