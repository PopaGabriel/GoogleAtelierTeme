import random

list_of_words = ['dezoxiribonucleic', 'Andrei', 'perdea', 'abecedar', 'capra', 'ostrogot', 'ostropel']

lives = 6


def print_lives(life):
    if life == 5:
        print("""
                             ______
                            /      \\
                            \\______/ 
                """)

    if life == 4:
        print("""
                             ______
                            /      \\
                            \\______/
                                |
                                |        
                                |         
                                |                   
                """)
    if life == 3:
        print("""
                             ______
                            /      \\
                            \\______/
                            __  |  __
                             \\ | /       
                              \\|/         
                                |         
                """)

    if life == 2:
        print("""                   
                                     ______
                                    /      \\
                                    \\______/
                                    __  |  __
                                     \\ | /       
                                      \\|/         
                                        |
                                       //\\
                                      //  \\
                                    //     \\      
                        """)
    if life == 1:
        print("""
                                     ______ 
                                    /      \\
                                    \\______/
                                    __  |  __
                                     \\ | /       
                                      \\|/         
                                        |
                                       //\\
                                      //  \\
                                    //     \\
                                |||||||||||||||||||
                                        Paie
                                |||||||||||||||||||      
                        """)
    if life == 0:
        print("""                  
                                     ______ 
                                    /      \\
                                    \\______/
                                    __  |  __
                                     \\ | /       
                                      \\|/         
                                        |
                                       //\\
                                      //  \\
                                    //     \\
                                |||||||||||||||||||
                                Arde uite cum arde
                                |||||||||||||||||||      
                        """)


aux = list_of_words[random.randint(0, len(list_of_words))]
word_din_lista = list(aux)
words_deja_bagati = {}

word_empty = ['_' for _ in range(len(word_din_lista))]

for i, val in enumerate(word_din_lista):
    if val == aux[0]:
        word_empty[i] = aux[0]
    if val == aux[-1]:
        word_empty[i] = aux[-1]

words_deja_bagati[aux[0]] = 1
words_deja_bagati[aux[-1]] = 1

print("".join(word_empty))
while ("".join(word_empty)).find('_') != -1 and lives > 0:
    character = input("Hit me!\n")

    while len(character) > 1:
        character = input("Mai baga o fisa\n")

    if words_deja_bagati.get(character) is not None:
        print("Ai mai bagat deja o data")
        continue

    words_deja_bagati[character] = 1

    pozitie = aux.find(character)
    poz = 0
    if pozitie == -1:
        lives -= 1
    else:
        pozitie = -1
        while poz != -1:
            pozitie += 1
            poz = aux[pozitie:].find(character)
            pozitie += poz
            word_empty[pozitie] = character

    print("Mai ai {} vieti".format(lives))
    print(print_lives(lives))
    print("".join(word_empty))
