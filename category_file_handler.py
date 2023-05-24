import os

def process_category(category):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = None
        if category == "Animal Skinner Tomes":
            file_path = os.path.join(current_dir,"category", "animal skinner tomes.txt")
        elif category == "Any":
             file_path = os.path.join(current_dir,"category", "any.txt")
        elif category == "Arcane Staff":
             file_path = os.path.join(current_dir,"category", "arcane staff.txt")
        elif category == "Arena Sigil":
            file_path = os.path.join(current_dir,"category", "arena sigil.txt")
        elif category == "Armored Horse":
            file_path = os.path.join(current_dir,"category", "armored horse.txt")
        elif category == "Artifact Armor":
            file_path = os.path.join(current_dir,"category", "artifact armor.txt")
        elif category == "Artifact Magic":
            file_path = os.path.join(current_dir,"category", "artifact magic.txt")
        elif category == "Bag":
            file_path = os.path.join(current_dir,"category", "bag.txt")
        elif category == "Battle Mount":
            file_path = os.path.join(current_dir,"category", "battle mount.txt")
        elif category == "Bridgewatch":
            file_path = os.path.join(current_dir,"category", "bridgewatch.txt")
        elif category == "Caerleon":
            file_path = os.path.join(current_dir,"category", "caerleon.txt")
        elif category == "Cape":
            file_path = os.path.join(current_dir,"category", "cape.txt")
        elif category == "City Resource":
            file_path = os.path.join(current_dir,"category", "city resource.txt")
        elif category == "Cloth Armor":
            file_path = os.path.join(current_dir,"category", "cloth armor.txt")
        elif category == "Cloth Helmet":
            file_path = os.path.join(current_dir,"category", "cloth helmet.txt")
        elif category == "Cloth Shoes":
            file_path = os.path.join(current_dir,"category", "cloth shoes.txt")
        elif category == "Consumable Cooked":
            file_path = os.path.join(current_dir,"category", "consumable cooked.txt")
        elif category == "Consumable Fish":
            file_path = os.path.join(current_dir,"category", "consumable fish.txt")
        elif category == "Consumable Fishing Bait":
            file_path = os.path.join(current_dir,"category", "consumable fishing bait.txt")
        elif category == "Consumable Map":
            file_path = os.path.join(current_dir,"category", "consumable map.txt")
        elif category == "Consumable Potion":
            file_path = os.path.join(current_dir,"category", "consumable potion.txt")
        elif category == "Consumable Vanity":
            file_path = os.path.join(current_dir,"category", "consumable vanity.txt")
        elif category == "Consumable Victory Emotes":
            file_path = os.path.join(current_dir,"category", "consumable victory emotes.txt")
        elif category == "Crossbow":
            file_path= os.path.join(current_dir,"category", "crossbow.txt")
        elif category == "Cursed Staff":
            file_path = os.path.join(current_dir,"category", "cursed staff.txt")
        elif category == "Demolition Hammer":
            file_path = os.path.join(current_dir,"category", "demolition hammer.txt")
        elif category == "Direbear":
            file_path = os.path.join(current_dir,"category", "direbear.txt")
        elif category == "Direboar":
            file_path = os.path.join(current_dir,"category", "direboar.txt")
        elif category == "Direwolf":
            file_path = os.path.join(current_dir,"category", "direwolf.txt")
        elif category == "Event":
            file_path = os.path.join(current_dir,"category", "event.txt")
        elif category == "Farmable Animal":
            file_path = os.path.join(current_dir,"category", "farmable animal.txt")
        elif category == "Farmable Seed":
            file_path = os.path.join(current_dir,"category", "farmable seed.txt")
        elif category == "Farming Journals":
            file_path = os.path.join(current_dir,"category", "farming journals.txt")
        elif category == "Fiber Harvester Tomes":
            file_path = os.path.join(current_dir,"category", "fiber harvester tomes.txt")
        elif category == "Fiber Trophy":
            file_path = os.path.join(current_dir,"category", "fiber trophy.txt")
        elif category == "Fire Staff":
            file_path = os.path.join(current_dir,"category", "fire staff.txt")
        elif category == "Fisherman Backpack":
            file_path = os.path.join(current_dir,"category", "fisherman backpack.txt")
        elif category == "Fisherman Boots":
            file_path = os.path.join(current_dir,"category", "fisherman boots.txt")
        elif category == "Fisherman Cape":
            file_path = os.path.join(current_dir,"category", "fisherman cape.txt")
        elif category == "Fisherman Garb":
            file_path = os.path.join(current_dir,"category", "fisherman garb.txt")
        elif category == "Fishing Rod":
            file_path = os.path.join(current_dir, "category", "fishing rod.txt")
        elif category == "Fishing Trophy":
            file_path = os.path.join(current_dir, "category", "fishing trophy.txt")
        elif category == "Fort Sterling":
            file_path = os.path.join(current_dir, "category", "fort sterling.txt")
        elif category == "Frost Staff":
            file_path = os.path.join(current_dir, "category", "frost staff.txt")
        elif category == "Furniture Banner":
            file_path = os.path.join(current_dir, "category", "furniture banner.txt")
        elif category == "Furniture Bed":
            file_path = os.path.join(current_dir, "category", "furniture bed.txt")
        elif category == "Furniture Chest":
            file_path = os.path.join(current_dir, "category", "furniture chest.txt")
        elif category == "Furniture Decoration":
            file_path = os.path.join(current_dir, "category", "furniture decoration.txt")
        elif category == "Furniture Flag":
            file_path = os.path.join(current_dir, "category", "furniture flag.txt")
        elif category == "Furniture Heretic":
            file_path = os.path.join(current_dir, "category", "furniture heretic.txt")
        elif category == "Furniture Keeper":
            file_path = os.path.join(current_dir, "category", "furniture keeper.txt")
        elif category == "Furniture Morgana":
            file_path = os.path.join(current_dir, "category", "furniture morgana.txt")
        elif category == "Furniture Repair Kit":
            file_path = os.path.join(current_dir, "category", "furniture repair kit.txt")
        elif category == "Furniture Table":
            file_path = os.path.join(current_dir, "category", "furniture table.txt")
        elif category == "Furniture Unique":
            file_path = os.path.join(current_dir, "category", "furniture unique.txt")
        elif category == "General Trophy":
            file_path = os.path.join(current_dir, "category", "general trophy.txt")
        elif category == "Harvester Backpack":
            file_path = os.path.join(current_dir, "category", "harvester backpack.txt")
        elif category == "Harvester Cap":
            file_path = os.path.join(current_dir, "category", "harvester cap.txt")
        elif category == "Harvester Garb":
            file_path = os.path.join(current_dir, "category", "harvester garb.txt")
        elif category == "Harvester Workboots":
            file_path = os.path.join(current_dir, "category", "harvester workboots.txt")
        elif category == "Hide Trophy":
            file_path = os.path.join(current_dir, "category", "hide trophy.txt")
        elif category == "Holy Staff":
            file_path = os.path.join(current_dir, "category", "holy staff.txt")
        elif category == "Leather Armor":
            file_path = os.path.join(current_dir, "category", "leather armor.txt")
        elif category == "Leather Helmet":
            file_path = os.path.join(current_dir, "category", "leather helmet.txt")
        elif category == "Leather Shoes":
            file_path = os.path.join(current_dir, "category", "leather shoes.txt")
        elif category == "Lumberjack Backpack":
            file_path = os.path.join(current_dir, "category", "lumberjack backpack.txt")
        elif category == "Lumberjack Cap":
            file_path = os.path.join(current_dir, "category", "lumberjack cap.txt")
        elif category == "Lumberjack Garb":
            file_path = os.path.join(current_dir, "category", "lumberjack garb.txt")
        elif category == "Lumberjack Tomes":
            file_path = os.path.join(current_dir, "category", "lumberjack tomes.txt")
        elif category == "Lumberjack Workboots":
            file_path = os.path.join(current_dir, "category", "lumberjack workboots.txt")
        elif category == "Lymhurst":
            file_path = os.path.join(current_dir, "category", "lymhurst.txt")
        elif category == "Map":
            file_path = os.path.join(current_dir, "category", "map.txt")
        elif category == "Martlock":
            file_path = os.path.join(current_dir, "category", "martlock.txt")
        elif category == "Material Essence":
            file_path = os.path.join(current_dir, "category", "material essence.txt")
        elif category == "Material Other":
            file_path = os.path.join(current_dir, "category", "material other.txt")
        elif category == "Material Relic":
            file_path = os.path.join(current_dir, "category", "material relic.txt")
        elif category == "Material Rune":
            file_path = os.path.join(current_dir, "category", "material rune.txt")
        elif category == "Material Soul":
            file_path = os.path.join(current_dir, "category", "material soul.txt")
        elif category == "Melee Artefact":
            file_path = os.path.join(current_dir, "category", "melee artefact.txt")
        elif category == "Melee Axe":
            file_path = os.path.join(current_dir, "category", "melee axe.txt")
        elif category == "Melee Dagger":
            file_path = os.path.join(current_dir, "category", "melee dagger.txt")
        elif category == "Melee Hammer":
            file_path = os.path.join(current_dir, "category", "melee hammer.txt")
        elif category == "Melee Mace":
            file_path = os.path.join(current_dir, "category", "melee mace.txt")
        elif category == "Melee Quarterstaff":
            file_path = os.path.join(current_dir, "category", "melee quarterstaff.txt")
        elif category == "Melee Spear":
            file_path = os.path.join(current_dir, "category", "melee spear.txt")
        elif category == "Melee Sword":
            file_path = os.path.join(current_dir, "category", "melee sword.txt")
        elif category == "Melee War Glowes":
            file_path = os.path.join(current_dir, "category", "melee war glowes.txt")
        elif category == "Mercenary Trophy":
            file_path = os.path.join(current_dir, "category", "mercenary trophy.txt")
        elif category == "Miner Backpack":
            file_path = os.path.join(current_dir, "category", "miner backpack.txt")
        elif category == "Miner Cap":
            file_path = os.path.join(current_dir, "category", "miner cap.txt")
        elif category == "Miner Garb":
            file_path = os.path.join(current_dir, "category", "miner garb.txt")
        elif category == "Miner Workboots":
            file_path = os.path.join(current_dir, "category", "miner workboots.txt")
        elif category == "Mule":
            file_path = os.path.join(current_dir, "category", "mule.txt")
        elif category == "Nature Staff":
            file_path = os.path.join(current_dir, "category", "nature staff.txt")
        elif category == "Offhand Artifact":
            file_path = os.path.join(current_dir, "category", "offhand artifact.txt")
        elif category == "Off-Hand Book":
            file_path = os.path.join(current_dir, "category", "off hand book.txt")
        elif category == "Off-Hand Horn":
            file_path = os.path.join(current_dir, "category", "off hand Horn.txt")
        elif category == "Off-Hand Orb":
            file_path = os.path.join(current_dir, "category", "off  hand Horn.txt")
        elif category == "Off-Hand Shield":
            file_path = os.path.join(current_dir, "category", "off hand shield.txt")
        elif category == "Off-Hand Torch":
            file_path = os.path.join(current_dir, "category", "off hand torch.txt")
        elif category == "Off-Hand Totem":
            file_path = os.path.join(current_dir, "category", "off hand totem.txt")
        elif category == "Ore Miner Tomes":
            file_path = os.path.join(current_dir, "category", "ore miner tomes.txt")
        elif category == "Ore Trophy":
            file_path = os.path.join(current_dir, "category", "ore trophy.txt")
        elif category == "Other Artifact":
            file_path = os.path.join(current_dir, "category", "other artifact.txt")
        elif category == "Ox":
            file_path = os.path.join(current_dir, "category", "ox.txt")
        elif category == "Pickaxe":
            file_path = os.path.join(current_dir, "category", "pickaxe.txt")
        elif category == "Plate Armor":
            file_path = os.path.join(current_dir, "category", "plate armor.txt")
        elif category == "Plate Helmet":
            file_path = os.path.join(current_dir, "category", "plate helmet.txt")
        elif category == "Plate Shoes":
            file_path = os.path.join(current_dir, "category", "plate shoes.txt")
        elif category == "Product Animal":
            file_path = os.path.join(current_dir, "category", "product animal.txt")
        elif category == "Product Cooked":
            file_path = os.path.join(current_dir, "category", "product cooked.txt")
        elif category == "Product Farming":
            file_path = os.path.join(current_dir, "category", "product farming.txt")
        elif category == "Quarrier Backpack":
            file_path = os.path.join(current_dir, "category", "quarrier backpack.txt")
        elif category == "Quarrier Cap":
            file_path = os.path.join(current_dir, "category", "quarrier cap.txt")
        elif category == "Quarrier Garb":
            file_path = os.path.join(current_dir, "category", "quarrier garb.txt")
        elif category == "Quarrier Tomes":
            file_path = os.path.join(current_dir, "category", "quarrier tomes.txt")
        elif category == "Quarrier Workboots":
            file_path = os.path.join(current_dir, "category", "quarrier workboots.txt")
        elif category == "Ranged Artifact":
            file_path = os.path.join(current_dir, "category", "ranged artifact.txt")
        elif category == "Ranged Bow":
            file_path = os.path.join(current_dir, "category", "ranged bow.txt")
        elif category == "Rare Mount":
            file_path = os.path.join(current_dir, "category", "rare mount.txt")
        elif category == "Resource Cloth":
            file_path = os.path.join(current_dir, "category", "resource cloth.txt")
        elif category == "Resource Fiber":
            file_path = os.path.join(current_dir, "category", "resource fiber.txt")
        elif category == "Resource Hide":
            file_path = os.path.join(current_dir, "category", "resource hide.txt")
        elif category == "Resource Leather":
            file_path = os.path.join(current_dir, "category", "resource leather.txt")
        elif category == "Resource Metalbar":
            file_path = os.path.join(current_dir, "category", "resource metalbar.txt")
        elif category == "Resource Ore":
            file_path = os.path.join(current_dir, "category", "resource ore.txt")
        elif category == "Resource Other":
            file_path = os.path.join(current_dir, "category", "resource other.txt")
        elif category == "Resource Planks":
            file_path = os.path.join(current_dir, "category", "resource planks.txt")
        elif category == "Resource Stone Block":
            file_path = os.path.join(current_dir, "category", "resource stone block.txt")
        elif category == "Resource Stone":
            file_path = os.path.join(current_dir, "category", "resource stone.txt")
        elif category == "Resource Wood":
            file_path = os.path.join(current_dir, "category", "resource wood.txt")
        elif category == "Riding Horse":
            file_path = os.path.join(current_dir, "category", "riding horse.txt")
        elif category == "Royal Sigils":
            file_path = os.path.join(current_dir, "category", "royal sigils.txt")
        elif category == "Sickle":
            file_path = os.path.join(current_dir, "category", "sickle.txt")
        elif category == "Skinner Garb":
            file_path = os.path.join(current_dir, "category", "skinner garb.txt")
        elif category == "Skinner Backpack":
            file_path = os.path.join(current_dir, "category", "skinner backpack.txt")
        elif category == "Skinner Cap":
            file_path = os.path.join(current_dir, "category", "skinner cap.txt")
        elif category == "Skinner Workboots":
            file_path = os.path.join(current_dir, "category", "skinner workboots.txt")
        elif category == "Skinning Knife":
            file_path = os.path.join(current_dir, "category", "skinning knife.txt")
        elif category == "Stag and Mose":
            file_path = os.path.join(current_dir, "category", "stag and mose.txt")
        elif category == "Stone Hammer":
            file_path = os.path.join(current_dir, "category", "stone hammer.txt")
        elif category == "Stone Trophy":
            file_path = os.path.join(current_dir, "category", "stone trophy.txt")
        elif category == "Swamp Dragon":
            file_path = os.path.join(current_dir, "category", "swamp dragon.txt")
        elif category == "Swiftclaw":
            file_path = os.path.join(current_dir, "category", "swiftclaw.txt")
        elif category == "Thetford":
            file_path = os.path.join(current_dir, "category", "thetford.txt")
        elif category == "Tome Of Insight":
            file_path = os.path.join(current_dir, "category", "tome of insight.txt")
        elif category == "Wood Axe":
            file_path = os.path.join(current_dir, "category", "wood axe.txt")
        elif category == "Wood Trophy":
            file_path = os.path.join(current_dir, "category", "wood trophy.txt")
            
        if file_path:
            with open(file_path, "r", encoding='utf-8') as file:
                data = file.read()
            return data

        return category_data