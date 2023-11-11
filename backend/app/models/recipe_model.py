class Recipe:
    def __init__(self, id, name, description, ingredients, steps, image, category, user_id):
        self.id = id
        self.name = name
        self.description = description
        self.ingredients = ingredients
        self.steps = steps
        self.image = image
        self.category = category
        self.user_id = user_id