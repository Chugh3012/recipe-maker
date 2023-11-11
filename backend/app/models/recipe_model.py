class Recipe:
    def __init__(self, recipe_name, servings, ingredients, instructions):
        self.recipe_name = recipe_name
        self.servings = servings
        self.ingredients = ingredients
        self.instructions = instructions

    def to_dict(self):
        return {
            'recipe_name': self.recipe_name,
            'servings': self.servings,
            'ingredients': self.ingredients,
            'instructions': self.instructions
        }