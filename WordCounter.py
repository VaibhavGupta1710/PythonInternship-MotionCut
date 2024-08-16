logo = """"
 __          __           _    _____                  _            
 \ \        / /          | |  / ____|                | |           
  \ \  /\  / /__  _ __ __| | | |     ___  _   _ _ __ | |_ ___ _ __ 
   \ \/  \/ / _ \| '__/ _` | | |    / _ \| | | | '_ \| __/ _ \ '__|
    \  /\  / (_) | | | (_| | | |___| (_) | |_| | | | | ||  __/ |   
     \/  \/ \___/|_|  \__,_|  \_____\___/ \__,_|_| |_|\__\___|_|   
                                                                   
                                                                   
"""

def wordcounter(text):
    count = 0
    text = text.replace(" ","")
    for i in text:
        count += 1
    return f"Total words are {count}"


def cont():
    while True:
        cont = input("Do you want to continue? (y/n):").lower()
        if cont == "y":
            break
        elif cont == "n":
            print("Thank you for using the word counter!")
            exit()
        else:
            print("Invalid input")
print(logo)


def main():
    to_continue = False
    while not to_continue:
        text = input("Enter a sentence or a paragraph: ")
        if text == "":
            print("You did not enter anything..")
            to_continue = True
            main()
        else:
            print(wordcounter(text))
            cont()


main()




