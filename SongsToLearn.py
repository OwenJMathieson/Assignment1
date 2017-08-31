import csv
number_of_songs = 6
songreader = open('SongList.csv')
songs = list(csv.reader(songreader, delimiter=','))
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


            for i in range(0, len(songs), 1):
                if songs[i][3] == 'Y':
                    songs[i][3] = '*'
                else:
                    songs[i][3] = ''
                print(i, '. {:1} {:30} {:1} {:30} {} {} {}'.format(songs[i][3], songs[i][0], '- ', songs[i][1],'(', songs[i][2], ')'))





        elif choice == "A":
            title = str(input("Title:"))
            while title == "":
                print("Input cannot be blank.")
                title = str(input("Title:"))


            artist = str(input("Artist:"))
            while artist == "":
                print("Input cannot be blank.")
                artist = str(input("Artist:"))

            year = int(input("Year:"))
            while year <= 0:
                print("Invalid Input; enter a valid number")
                year = input("Year:")

            new_song = [title, artist, year,'N']
            songreader = open('SongList.csv', 'w', newline='')
            songs.append(new_song)
            writer = csv.writer(songreader, delimiter=",")
            for lines in songs:
                writer.writerow(lines)
            songreader.close()











        elif choice == "C":
            print("Hello ")


        else:
            print("Invalid Option")
            choice = input(">>> ").upper()


main()
