import random
import pyttsx3



def main():
 

    def setup_player():
# TODO: Ask the user for their name using input()
        name = input("User what is your name?\n")

# TODO: Initialize a dictionary with keys: "name", "health", and "inventory"
        stats_dictionary = {
                "name": name,
                "health": 10,
                "inventory":[]
        }
            
# TODO: Return the dictionary
        return stats_dictionary



    def create_treasures(): 
        # TODO: Create a dictionary of treasure names and integer values
        treasures_dictionary = {
            
                    "gold coin": 5,
                    "ruby": 10,
                    "ancient scroll": 7,
                    "emerald": 9,
                    "silver ring": 4
        }
        # TODO: Return treasures_dictionary
        return treasures_dictionary




    def display_options(room_number):  
   # TODO: Print the room number and the 4 menu options 
        print(f"You are in room {room_number}.")
        print("What would you like to do?")
        print("1. Search for treasure")
        print("2. Move to next room")
        print("3.Check health and inventory")
        print("4. Quit the game")
    


      


    def search_room(player, treasures):
        
        # TODO: Randomly assign outcome = random.choice(["treasure", "trap"])
        outcome = random.choice(["treasure", "trap"])

        # TODO: Write an if/else to handle treasure vs trap outcomes
        if outcome == "treasure":
            random_treasure = random.choice(treasures.keys())
            player["Inventory"].append(random_treasure)
            print(f"{random_treasure} was added to your inventory")
        elif outcome == "trap":
        # TODO: Update player dictionary accordingly
            player['health'] -= 2
        # TODO: Print messages describing what happened    
            print("You ran into a trap and lost 2 health")

    


    def check_status(player):
     
        # TODO: Print player health
        print(f"Player health: {player['health']}")

        # TODO: If the inventory list is not empty, print items joined by commas
        if player['Inventory'] != []:

        # TODO: Otherwise print“You have no items yet."
            print("You have no items yet.")
            
            



    def end_game(player, treasures):
    
     
        # TODO: Calculate total score by summing the value of collected treasures
        total_value = 0
        for treasure in player['inventory']:
            total_value += treasures[treasure]

        # TODO: Print final health, items, and total value
        print(f"health = {player['health']}")
        print(f"Inventory (total value ={total_value})=")

        # TODO: End with a message like "Game Over! Thanks for playing."
        print("Would you like to play a game?")
        import pyttsx3


        engine = pyttsx3.init()

        text = "Would you like to play a game?"

        engine.say(text)
        engine.runAndWait()


       


    def run_game_loop(player, treasures):
        # TODO: Loop through 5 rooms (1–5)
        for room in range(1,6):

        # TODO: Inside each room, prompt player choice using input()
            while True:
                display_options(room)
                selection = input("Please select 1 - 4 ")

        # TODO: Use if/elif to handle each choice (1–4)
                if selection == "1":
                    search_room(player, treasures)

        # TODO: Break or return appropriately when player quits or dies
                if selection == "2":
                    break
                if selection =="3":
                    check_status(player)
                if selection == "4":
                    end_game(player, treasures)
                    return
                else:
                    print("Invalid input")

       # TODO: Call end_game() after all rooms are explored
        end_game(player, treasures)
                
        

       


        # -----------------------------------------------------
        # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------
    player = setup_player()
    treasures = create_treasures()

    run_game_loop(player, treasures)

if __name__ == "__main__":
    main()
