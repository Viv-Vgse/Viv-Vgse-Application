import os
import platform

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def game():
    
    print("Welcome to the Kingdom of Undervale!")
    print("A blight has spread across the land, and all hope is fading.")
    print("Legends speak of the Staff of Light, hidden deep within the Cave of Doom.")
    print("It is said only the true hero can wield the staff to dispel the accursed Blight")
    print("You, a brave adventurer, have taken it upon yourself to find the Staff and save the kingdom.")
    print("Will you be successful in your quest to save Undervale? Or perish like others in the Cave of Doom?")
    print("Are you ready to begin your quest?")
    choice=input("Enter Yes or No\n").lower()
    if choice == "yes":
        main()
    elif choice == "no":
        clear_screen()
        print("Goodbye, adventurer. It seems the fate of Undervale remains unseen, or does it?..")
        print("Would you like to try again?")
        choice=input("Enter Yes or No\n").lower()
        if choice == "yes":
            clear_screen()
            game()
        elif choice == "no":
             clear_screen()
             print("Thank you for playing!")
             game_over()
    
    else:
        clear_screen()
        print("Invalid response. Please try again.")
        game()
    
                



def main():
    clear_screen()
    print("You stand at the edge of the path leading to the Cave of Doom.")
    print("What will you do?")

    print("1. Go down the path and enter the Cave of Doom")
    print("2. Search the area for any supplies")
    print("3. Speak to the local townsfolk for information")
    print("4. Choose to end your quest and leave the fate of Undervale to the darkness")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        enter_cave()
    elif choice == "2":
        search_area()
    elif choice == "3":
        speak_townsfolk()
    elif choice == "4":
        print("You have chosen to end your quest. The Blight will ravish the Kingdom of Undervale. Game Over")
        print("Would you like to play again?")
        choice = input("Enter Yes or No\n").lower()
        if choice == "yes":
            clear_screen()
            game()
        elif choice == "no":
            clear_screen()
            print("Thank you for playing!")
        game_over()
    else:
        print("Invalid choice. Please try again.")
        main()



def enter_cave():
    clear_screen()
    print("You proceed to enter the Cave of Doom. Its air is filled with malice, giving you a foreboding feeling.")
    print("Suddenly, you see an ancient Guardian wielding a fiery sword.")
    print("What will you do?")
    print("1. Fight")
    print("2. Flee")
    print("3. Reason")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        if 'amulet' in inventory:
            print("You fight bravely, and the Amulet of Plot-Armour saves you from the Guardian's attacks.")
            print("The guardian acknowledges your efforts. Impressed, he says:")
            print("\"You are clearly worthy of passing the 3 challenges required to obtain the Staff of Light.\"")
            print("\"Lest Undervale be stricken by the Blight, hear me well and answer my first challenge.\"")
            challenge1()
        else:
            clear_screen()
            print("You fight bravely, but the guardian is too powerful. You are bested like those before you in the Cave of Doom.")
            print("Game Over.")
            game_over()
    elif choice == "2":
        clear_screen()
        print("You flee, leaving Undervale to its fate. Darkness engulfs the land and the Blight remains forever.")
        print("Game Over.") 
        game_over()
    elif choice == "3":
        reason()
    else:
        clear_screen()
        print("Invalid choice. Please try again.")
        enter_cave()

def reason():
    clear_screen()
    print("You speak with the Guardian and reason with him")
    print("The guardian listens and says \"You must pass 3 challenges to be bestowed the Staff of Light\"")
    print("\"Lest Undervale be stricken by the Blight. Hear me well and answer my challenge.\"")
    challenge1()
def challenge1():
    print("The guardian asks you the first of 3 questions:")
    print("\"I have roots as nobody sees, I am as tall as trees, up up up I go, yet I never grow?\"")
    print("\"What am I?\"")
    print("1. Eggs")
    print("2. Mountain")
    print("3. Feet")

    choice = input("Enter the number of your choice: ")

    if choice == "1" or choice == "3":
        clear_screen()
        print("\"That is incorrect. It seems you are not the hero afterall.\"")
        print("Game Over.")
        game_over()
    elif choice == "2":
        challenge2()
        
             
    else:
            clear_screen()
            print("Invalid choice. Please try again.")
            challenge1()
    

