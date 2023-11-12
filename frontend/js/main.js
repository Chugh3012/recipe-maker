document.getElementById('recipe-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const ingredientsInput = document.getElementById('ingredients').value;
    
    fetch('https://super-duper-capybara-4jxg57x67r937j6v-5000.app.github.dev/api/generate_recipe', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ ingredients: ingredientsInput })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json(); // Parse the data as JSON
    })
    .then(data => {
        renderRecipe(data.response); // Render the recipe
    })
    .catch(error => {
        console.error('Error:', error); // Handle the error
    });
});

function renderRecipe(recipe) {
    const title = document.getElementById('recipe-title');
    const ingredients = document.getElementById('recipe-ingredients');
    const instructions = document.getElementById('recipe-instructions');

    title.textContent = recipe.recipe_name;
    ingredients.innerHTML = '';
    recipe.ingredients.forEach(ingredient => {
        const li = document.createElement('li');
        li.textContent = ingredient;
        ingredients.appendChild(li);
    });
    instructions.textContent = recipe.instructions.join('\n');
}