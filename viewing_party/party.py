# ------------- WAVE 1 --------------------

from enum import unique
from os import waitstatus_to_exitcode


def create_movie(title, genre, rating):
    movie_dict = {}
    movie_dict["title"] = title
    movie_dict["genre"] = genre
    movie_dict["rating"] = rating

    if movie_dict["title"] == None\
    or movie_dict["genre"] == None\
    or movie_dict["rating"] == None:
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



def watch_movie(user_data, title):  
    watch_list = user_data["watchlist"]
    for movie in watch_list:
        if (movie["title"]) == title:
            watch_list.remove(movie)
            user_data["watched"].append(movie)
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
    # print(genre_list)
    if len(genre_list) == 0:
        return None
    else:
       for j in range (len(genre_list)):
            popular_genre.append(genre_list[j]["genre"])
            # print(popular_genre)
    return max(set(popular_genre), key = popular_genre.count)




# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    # tried to use set and .difference() method to solve,
    # but finally found out need to return a list
    friends_list = []
    unique_list = []
    friend_watched = user_data["friends"]
    user_watched = user_data["watched"]

    for val in friend_watched:
        # read all the "watched" in friends watched list
        for movie in val["watched"]:
            # read every title/genre/rating in each watched
            friends_list.append(movie["title"])
            # put the name of the movie into the empty list
    for title in user_watched:
        # read every movie in user watched list
        if title["title"] not in friends_list: 
            unique_list.append(title)
    return unique_list   


def get_friends_unique_watched(user_data):
    user_watched_list = []
    friends_unique_movies = []
    friend_watched = user_data["friends"]
    user_watched = user_data["watched"]

    for title in user_watched:
        user_watched_list.append(title["title"])
    for watched in friend_watched: 
        for title in watched["watched"]:
            if title["title"] not in user_watched_list and\
               title not in friends_unique_movies:
               # and statement make sure the friends_unique_movies list
               # won't have duplicated elements 
                friends_unique_movies.append(title)
    return friends_unique_movies   




        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    """ use helper function from get_friends_unique_watched """

    recommended_movie = []
    subscriptions_list = user_data["subscriptions"]
    friens_unique_watched = get_friends_unique_watched(user_data)
    # call the funtion 'get_friends_unique_watched' 
    # and assign it to a new variable

    for i in range(len(friens_unique_watched)):
        if friens_unique_watched[i]["host"] in subscriptions_list:
            recommended_movie.append(friens_unique_watched[i])     
    return recommended_movie       
      
    


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    ''' 
    use helper function from get_most_watched_genre(user_data) 
    and get_friends_unique_watched()
    '''
    recommended_movie = []
    popular_genre = get_most_watched_genre(user_data)
    friends_unique_watched = get_friends_unique_watched(user_data)
    
    for i in range(len(friends_unique_watched)):
        # print(friens_unique_watched[i]["genre"])
        if friends_unique_watched[i]["genre"] == popular_genre:
            recommended_movie.append(friends_unique_watched[i])
    return recommended_movie



def get_rec_from_favorites(user_data):
    ''' 
    use the helper function get_unique_watched(user_data)
    to get the the movie list that none of the user's friends 
    have watched it 
    '''
    recommended_movie_by_favorite = []
    user_favorite_movies = user_data["favorites"]
    # access the list of the user's favorite movies
    friends_not_watched = get_unique_watched(user_data)
    # assign the helper function to a new variable
    
    for movie in friends_not_watched:  # loop the list of friends not watched
        if movie in user_favorite_movies:
            recommended_movie_by_favorite.append(movie) 
    return recommended_movie_by_favorite