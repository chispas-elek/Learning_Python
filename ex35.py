from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"
    choice = raw_input("> ")
    # Deberia declararse la variable aqui
    # how_much = -1

    # Este bloque significa que si choice contiene 0 o 1 entonces el programa sigue adelante
    if "0" in choice or "1" in choice:
        # Se pueden crear variables locales que funcionan dentro del bloque def
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy , you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print "There is a bear here"
    print "The bear has a bunch of honey"
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    # Esto es una forma de hacer un bucle while infinito, no vale para el paradigma de la programacion

    while True:
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now"
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."

def cthulu_room():
    print "Here you see the great evil Cthulu"
    print "He, it, whatever stares at you and you go insane"
    print "Do you flee for your live or eat your head?"

    choice = raw_input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulu_room()

def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room"
    print "There is a door to your right and left"
    print "Which one do you take?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve.")

# Ejecucion principal del programa, al ser funciones el codigo llega hasta aqui y se ejecuta esto que se ve
start()

# Pass me permite hacer un bloque vacio. util para hacer un equeleto que luego debo llenar
def vacio():
    pass
