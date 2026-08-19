import json
import os
import random

def random_runes():
    
    #save info from json to a variable
    with open(os.path.join(os.path.dirname(__file__),"stored_info/runes.json"), "r") as f:
        runes = json.load(f)
        
    
    #generate main tree, keystone rune
    main_tree_id = random.randint(0,len(runes)-2)
    keystone_id = random.randint(0,len(runes[main_tree_id]["keystones"])-1)
    print(runes[main_tree_id]["Name"])
    print(runes[main_tree_id]["keystones"][keystone_id])
    
    
    #generate the 3 slots of the rune, will need to run a loop to display it with this setup
    rune_slots_ids = [0,0,0]
    for i in range(3):
        rune_slots_ids[i] = random.randint(0,2)
        print(runes[main_tree_id]["slots"][i][rune_slots_ids[i]])
    
    
    
    
    
