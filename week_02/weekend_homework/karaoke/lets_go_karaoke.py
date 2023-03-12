from classes.room import Room
from classes.guest import Guest
from classes.song import Song
from classes.alcobot import Alcobot
from classes.drink import Drink

drink1 = Drink("Beer", 5, 2)
drink2 = Drink("Sake", 6, 4)
drinks_list = {drink1, drink2}
bot1 = Alcobot(666, 100, drinks_list)
guest1 = Guest("Bob Loblaw", 100, "I fought the law", 0)
guest2 = Guest("Stove Jeebs", 0, "lalalala", 20)

group1 = [guest1, guest2]
group2 = [
    guest1,
    guest2,
    guest1,
    guest2,
    guest1,
    guest2,
    guest1,
    guest2,
]
song1 = Song("Woowoowoo", "The Woo", 200)
song2 = Song("doopidoo", "The doo", 300)
song_list1 = [song1, song2]
song_list2 = [song1, song2, song1, song2]

room1 = Room(
    1,
    6,
    group1,
    song1,
    song_list1,
    song_list2,
    bot1,
)


def lets_go_karaoke():
    user_name = input("What is your name?")
    user_wallet = int(input("How much you want to spend?"))
    user_fav_song = input("What's your all time Karaoke favorite?")
    user_intoxication = int(input("How drunk are you already"))

    user = Guest(user_name, user_wallet, user_fav_song, user_intoxication)
    user_checked_in = False
    check_in = input("Do you want to check into a room? (y/n)")
    if check_in == "y":
        user_checked_in = True
        print(
            f"room {room1.id} has a space. you can join {[guest.name for guest in room1.guests]}"
        )

        while user_checked_in:
            choice = input(
                "OK, do you want to drink (d), sing (s), or hear a joke from the robo-bartender (j)?  If you have had enough fun you can exit (x)"
            )
            if choice == "x":
                user_checked_in = False
                print("Have a nice day 😘")
            if choice == "d":
                drink_choice = input(
                    "OK, let's drink!  do you want Beer (b), or Sake (s)"
                )
                if drink_choice == "b":
                    drink_choice = "Beer"
                if drink_choice == "s":
                    drink_choice == "Sake"
                room1.sell_drink(bot1, user, drink_choice)

            if choice == "j":
                print(bot1.tell_joke())


# lets_go_karaoke()
