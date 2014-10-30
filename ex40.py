__author__ = 'administrador'
# A partir de aqui vamos a aprender a usar las clases por lo que vamos a ponernos algo serios con todo
class Song(object):

    # CONSTRUCTORA DE LA CLASE
    # PONER SELF ES COMO PONER EN JAVA THIS.BLBALBLA Referencia la clase.
    def __init__(self, lyrics):
        self.lyrics = lyrics
        # Con SELF puedo meter los tipos de datos necesarios, no necesito declarar antes las variables privadas
        self.ruben = "Hola soy ruben"
    # METODOS DE LA CLASE
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
# A PARTIR DE AQUI ESCRIBO EL PROGRAMA PRINCIPAL

# Declaramos dos variables de tipo SONG
happy_birday = Song(["Happy birthday to you",
                     "I don't want to get sued",
                     "So i will stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "with pockets full of shells"])

# Ahora utilizo el metodo sing_me_a_song declarado anteriormente para que imprima la cancion completa.
happy_birday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()