"""Restaurant rating lister."""


# put your code here

the_file = open("scores.txt")

scores = {}
for line in the_file:
    restaurant, score = line.strip().split(":")
    scores[restaurant] = score

the_file.close()

def get_user_restaurant(scores):

    print("Please enter your favorite restaurant and a rating!")    
    restaurant = input("Restaurant Name: ")
    rating = input("Rating: ")

    scores[restaurant.capitalize()] = rating

    for restaurant_temp, rating_temp in sorted(scores.items()):
        print(f"{restaurant_temp} is rated at {rating_temp}")


get_user_restaurant(scores)