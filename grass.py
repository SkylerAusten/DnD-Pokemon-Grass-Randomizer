import random

def generate_map():
    pokemon_spots = []
    counter = 0
    while counter < 12:
        coordinate = (random.randint(1, 6), random.randint(1, 7))
        if not coordinate in pokemon_spots:
            counter += 1
            pokemon_spots.append(coordinate)
    grass_map = []
    grass_map.append(["#", "A", "B", "C", "D", "E", "F", "G"])
    
    for column in range(1, 7):
        grass_map.append([str(column)] + ["-"] * 7)

    for spot in pokemon_spots:
        grass_map[spot[0]][spot[1]] = "*"
    
    for i in grass_map:
        print(i)

    print(len(pokemon_spots))
    #for row in range(1, 7):
    #    grass_map += "\n" + str(row) + " "
    #    for column in range(1, 8):
    #        grass_map += random.choice(weighted_options) + " "
    #print(grass_map)

def open_map():
    print()

def game():
    print()


def main():
    names = ["Eric", "Clement", "William", "James"]
    initials = [i[0] for i in names]

    starter_message = """Program options:
    1. Continue with the last saved randomized map.
    2. Generate a new randomized map.
    3. Exit the program."""

    while True:
        #try:
        print(starter_message)
        program_mode = int(input("Option: "))

        if program_mode == 1:
            map_state = open_map()
            game(map_state)
            break

        elif program_mode == 2:
            map_state = generate_map()
            game(map_state)
            break

        elif program_mode == 3:
            print("Exiting...")
            return

        else:
            print("Invalid option!  Please enter '1', '2', or '3'")

        #except:
            #print("Invalid option!  Please enter '1', '2', or '3'")

if __name__ == "__main__":
    main()