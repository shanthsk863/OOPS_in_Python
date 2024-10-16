class Sports:
    def sportsnews(self):
        print('Sports News One ')
        print('Sports News Two ')
        print('Sports News Three')
        print('Sports News Four ')
        print('Sports News Five ')

class Movie:
    def movie_news(self):
        print('Movie News One')
        print('Movie News Two ')
        print('Movie News Three')
        print('Movie News Four ')
        print('Movie News Five ')

class Politics:
    def politics_news(self):
        print('Politics News One')
        print('Politics News Two ')
        print('Politics News Three')
        print('Politics News Four ')
        print('Politics News Five ')

class Shantesh_News_Hub:
    def __init__(self):
        self.sp = Sports()
        self.m = Movie()
        self.p = Politics()

    def get_all_news(self):
        print('Welcome To Shantesh News Hub!')
        self.sp.sportsnews()
        self.m.movie_news()
        self.p.politics_news()

    def disp(self):
        print('\nChoose the Option for the kind of news you would like to read:')
        print('1. Sports')
        print('2. Movie')
        print('3. Politics')
        print('4. Exit')

# Create an instance of the News Hub
sn = Shantesh_News_Hub()

while True:
    sn.disp()  # Display the options
    choice = input('Enter Your Choice [1-4]: ')

    if choice == '1':
        print("\nYou chose Sports news!")
        sn.sp.sportsnews()  # Call the sports news function
    elif choice == '2':
        print("\nYou chose Movie news!")
        sn.m.movie_news()  # Call the movie news function
    elif choice == '3':
        print("\nYou chose Politics news!")
        sn.p.politics_news()  # Call the politics news function
    elif choice == '4':
        print("Exiting the news reader. Have a great day!")
        break  # Exit the loop
    else:
        print("Invalid choice. Please choose a valid option.")
