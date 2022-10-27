from app import app
from flask import render_template, request, redirect, url_for 
import requests as r
from app.forms import CatchPokemonForm
from app.models import Pokemon

pokemonInfo = {}

@app.route('/', methods=["GET", "POST"])
def SearchPokemon():
    form = CatchPokemonForm()
    if request.method == "POST":
        print('POST')
        if form.validate():
            print('Validate')
            pokemon = form.pokemon.data
                        
            poke_data = {}
            response = r.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
            if response.ok:
                data = response.json()
                poke_data = data
                for entry in poke_data:
                    id = poke_data['id']
                    pokemonInfo['id'] = id                     
                    name = poke_data['name'].title()
                    pokemonInfo['name'] = name 
                    ability = poke_data['abilities'][0]['ability']['name'].title()
                    pokemonInfo['ability'] = ability 
                    ability2 = poke_data['abilities'][1]['ability']['name'].title()
                    pokemonInfo['ability2'] = ability2 
                    base_exp = poke_data['base_experience']
                    pokemonInfo['base_exp'] = base_exp 
                    front_shiny = poke_data['sprites']['other']['official-artwork']['front_default']
                    pokemonInfo['front_shiny'] = front_shiny
                    attack_stat = poke_data['stats'][1]['base_stat']
                    pokemonInfo['attack_stat'] = attack_stat
                    hp_stat = poke_data['stats'][0]['base_stat']
                    pokemonInfo['hp_stat'] = hp_stat
                    defense_stat = poke_data['stats'][2]['base_stat']
                    pokemonInfo['defense_stat'] = defense_stat

                    post = Pokemon.query.filter_by(pokemon=name).first()
                    if post:
                        return redirect(url_for('pokemonCard')) 

                    post = Pokemon(name, ability, hp_stat, attack_stat, defense_stat, base_exp, front_shiny, id)

                    post.saveToDB()

                    return redirect(url_for('pokemonCard'))                
            return f"Please check your spelling, as '{pokemon}' is not found in the Pokedex."


    return render_template('index.html', form=form)

@app.route('/PokemonField')
def pokemonCard():
    return render_template('poke_field.html', pokemonInfo=pokemonInfo)