def search_area():
    clear_screen()
    print("You search the area and find the Amulet of Plot-Armour. Whatever could it be useful for?")
    print("Will you take the amulet of Plot-Armour?")
    choice=input("Enter Yes or No:\n").lower()
    if choice == "yes":
        inventory.append('amulet')
        print("You now have the Amulet of Plot-Armour.")
        print("Will you proceed to the Cave of Doom?")
        choice=input("Enter Yes or No:\n").lower()
        if choice == "yes":
            enter_cave()
        elif choice == "no":
            print("Will you abandon your quest to save Undervale?")
        choice=input("Enter Yes or No:\n").lower()
        if choice == "no":
            enter_cave()
        elif choice == "yes":
            print("Goodbye, adventurer. It seems the fate of Undervale remains unseen, or does it?..")
            print("Would you like to try again?")
            choice=input("Enter Yes or No\n").lower()
            if choice == "yes":
                clear_screen()
                game()
            elif choice == "no":
                clear_screen()
                print("Thank you for playing!")
                game_over()
            else:print("Invalid response. Please try again.")
    elif choice == "no":
        print("You leave behind this strange amulet; having no meaning in this world of Undervale.")
        print("Will you proceed to the Cave of Doom?")
        choice=input("Enter Yes or No:\n").lower()
        if choice == "yes":
            enter_cave()
        elif choice == "no":
            print("Will you abandon your quest to save Undervale?")
        choice=input("Enter Yes or No:\n").lower()
        if choice == "no":
            enter_cave()
        elif choice == "yes":
            print("Goodbye, adventurer. It seems the fate of Undervale remains unseen, or does it?..")
            print("Would you like to try again?")
            choice=input("Enter Yes or No\n").lower()
            if choice == "yes":
                clear_screen()
                game()
            elif choice == "no":
                clear_screen()
                print("Thank you for playing!")
    else:

        print("Invalid choice. Please try again.")
        search_area()   
  

def speak_townsfolk():
    clear_screen()
    print("You speak to the local townsfolk, but they reply in a language unknown to you.")
    print("You then remember you're a brave adventurer, from a foreign land. D'oh!")
    print("Chin up adventurer, everyone forgets they're not really from Undervale!")
    print("Will you press on towards the Cave of Doom?")
    choice=input("Enter Yes or No:\n").lower()
    if choice == "yes":
        enter_cave()
    elif choice == "no":
        print ("Are you abandoning your quest to save Undervale?")
        choice=input("Enter Yes or No:\n").lower()
        if choice == "Yes":
            print("Goodbye, adventurer. It seems the fate of Undervale remains unseen, or does it?..")
            print("Would you like to try again?")
        choice=input("Enter Yes or No\n").lower()
        if choice == "yes":
            clear_screen()
            game()
        elif choice == "no":
             clear_screen()
             print("Thank you for playing!")
        else: print("Invalid response. Please try again.")
    else:print("Invalid response. Please try again.")   

def challenge2():
    clear_screen()
    print("\"That is correct hero. On to my next challenge.\"")
    print("\"Alive without breath, as cold as death, never thirsty, always drinking, all in mail, never clinking?\"")
    print("\"What am I?\"")
    print("1. Fish")
    print("2. Knight")
    print("3. Feet")

    choice = input("Enter the number of your choice: ")

    if choice == "2" or choice == "3":
        clear_screen()
        print("\"That is incorrect. It seems you are not the hero afterall.\"")
        game_over()
    elif choice == "1":
        challenge3()
    else:
        clear_screen()
        print("Invalid choice. Please try again.")
        challenge2()

def challenge3():
    clear_screen()
    print("\"That is correct! On to the final and most fateful challenge\"")
    print("\"What is the meaning of life?\"")
    print("1. Being the best you can be")
    print("2. Have no regrets")
    print("3. 42")

    choice = input("Enter the number of your choice: ")

    if choice == "1" or choice == "2":
        clear_screen()
        print("The Guardian looks disappointed.")
        print("\"Those are both fine answers young warrior, yet that is not the true meaning of life.\"")
        print("\"It seems my faith in you was misplaced. The Blight afterall will consume Undervale.\"")
        print("Game Over.")
        game_over()
    elif choice == "3":
        clear_screen()
        print("The guardian was impressed, a smile seemed to appear across his face.")
        print("\"You are both well-travelled and knowledgeable.\" The Guardian said.\"The Staff of Light will pass to your hands young adventurer.\"")
        print("You wielded the magical staff, dispelling the blight from the lands of Undervale")
        print("Congratulations on returning the Kingdom of Undervale to peace and prosperity!")
        print("I hope you enjoyed your journey, and the little easter eggs for those of you who found them")
        print("Thank you for playing!")
        game_over()
    else:
        clear_screen()
        print("Invalid choice. Please try again.")
        challenge3()

def game_over():
    print("Would you like to play again? (yes/no)")
    choice = input("Enter Yes or No:\n").lower()
    if choice == "yes":
        clear_screen()
        game()
    elif choice == "no":
        clear_screen()
        print("Thank you for playing!")
    else:
        clear_screen()
        print("Invalid response. Please try again.")
        game_over()

if __name__ == "__main__":
    inventory = []
    game()
    main()