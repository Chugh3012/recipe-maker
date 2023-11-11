from backend.app.services.recipe_service import generate_recipe
from flask import Blueprint, request

api_bp = Blueprint('api', __name__)

@api_bp.route('/health', methods=['GET'])
def health():
    return {"status": "Healthy"}, 200


@api_bp.route('/generate_recipe', methods=['POST'])
def get_recipe():
    data = request.get_json()
    ingredients = data['ingredients']
    recipe = generate_recipe(ingredients)
    return {"recipe": recipe}, 200