const Ratatouille = require('@captainsafia/ratatouille');
const fs = require('fs');

const url = process.argv[2];
const recipe = new Ratatouille.default(url);

const data = {
  name: recipe.name,
  readyInTime: recipe.readyInTime,
  cookTime: recipe.cookTime,
  calories: recipe.calories,
  servings: recipe.servings,
  prepTime: recipe.prepTime,
  ingredients: recipe.ingredients,
  steps: recipe.steps,
};

fs.writeFileSync('recipe.json', JSON.stringify(data));
