import csv


def main():
    menu = """Songs To Learn - 1.0 By Owen Mathieson
    L - List of Songs
    A - Add New Song
    C - Complete A Song
    Q - Quit"""

    print(menu)

    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "L":
            printsongs = csv.DictReader('Songs.csv', delimiter=',')
            for line in printsongs:
                print(line["Song"]),
                print(line["Artist"])
                print(line["Year"])
                print(line["Learned?"])


        elif choice == "A":
            print("Hello")


        elif choice == "C":
            print("Hello")

        else:
            print("Invalid Option")
            choice = input(">>> ").upper()


main()