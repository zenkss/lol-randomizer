import json
import os
import random
def random_champ_and_abilities():
    
    maxing_order = ""
    
    #save info from json to a variable
    with open(os.path.join(os.path.dirname(__file__),"stored_info/champions.json"), "r") as f:
        champions = json.load(f)
    
    
    #random champion, save champion id to use it for the abilities names and later pictures
    champ_id = random.randint(1, len(champions))
    print(champions[champ_id]["name"])
    
    #shuffle 0,1 and 2 to get our random order to max our abilities
    abilities_order = [0,1,2]
    random.shuffle(abilities_order)
    
    
    #printing out keys of the randomized abilties order, if statement to not add -> after the last one
    for i in range(3):
        current_ability = abilities_order[0]
        abilities_order.remove(current_ability)
        if i!=2:
            maxing_order += champions[champ_id]["abilities"][current_ability]["key"]+"->"
            continue
        maxing_order += champions[champ_id]["abilities"][current_ability]["key"]
    
    print(maxing_order)
    
    
    

        