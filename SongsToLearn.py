import csv
number_of_songs = 6

def main():
    choice = ""
    while choice != "Q":
        print("""Songs To Learn - 1.0 By Owen Mathieson
        {} Songs Loaded
        L - List of Songs
        A - Add New Song
        C - Complete A Song
        Q - Quit""".format(number_of_songs))



        choice = input(">>> ").upper()


        if choice == "L":
            with open('SongList.csv') as songreader:
                songs = list(csv.reader(songreader, delimiter=','))
                for i in range(0, len(songs), 1):
                    print(i, '. {}'.format(songs[i]))





        elif choice == "A":
            print("Hello")


        elif choice == "C":
            print("Hello")

        else:
            print("Invalid Option")
            choice = input(">>> ").upper()


main()
