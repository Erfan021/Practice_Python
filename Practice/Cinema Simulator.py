# Cinema Simulator

films = {
    "Captain Marvel": [12,5],
    "Night School": [18,5],
    "What Men Want": [18,5],
    "Avengers 4": [18,5]
}

while True:
    movie_choice = input("Which movie do you want to watch?: ").strip().title()
    if movie_choice in films:
        # check user age
        age = int(input("How old are you? ").strip())
        if age >= films[movie_choice][0]:
            # check if seats available
            num_seats = films[movie_choice][1]
            if num_seats > 0:
                films[movie_choice][1] = films[movie_choice][1] - 1
                print("Enjoy the film")
            else:
                print("Sorry, movie is sold out!")
        else:
            print("You are too young to watch the film")
    else:
        print("We don't have that film..!")
