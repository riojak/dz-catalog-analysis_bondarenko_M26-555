import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]}, # noqa: E501
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies_check):
    if not movies_check:
        return 0.0

    summ_rating = 0.0
    for movie in movies_check:
        summ_rating += movie['rating']
    return round(summ_rating / len(movies_check), 1)


def catalog_age_stats(movies_check, current_year=2026):
    if not movies_check:
        return (0, 0, 0)

    years_list = []
    for movie in movies_check:
        age = current_year - movie['year']
        years_list.append(age)
    
    oldest = max(years_list)
    newest = min(years_list)
    avg = math.ceil(sum(years_list) / len(movies_check))

    return (oldest, newest, avg)

def duration_in_hours(minutes):
    
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f'{hours}ч {remaining_minutes}м'

def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    return "средне" if rating >= 5 else "слабо"

def decade_label(year):

    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"

for movie in movies:
    if 'comedy' in movie['genres']:
        continue
    print(movie['title'])

i = 0
while i < len(movies):
    if movies[i]["rating"] > 9.0:
        print(movies[i]["title"])
        break
    i += 1
else: 
    print("Шедевров не найдено")

def count_long_movies(movies_check, threshold=120):
    n = 0
    for movie in movies_check:
        if movie['duration_min'] > threshold:
            n += 1
    return n

def normalize_title(title):
    result = []
    words = title.split()
    for word in words:
        result.append(word[0].upper() + word[1:])
    return ' '.join(result)

def make_slug(title):
    start = normalize_title(title)
    result = start.lower().replace(' ', '-')
    return result

def format_report_line(movie):
    genres_text = ", ".join(sorted(movie["genres"]))
    duration_text = duration_in_hours(movie['duration_min'])
    movie_title = normalize_title(movie['title'])
    return (
        f'"{movie_title}" ({movie['year']}) — '
        f'{movie['rating']}/10, {duration_text}, жанры: {genres_text}'
    )

def titles_sorted_by_rating(movies_check):
    sorted_movies = sorted(
        movies_check, 
        key=lambda movie: movie['rating'], 
        reverse=True
    )
    result = []
    for movie in sorted_movies:
        result.append(movie['title'])
    return result

def top_n_by_rating(movies_check, n=3):
    sorted_movies = sorted(
        movies_check,
        key=lambda movie: movie['rating'],
        reverse=True
    )
    result = []
    for movie in sorted_movies[:n]:
        result.append((movie['title'], movie['rating']))
    return result

def count_by_genre(movies_check):
    genre_counts = {}
    for movie in movies_check:
        for genre in movie['genres']:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1
    return genre_counts

def actor_filmography(movies_check):
    filmography = {}
    for movie in movies_check:
        for actor in movie['actors']:
            if actor not in filmography:
                filmography[actor] = []
            filmography[actor].append(movie['title'])
    return filmography

avg_rating = average_rating(movies)
title_rating = {
    movie['title']: movie['rating']
    for movie in movies
    if movie['rating'] > avg_rating
}

def all_genres(movies_check):
    all_found_genres = set()
    for movie in movies_check:
        all_found_genres.update(movie['genres'])
    return all_found_genres

def common_actors(movie1, movie2):
    result1 = set(movie1['actors'])
    result2 = set(movie2['actors'])
    common = result1 & result2
    return common

def genres_only_in_one(movies_a, movies_b):
    genres_a = all_genres(movies_a)
    genres_b = all_genres(movies_b)
    difference = genres_a - genres_b
    return difference

def iter_high_rated(movies_check, min_rating=8.0):
    for movie in movies_check:
        if movie['rating'] >= min_rating:
            yield movie

for movie in iter_high_rated(movies):
    print(format_report_line(movie))

total_duration = sum(movie['duration_min'] for movie in movies if movie['rating'] > 7)