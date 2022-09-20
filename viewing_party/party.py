# ------------- WAVE 1 --------------------

from os import waitstatus_to_exitcode


def create_movie(title, genre, rating):
    movie_dict = {}
    movie_dict["title"] = title
    movie_dict["genre"] = genre
    movie_dict["rating"] = rating

    if movie_dict["title"] == None or movie_dict["genre"] == None or movie_dict["rating"] == None:
        return None
       
    return movie_dict

def add_to_watched(user_data, movie_dict):
    # "watched" is the key, the whole movie_dict as a value thta 
    # append into the user_data which is also a dictionary
    user_data["watched"].append(movie_dict)
    return user_data


def add_to_watchlist(user_data, movie_dict):
    user_data["watchlist"].append(movie_dict)
    return user_data


def watch_movie(user_data, title):  # this one can still improve
    # get the values from the user_data's "watchlist" key, and put them into a list
    watch_list = user_data["watchlist"]
    watch_list_size = len(watch_list)
    for i in range(watch_list_size):
        # try to use for movie in watch_list
        if watch_list[i]["title"] == title:
            movie = watch_list[i]
            add_to_watched(user_data, movie)
            watch_list.remove(movie) 
            return user_data
    return user_data




# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    rating_list = []
    ratings_sum = 0
    watch_list = user_data["watched"]
    # access the list inside the dict
    if len(watch_list) == 0:   # check if the list is empty
        return 0.0
    else: 
        for i in range(len(watch_list)):    
            rating_list.append(watch_list[i]["rating"])
            # a list contains elements, each elements as a key-value pair
            # watch_list[i]["rating"] only access the value from the key names "rating"
    for rate in rating_list:
        # access every rate inside the rating list
        ratings_sum += rate
        # add the rates together
    average = ratings_sum/len(rating_list)
    return average
    
    
def get_most_watched_genre(user_data):
    popular_genre = []
    genre_list = user_data["watched"]
    print(genre_list)
    if len(genre_list) == 0:
        return None
    else:
       for j in range (len(genre_list)):
            popular_genre.append(genre_list[j]["genre"])
            print(popular_genre)
    
    return max(set(popular_genre), key = popular_genre.count)

# def most_frequent(List):
# return max(set(List), key = List.count)

# List = [2, 1, 2, 2, 1, 3]
# print(most_frequent(List))

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

