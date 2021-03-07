print('''                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \\
             \________________\####/________________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__    '-. \\uuu/.-'    __/ \__ |
              |============= .'.'^'.'.=============|
              |  _\\o/   __  {.' __  '.} _   _\\o/  _|
              `""""-""""""""""""""""""""""""""-""""`''')


print("\n\nWelcome to Treasure Island.")
print("Your mission is to find the treasure.")


level1=input("You are at a cross road. Where do you want to go? \"left\" or \"right\"\n")
if(level1=="left" or level1=="Left" or level1=="LEFT"):
    level2=input("You come to a lake. There is a island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
    if (level2=="wait" or level2=="Wait" or level2=="WAIT" ):
        level3=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")


        if(level3=="red" or level3=="Red" or level3=="RED"):
            print("It's a room full of fire. Game Over")
            print('''             --|-------------|--
               |  GAME OVER  |
             --|-------------|--''')



        elif(level3=="yellow" or level3=="Yellow" or level3=="YELLOW"):
            print("You found the treasure! You Win!")
            print('''                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-\'''')



        elif(level3=="blue" or level3=="Blue" or level3=="BLUE"):
            print("You enter a room of beasts. Game Over.")
            print('''             --|-------------|--
               |  GAME OVER  |
             --|-------------|--''')



        else:
            print("You chose a door that doesn't exist. Game Over")
            print('''             --|-------------|--
               |  GAME OVER  |
             --|-------------|--''')



    else:
        print("You get attacked by an angry trout. Game Over.")
        print('''             --|-------------|--
               |  GAME OVER  |
             --|-------------|--''')


else:
    print("You fell into a hole. Game Over.")
    print('''             --|-------------|--
               |  GAME OVER  |
             --|-------------|--''')


q= input("press anything to end the program:-")
