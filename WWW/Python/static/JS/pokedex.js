const poke_containter=document.getElementById('poke_container');
const pokemon_number=450;
const colors={
    fire:'#FDDFDF',
    grass:'#defde0',
    electric:'#fcf7de',
    water:'#def3fd',
    ground:'#f4e7da',
    rock:'#d5d5d4',
    fairy:'#fceaff',
    poison:'#98d7a5',
    bug:'#f8d5a3',
    dragon:'#97b3e6',
    psychic:'#eaeda1',
    flying:'#F5F5F5',
    fighting:'#E6E0D4',
    normal:'#F5F5F5'

};
const main_types=Object.keys(colors);
console.log(main_types);



const fetchPokemons=async ()=>{
    for(i=1;i<=pokemon_number;i++){
        await getPokemon(i);
        console.log(i);
    }
}


const getPokemon= async id=>{
    const url=`https://pokeapi.co/api/v2/pokemon/${id}`;
    console.log(url);
    const res=await fetch(url);
    const pokemon=await res.json();
    console.log(pokemon);
    createPokemonCard(pokemon);

}

function createPokemonCard(pokemon){
    const pokemonEl=document.createElement('div');
    pokemonEl.classList.add('pokemon');
    const name=pokemon.name[0].toUpperCase()+pokemon.name.slice(1);
    const poke_types=pokemon.types.map(el=>el.type.name);
    const type=main_types.find(type=>poke_types.indexOf(type)>-1);

    var img_id=1;
    if(pokemon.id<=9){
        img_id='00'+pokemon.id;
    }else if(pokemon.id<=99){
        img_id='0'+pokemon.id;
    }else img_id=pokemon.id;
    const color=colors[type];
    pokemonEl.style.backgroundColor=color;
    const hp=pokemon.stats[0].base_stat;
    const attack=pokemon.stats[1].base_stat;
    const defense=pokemon.stats[2].base_stat;
    const special_attack=pokemon.stats[3].base_stat;
    const special_defense=pokemon.stats[4].base_stat;
    const speed=pokemon.stats[5].base_stat;


    const pokeInnerHTML=`
<div class="the_card">
<div class="front_side">


<div class="img-container"><img src="https://assets.pokemon.com/assets/cms2/img/pokedex/full/${img_id}.png"></div>
<div class="info">
<span class="number">#${pokemon.id.toString().padStart(3,'0')}</span>
<h3 class="name">${name}</h3>
<small class="type">Type:<span>${type}</span></small>

</div>

</div>

<div class="back_side">
<div class="stat">
<span class="hp">HP:${hp}

<!--<div class="bar_background">-->
<!--    <div class="bar_front"></div></div>-->
    
    </span><br>
<span class="attack">Attack:${attack}</span><br>
<span class="defense">Defense:${defense}</span><br>
<span class="special-attack">Sp-Atk:${special_attack}</span><br>
<span class="special-defense">Sp-Def:${special_defense}</span><br>
<span class="speed">Speed:${speed}</span><br>

</div>
</div>

</div>
`;

    pokemonEl.innerHTML=pokeInnerHTML;
    console.log(pokemonEl);
    poke_containter.appendChild(pokemonEl);

}

// getPokemon(1); just for testing, then move on.

fetchPokemons();



