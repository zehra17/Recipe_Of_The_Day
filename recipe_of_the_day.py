import random

class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

recipes = [
    Recipe("Pasta", ["spaghetti", "tomato sauce", "cheese"], "Boil pasta, add sauce, top with cheese."),
    Recipe("Salad", ["lettuce", "tomato", "cucumber", "olive oil"], "Chop vegetables, mix, add oil."),
    Recipe("Smoothie", ["banana", "milk", "honey"], "Blend all ingredients together."),
    Recipe("Sandwich", ["bread", "cheese", "ham", "lettuce"], "Assemble ingredients between slices of bread."),
    Recipe("Pizza", ["dough", "tomato sauce", "cheese", "pepperoni"], "Roll dough, add sauce and toppings, bake."),
    Recipe("Omelette", ["eggs", "cheese", "onion", "butter"], "Whisk eggs, cook with butter, add cheese and onion."),
    Recipe("Soup", ["carrot", "potato", "onion", "broth"], "Boil vegetables in broth until soft."),
    Recipe("Burger", ["bun", "beef patty", "cheese", "lettuce"], "Grill patty, assemble with bun and toppings."),
    Recipe("Tacos", ["tortilla", "ground beef", "cheese", "lettuce", "tomato"], "Cook beef, assemble in tortilla with toppings."),
    Recipe("Pancakes", ["flour", "milk", "egg", "butter", "syrup"], "Mix ingredients, cook on griddle, serve with syrup."),
    Recipe("Spaghetti Bolognese", ["spaghetti", "ground beef", "tomato sauce", "onion", "garlic"], "Cook beef and onion, add sauce, serve over pasta."),
    Recipe("Muffins", ["flour", "sugar", "egg", "milk", "butter"], "Mix ingredients, bake in muffin tin."),
    Recipe("Quiche", ["pie crust", "eggs", "cheese", "spinach", "cream"], "Mix ingredients, pour into crust, bake."),
    Recipe("Chili", ["ground beef", "tomato", "beans", "onion", "chili powder"], "Cook beef and onion, add beans and spices, simmer."),
    Recipe("Fried Rice", ["rice", "egg", "carrot", "peas", "soy sauce"], "Fry rice with vegetables, add soy sauce."),
    Recipe("Steak", ["beef steak", "salt", "pepper", "butter"], "Season steak, cook in pan with butter."),
    Recipe("Ice Cream", ["cream", "sugar", "vanilla", "chocolate"], "Mix ingredients, freeze in ice cream maker."),
    Recipe("Cupcakes", ["flour", "sugar", "egg", "butter", "vanilla"], "Mix ingredients, bake in cupcake tin."),
    Recipe("Lasagna", ["lasagna noodles", "ground beef", "tomato sauce", "cheese", "onion"], "Layer noodles, beef, and cheese, bake."),
    Recipe("Curry", ["chicken", "curry powder", "onion", "coconut milk"], "Cook chicken with onions, add curry powder and milk, simmer."),
    Recipe("Bagel", ["flour", "yeast", "water", "salt"], "Mix dough, shape into bagels, boil, then bake."),
    Recipe("Waffles", ["flour", "sugar", "egg", "milk", "butter"], "Mix ingredients, cook in waffle iron."),
    Recipe("Ratatouille", ["eggplant", "zucchini", "tomato", "onion", "bell pepper", "olive oil"], "Chop vegetables, sauté with olive oil until tender."),
    Recipe("Fajitas", ["tortilla", "chicken", "onion", "bell pepper", "lime"], "Grill chicken, sauté vegetables, assemble in tortilla."),
    Recipe("Spring Rolls", ["rice paper", "shrimp", "lettuce", "carrot", "cucumber", "hoisin sauce"], "Fill rice paper with ingredients, roll tightly."),
    Recipe("Beef Stroganoff", ["beef", "onion", "mushrooms", "sour cream", "beef broth"], "Sauté beef and onions, add mushrooms and broth, stir in sour cream."),
    Recipe("Baked Salmon", ["salmon", "lemon", "garlic", "butter"], "Season salmon, bake with butter, garlic, and lemon."),
    Recipe("Ceviche", ["shrimp", "lime", "onion", "tomato", "cilantro"], "Marinate shrimp in lime juice, mix with chopped vegetables."),
    Recipe("Chicken Parmesan", ["chicken breast", "tomato sauce", "mozzarella", "parmesan", "bread crumbs"], "Bread and fry chicken, top with sauce and cheese, bake."),
    Recipe("Goulash", ["ground beef", "onion", "tomato paste", "paprika", "noodles"], "Cook beef with onions, add tomato paste and paprika, serve over noodles."),
    Recipe("Tiramisu", ["ladyfingers", "mascarpone cheese", "coffee", "cocoa powder", "sugar"], "Layer ladyfingers with mascarpone mixture, dust with cocoa."),
    Recipe("Paella", ["rice", "seafood", "chicken", "saffron", "bell pepper", "tomato"], "Cook rice with saffron and vegetables, add seafood and chicken."),
    Recipe("Fettuccine Alfredo", ["fettuccine", "butter", "cream", "parmesan", "garlic"], "Cook pasta, prepare sauce with butter, cream, and garlic, mix."),
    Recipe("Chicken Tenders", ["chicken breast", "flour", "egg", "bread crumbs", "oil"], "Coat chicken in flour and breadcrumbs, fry."),
    Recipe("Apple Pie", ["apples", "sugar", "butter", "flour", "cinnamon", "pie crust"], "Layer apples with sugar and cinnamon in pie crust, bake."),
    Recipe("French Toast", ["bread", "egg", "milk", "cinnamon", "butter"], "Dip bread in egg mixture, cook in buttered pan, serve with syrup."),
    Recipe("Shrimp Scampi", ["shrimp", "garlic", "butter", "lemon", "parsley"], "Sauté shrimp with garlic, butter, and lemon, serve with pasta."),
    Recipe("Vegetable Stir-Fry", ["carrot", "broccoli", "bell pepper", "soy sauce", "garlic", "tofu"], "Stir-fry vegetables and tofu with garlic and soy sauce."),
    Recipe("Chicken Soup", ["chicken", "carrot", "celery", "onion", "broth"], "Boil chicken and vegetables in broth until tender."),
    Recipe("Churros", ["flour", "sugar", "cinnamon", "butter", "egg"], "Mix dough, fry, coat in sugar and cinnamon."),
    Recipe("Cheesecake", ["cream cheese", "sugar", "eggs", "vanilla", "graham cracker crust"], "Mix filling, pour into crust, bake."),
    Recipe("Gnocchi", ["potato", "flour", "egg", "parmesan", "butter"], "Mix ingredients, form dumplings, boil and sauté in butter."),
    Recipe("Falafel", ["chickpeas", "garlic", "onion", "parsley", "flour", "spices"], "Form mixture into balls, fry."),
    Recipe("Bruschetta", ["bread", "tomato", "garlic", "basil", "olive oil"], "Toast bread, top with tomato, garlic, basil, and oil."),
    Recipe("Beef Wellington", ["beef tenderloin", "puff pastry", "mushrooms", "prosciutto", "egg"], "Wrap beef in mushrooms and prosciutto, encase in pastry, bake."),
    Recipe("Sushi", ["sushi rice", "nori", "fish", "soy sauce", "wasabi"], "Prepare rice, roll with fish and nori, serve with soy sauce and wasabi."),
    Recipe("Chicken Fried Rice", ["rice", "chicken", "egg", "carrot", "peas", "soy sauce"], "Fry rice with chicken, vegetables, and egg, add soy sauce."),
    Recipe("Pavlova", ["egg whites", "sugar", "cornstarch", "vanilla", "fruit"], "Whisk egg whites with sugar, bake meringue, top with fruit."),
    Recipe("Moussaka", ["eggplant", "ground beef", "tomato", "bechamel sauce", "cheese"], "Layer eggplant, beef, and sauce, bake."),
    Recipe("Minestrone Soup", ["carrot", "celery", "tomato", "beans", "pasta", "onion", "broth"], "Cook vegetables in broth, add beans and pasta, simmer."),
    Recipe("Shakshuka", ["eggs", "tomato", "onion", "garlic", "spices"], "Simmer tomato sauce with spices, crack eggs in, cook until set."),
    Recipe("Frittata", ["eggs", "potato", "cheese", "onion", "spinach"], "Cook potato and onion, pour over whisked eggs, bake."),
    Recipe("Baklava", ["phyllo dough", "nuts", "butter", "sugar", "honey"], "Layer dough with nuts, bake, drizzle with honey."),
]

def get_random_recipe():
    recipe = random.choice(recipes)
    print(f"Recipe: {recipe.name}")
    print("Ingredients:", ', '.join(recipe.ingredients))
    print("Instructions:", recipe.instructions)

get_random_recipe()
