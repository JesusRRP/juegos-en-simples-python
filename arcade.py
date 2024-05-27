import random
#Antes que todo por favor leer todos los comentarios (todo lo de color verde)
#para una correcta comprension del codigo.
#si tienes duda en las funciones (def) ver el siguiente video antes de 
# empezar a leer
# video en español:
#https://www.youtube.com/watch?v=ByBaYB74Tx8
#o este tambien esta bueno este (en ingles):
#https://www.youtube.com/watch?v=89cGQjB5R4M
#puedes modificar el codigo para ponerle mas preguntas en la trivia 
#o ponerle mas palbras en el ahorcado
#creo que no tiene errores el codigo pero si encuentras uno el lunes lo corrijo
#cuando acaben de leer este show borren todos los comentarios ANTES de que lo entreguen.
#cualquier otra duda de python entrar a: https://www.w3schools.com/python/default.asp
#o me preguntan a mi.
#copialo todo tal y como esta y pegalo en replit
#bexos :)


print("******* BIENVENIDO A NUESTRO ARCADE ********:")

#juego numero 1
def play_hangman():
   
    # Lista de palabras posibles para adivinar
    words = ["laipz", "goma", "caleidoscopio"] #puedes añadir mas palabras 

    # Selecciona una palabra aleatoria de la lista
    word_to_guess = random.choice(words)

    # Crea una cadena de guiones bajos de la misma longitud que la palabra a adivinar
    length = '_' * len(word_to_guess)

    # Inicializa el contador de intentos a 0
    intentos = 0

    print("Welcome to the 'ahorcado' game")  # Mensaje de bienvenida al juego

    # Bucle principal del juego
    while True:
        print(length)  # Muestra la palabra con las letras adivinadas y guiones bajos
        letra = input("Ingresar una letra: ")  # Pide al usuario que ingrese una letra

        # Verifica si la letra ingresada está en la palabra a adivinar
        if letra in word_to_guess:
            # Recorre cada letra de la palabra a adivinar
            for i in range(len(word_to_guess)):
                # Si la letra ingresada coincide con la letra en la posición i
                if word_to_guess[i] == letra:
                    # Actualiza la cadena length con la letra correcta en la posición i
                    length = length[:i] + letra + length[i + 1:]

        else:
            # Incrementa el contador de intentos si la letra no está en la palabra
            intentos += 1
            # Dibuja el estado del ahorcado según el número de intentos
            if intentos == 1:
                print(" O")
            elif intentos == 2:
                print(" O")
                print("/")
            elif intentos == 3:
                print(" O")
                print("/ \\")
            elif intentos == 4:
                print(" O")
                print("/|\\")
            elif intentos == 5:
                print(" O")
                print("/|\\")
                print("/  ")
            elif intentos == 6:
                print(" O")
                print("/|\\")
                print("/ \\")
                print("has perdido")  # Mensaje de derrota
                print("la palabra era:")
                print(word_to_guess)
                break  # Termina el juego si se alcanzan 6 intentos

        # Verifica si el jugador ha adivinado la palabra completa
        if length == word_to_guess:
            print("Felicidades has ganado el juego")  # Mensaje de victoria
            print("la palabra es: ")
            print(word_to_guess)
            break  # Termina el juego si se adivina la palabra


#juego número 2

def adivinar_numero():
    # Genera un número aleatorio entre 1 y 100 y lo guarda en la variable numero_secreto
    numero_secreto = random.randint(1, 100)
    intentos = 0  # Inicializa el contador de intentos a 0
    adivinado = False  # Inicializa la variable adivinado como False

    print("¡Bienvenido al juego de adivinar el número!")
    print("Estoy pensando en un número entre 1 y 100.")

    # Bucle que continúa hasta que el número sea adivinado
    while not adivinado:
        try:
            # Pide al usuario que introduzca una adivinanza y la convierte a entero
            adivinanza = int(input("Introduce tu adivinanza: "))
            intentos += 1  # Incrementa el contador de intentos en 1

            # Compara la adivinanza del usuario con el número secreto
            if adivinanza < numero_secreto:
                print("Demasiado bajo. Intenta otra vez.")  # Informa que la adivinanza es demasiado baja
            elif adivinanza > numero_secreto:
                print("Demasiado alto. Intenta otra vez.")  # Informa que la adivinanza es demasiado alta
            else:
                adivinado = True  # Cambia la variable adivinado a True para salir del bucle
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")  # Felicita al usuario
        except ValueError:
            # Maneja el caso en que el usuario no introduce un número válido
            print("Por favor, introduce un número válido.")



#juego 3
def print_board(board):
    """Imprime el tablero de Tic Tac Toe."""
    # Recorre cada fila del tablero
    for row in board:
        # Imprime las celdas de la fila actual separadas por " | "
        print(" | ".join(row))
        # Imprime una línea de guiones para separar las filas
        print("-" * 5)

