questions = ("¿Cúantos elementos hay en una tabla periodica?",
             "Qué animal deja los huevos más grandes?",
             "¿Cuál es el gas más abundante en la atmosfera de tierra?",
             "¿Cuántos huesos hay en el cuerpo humano?",
             "¿Qué planetaen el sistema solar es el más caliente?")
options = (("A. 116" , "B. 117" , "C. 118" , "D. 119"), 
           ("A. Ballena" , "B. Cocodrilo" , "C. Elefante" , "D. Avestrúz"), 
           ("A. Nitrogeno" , "B. Oxigeno" , "C. Dioxido de carbono" , "D. Hidrógeno"),
           ("A. Mercurio" , "B. Venus" , "C. Tierra" , "D. Marte"))
answers = ("C", "D", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
print ("La respuesta correcta es la letra: ")
print (question)
