import random

from faker import Faker
fake = Faker()

fake = Faker("pl_PL")
video_list = []


class Movies:
    def __init__(self, title, year, type, numbers_of_plays):
        self.title = title
        self.year = year
        self.type = type
        #Variables
        self.numbers_of_plays = numbers_of_plays

    #def plays(self, step=1):
     #   self.numbers_of_plays += step

    def __str__(self):
        return f'{self.title}, {self.year},{self.type}, {self.numbers_of_plays}' # {self.episode_number}, {self.season_number}'
    def __repr__(self):
        return f'(title: %s, year: %s, type: %s, numbers_of_plays: %s)' % (
            self.title, self.year, self.type, self.numbers_of_plays)


class Serials(Movies):
    def __init__(self, season_number, episode_number,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season_number = season_number
        self.episode_number = episode_number

    def movie_list(self):
        return f" film {self.title}  {self.year}"

    def series_list(self):
        return f"{self.title} S{self.season_number}E{self.episode_number}"


    def __repr__(self):
        return f'(title: %s, year: %s, type: %s, numbers_of_plays: %s, S%d, E{1:02d}%d )' % (
            self.title, self.year, self.type, self.numbers_of_plays, self.season_number, self.episode_number)

#generowanie list filmów i seriali
def base(copies):
    type_list = ["Comedy", "Action", "Thriller", "Horror", "Romance"]
    for movie_list in range (copies):
        video_list.append(Movies(
            title=fake.last_name(),
            year=fake.year(),
            type= random.choice(type_list),
            numbers_of_plays= fake.random_int(0,10)
        ))
        video_list.append(movie_list)

    return video_list

def series(copies):
    type_list = ["Comedy", "Action", "Thriller", "Horror", "Romance"]
    for series_list in range(copies):
        video_list.append(Serials(
            title=fake.last_name(),
            year=fake.year(),
            type=random.choice(type_list),
            season_number=fake.random_int(1, 4),
            episode_number=fake.random_int(0, 20),
            numbers_of_plays=fake.random_int(0, 10)
        ))
        video_list.append(series_list)

    return video_list


# create another list to take out only movies - sorted
def get_movies(video_list):
    movie_list = []
    for item in video_list:
        if item.isMovies() == True:
            movie_list.append(item)
    movie_list_by_title = sorted(movie_list, key=lambda item: item.title)

    print("Lista poukładana alfabetycznie")
    print(movie_list_by_title)

#create another list to take out only series - sorted
def get_series(video_list):
    series_list = []
    for item in video_list:
        if item.isMovies() == False:
            series_list.append(item)
    series_list_by_title = sorted(series_list, key=lambda item: item.title)
    print("Lista poukładana alfabetycznie")
    print(series_list_by_title)


def prepare_movies():
    welcome = input("Jakiego rodzaju chcesz video 1 = Movies, 2 = Series")
    copies = int(input("ile kopii?:"))
    get_classic_movies = input("Czy chcesz zobaczyc tylko filmy? Y/N")
    get_series_video = input("Czy chcesz zobaczyć tylko seriale? Y/N")
    if welcome == "1":
        print(base(copies))
    elif welcome == "2":
        print(series(copies))
    elif get_classic_movies == "Y" or "y" or "yes":
            get_movies(video_list)
    elif get_classic_movies == "N" or "n" or "no":
        print("Okey no problem")
    elif get_series_video == "Y" or "y" or "yes":
            get_series(video_list)
    elif get_series_video == "N" or "n" or "no":
        print("Okey no problem")
    else:
        error = "error"
        print(error)
        exit()


##Program
if __name__ == "__main__":
    print("Hello")
    #print("Print >>> Y/N <<< to create new video list: ")

    choice = input("Print >>> Y/N <<< to create new video list: ")

    while True:
        if choice == "Y" or "y" or "yes":
            prepare_movies()
            #generate_data()
            #continue
        else:
            error = "error"
            print(error)
            exit()