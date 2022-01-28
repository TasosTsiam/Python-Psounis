movie_list = ["LotR", "Matrix", "Hero", "8 Mile"]
print(movie_list)
add = input("Enter your movie: ")
if add in  movie_list:
    print(" is already included, try a different one.")
else:
    movie_list.append(add)
    movie_list.sort()
    print(movie_list)
print(len(movie_list))