def check_winner(board):
    """Verifica si hay un ganador o un empate en el tablero."""
    # Verificar todas las filas
    for row in board:
        # Si todas las celdas en la fila son iguales y no están vacías, hay un ganador
        if row[0] == row[1] == row[2] != " ":
            return row[0]  # Retorna el jugador ganador ("X" o "O")
    # Verificar todas las columnas
    for col in range(3):
        # Si todas las celdas en la columna son iguales y no están vacías, hay un ganador
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]  # Retorna el jugador ganador ("X" o "O")
    # Verificar la diagonal principal (de izquierda a derecha)
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]  # Retorna el jugador ganador ("X" o "O")
    # Verificar la diagonal secundaria (de derecha a izquierda)
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]  # Retorna el jugador ganador ("X" o "O")
    # Verificar si todas las celdas están llenas para determinar un empate
    if all(cell != " " for row in board for cell in row):
        return "Tie"  # Retorna "Tie" si hay un empate
    # Si no hay ganador y no hay empate, retorna None
    return None

def tic_tac_toe():
    """Función principal para jugar Tic Tac Toe."""
    # Inicializar el tablero vacío (3x3) con espacios en blanco
    board = [[" " for _ in range(3)] for _ in range(3)]
    # Establece el jugador que comienza ("X")
    current_player = "X"

    # Bucle principal del juego
    while True:
        # Imprime el estado actual del tablero
        print_board(board)
        # Imprime el jugador actual
        print(f"Turno del jugador {current_player}")

        # Solicitar la jugada al jugador actual
        try:
            # Leer la fila y columna ingresadas por el jugador, separadas por un espacio
            row, col = map(int, input("Introduce la fila y columna (0, 1, 2) separadas por un espacio: ").split())
            # Verifica si la celda seleccionada está vacía
            if board[row][col] != " ":
                # Si la celda no está vacía, informa al jugador y pide otra jugada
                print("¡Espacio ya ocupado! Intenta de nuevo.")
                continue  # Volver al inicio del bucle para pedir otra jugada
        except (ValueError, IndexError):
            # Captura errores de entrada inválida (no enteros o fuera de rango)
            print("Entrada inválida. Introduce dos números entre 0 y 2 separados por un espacio.")
            continue  # Volver al inicio del bucle para pedir otra jugada

        # Actualizar el tablero con la jugada del jugador actual
        board[row][col] = current_player

        # Verificar si hay un ganador o empate después de la jugada
        winner = check_winner(board)
        if winner:
            # Imprime el estado final del tablero
            print_board(board)
            if winner == "Tie":
                print("¡Es un empate!")
            else:
                print(f"¡El jugador {winner} gana!")
            break  # Terminar el juego

        # Cambiar de jugador para el siguiente turno
        current_player = "O" if current_player == "X" else "X"


#4 juego
        
def ask_question(question, options, correct_answer):
    1
    print(question)
    for idx, option in enumerate(options):
        print(f"{idx + 1}. {option}")
    
    try:
        answer = int(input("Selecciona la opción correcta (1-4): "))
        if options[answer - 1] == correct_answer:
            print("¡Correcto!\n")
            return True
        else:
            print("Incorrecto.\n")
            return False
    except (ValueError, IndexError):
        print("Entrada inválida. Se considera incorrecta.\n")
        return False

def quiz():
    
    #si quieren pueden añadir mas preguntas
    #nadamas en question ponen la pregunta
    #en option las opciones que quieren que aparescan
    #entre comillas y separadas por coma
    #y en correct answer la respuesta 
    questions = [
        {
            "question": "¿Cuál es la capital de Francia?",
            "options": ["Madrid", "París", "Roma", "Berlín"],
            "correct_answer": "París"
        },
        {
            "question": "¿Quién pintó la Mona Lisa?",
            "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"],
            "correct_answer": "Leonardo da Vinci"
        },
        {
            "question": "¿Cuál es el planeta más grande del sistema solar?",
            "options": ["Tierra", "Marte", "Júpiter", "Saturno"],
            "correct_answer": "Júpiter"
        },
        {
            "question": "¿Quién escribió 'Cien años de soledad'?",
            "options": ["Mario Vargas Llosa", "Gabriel García Márquez", "Isabel Allende", "Jorge Luis Borges"],
            "correct_answer": "Gabriel García Márquez"
        }
    ]

    score = 0  # Inicializar la puntuación

    for q in questions:
        if ask_question(q["question"], q["options"], q["correct_answer"]):
            score += 1

    print(f"Tu puntuación final es: {score} de {len(questions)}")

#si tienes dudas con el menu de aqui abajo 
# ve este video https://www.youtube.com/watch?v=DDX6vyP4lMc
#cualquier cosa mañana nos vemos por si tienes alguna duda men 
while True:
    print("por favor seleccione un juego: ")
    print("1. Ahorcado.")
    print("2. Adivinar numero.")
    print("3. gato")
    print("4. trivia")
    print("5. Salir")

    try:
        choice = int(input("Selecciona una opción (1-5): "))
    except ValueError:
        print("Por favor, introduce un número.")
        continue

    if choice == 1:
        play_hangman()
    elif choice == 2:
        adivinar_numero() 
    elif choice == 3:
        tic_tac_toe() 
    elif choice == 4:
         quiz()
    elif choice == 5:
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 5.\n")