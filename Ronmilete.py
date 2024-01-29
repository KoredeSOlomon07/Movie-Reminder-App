# Import datetime libraries
from datetime import datetime


# Define the main function
def main():

    try:
        # Initialize movie list
        moviesList = []

        # Open the moviesList.txt file for reading
        infile = open("moviesList.txt", "r")
        line = infile.readline()

        # Open the file, read the contents, and add movies.List
        while line:
            moviesList.append(line.rstrip("\n").split(","))
            line = infile.readline()
        # Close the input file
        infile.close()
        # this is an error handling line of cose this code will run when a txt file isn't find and it wil create a new txt file.
    except FileNotFoundError:
        print("The moviesList.txt file is not found.")
        print("Starting a new movies list!")
        moviesList = []

# Call the menu function to display options and process user's choice
    choice = 0
    while choice != 4:
        print("<<<Movie Manager>>>")
        print("1) Add a Movie")
        print("2) Search for a Movie")
        print("3) Display Moive")
        print("4) Quit")

        try:
            # Get user choice
            choice = int(input("Enter your choice from 1 - 4: "))
        except ValueError:
            print("Invalid number. Please enter a right number.")
            continue

        # this line of code helps to create or Add to to a new or existing Movies file.
        if choice == 1:
            print("Adding a Movie my guy 😛")
            Movie = input("Enter the Title of this Movie :- ")
            Actor = input("Enter the Main Actor's Name:- ")
            date_released = input("Input the date release (YYYY-MM-DD): ")
            # Try to convert the 'date_released' input to a datetime object using the format '%Y-%m-%d'.
# If successful, it implies a valid date format; otherwise, catch the ValueError.
            try:
                datetime.strptime(date_released, '%Y-%m-%d')
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                # Continue to the next iteration of the loop to prompt the user again for a valid input.
                continue

            rating = input("Enter the Rating (out of 5): ")
            try:
                rating = float(rating)
            except ValueError:
                print("Invalid rating. Please enter a valid number.")
                continue
            Short_Descriptipon = input("Narrate the Movie for us in a bit :- ")
            Chracters_Name = input(
                "Enter the names of Characters you could remember :-")
            moviesList.append(
                [Movie, Actor, Short_Descriptipon, rating, date_released, Chracters_Name])
            print("You Successfully Add a moive")
        # this line of code search for a aparticular Movie using keyword such as the Movie (i.e the movie name)
        elif choice == 2:
            print("Looking up for Movie...")
            keyword = input("Enter Search Term: ")
            for movie in moviesList:
                if keyword in movie:
                    print(movie)

        # This Part  Displays all the moviess added to my file
        elif choice == 3:
            print("Displaying all movies...")
            for i in range(len(moviesList)):
                print(moviesList[i])
        # This is a part where all code will stop running
        elif choice == 4:
            print("Quitting Program")
    print("Program Terminated!")

    # Saving to external TXT file
    with open("moviesList.txt", "w") as outfile:
        for movie in moviesList:
            outfile.write(",".join(map(str, movie)) + "\n")


# Check if the script is run as the main program
if __name__ == "__main__":
    main()
