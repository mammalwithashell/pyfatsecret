from fatsecret import Fatsecret

# Be sure to add your own keys
consumer_key = None
consumer_secret = None


fs = Fatsecret(consumer_key, consumer_secret)

# Test Calls w/o authentication

print("\n\n ---- No Authentication Required ---- \n\n")

foods = fs.foods_search("Tacos")
print(f"Food Search Results: {len(foods)}")
print(f"{foods}\n")

food = fs.food_get("1345")
print("Food Item 1345")
print(f"{food}\n")

recipes = fs.recipes_search("Tomato Soup")
print("Recipe Search Results:")
print(f"{recipes}\n")

recipe = fs.recipe_get("88339")
print("Recipe 88339")
print(f"{recipe}\n")

# Test Calls with 3 Legged Oauth

print("\n\n ------ OAuth Example ------ \n\n")

print(fs.get_authorize_url())
session_token = fs.authenticate(input("\nPIN: "))

foods = fs.foods_get_most_eaten()
print(f"Most Eaten Food Results: {len(foods)}")

recipes = fs.recipes_search("Enchiladas")
print(f"Recipe Search Results: {len(recipes)}")

profile = fs.profile_get()
print(f"Profile: {profile}")
