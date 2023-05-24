import customtkinter as ctk
from category_file_handler import process_category
import os


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Albion Helper")

        # Получение размеров экрана
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Вычисление размеров окна
        window_width = int(screen_width * 0.9)
        window_height = int(screen_height * 0.9)

        # Вычисление координат для центрирования окна
        x = int((screen_width - window_width) / 2)
        y = int((screen_height - window_height) / 2)

        # Установка размеров и позиции окна
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.sidemenu = ctk.CTkFrame(self, border_width=1)
        self.sidemenu.grid(row=0, column=0, sticky="nsew")

        self.body = ctk.CTkScrollableFrame(self, border_width=1)
        self.body.grid(row=0, column=2, sticky="nsew")
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)

        self.market = ctk.CTkLabel(self.sidemenu, text="Albion Market", font=("Arial", 20,), text_color="#FEE75C")
        self.market.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.marketbutton = ctk.CTkButton(self.sidemenu, text='Market Scanner', command=self.toggle_sidemenu, fg_color='darkgreen', bg_color='darkgreen')
        self.marketbutton.configure(hover_color='#57F287', text_color='white')
        self.marketbutton.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")

        self.grid_rowconfigure(0, weight=1)

        self.menu = None

    def toggle_sidemenu(self):
        if self.menu is None:
            self.create_sidemenu()
        else:
            self.destroy_sidemenu()

    def create_sidemenu(self):
        self.menu = ctk.CTkFrame(self)
        self.menu.grid(row=0, column=1, sticky="nsew")
        self.menu.grid_columnconfigure(0, weight=1)

        self.settings = ctk.CTkLabel(self.menu, text="Settings:",text_color="light blue", font=("Arial", 20,))
        self.settings.grid(row=0, column=0, sticky="nsew")

        self.server = ctk.CTkLabel(self.menu, text="Server")
        self.server.grid(row=2, column=0, padx=10, pady=1, sticky="nsew")

        self.server_cmb = ctk.CTkComboBox(self.menu, values=["east", "west"], state="readonly")
        self.server_cmb.set("east")
        self.server_cmb.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

        self.premium = ctk.CTkLabel(self.menu, text="Premium")
        self.premium.grid(row=4, column=0, padx=10, pady=1, sticky="nsew")

        self.premium_cmb = ctk.CTkComboBox(self.menu, values=["Non - Premium", "Premium"], state="readonly")
        self.premium_cmb.set("Non - Premium")
        self.premium_cmb.grid(row=5, column=0, padx=5, pady=10, sticky="nsew")

        self.city = ctk.CTkLabel(self.menu, text="Buy city")
        self.city.grid(row=6, column=0, padx=10, pady=1, sticky="nsew")

        self.city_cmb = ctk.CTkComboBox(self.menu, state="readonly", values=["Thetford", "Martlock", "Fort Sterling", "Caerleon", "Bridgewatch", "Lymhurst"])
        self.city_cmb.set("Thetford")
        self.city_cmb.grid(row=7, column=0, padx=5, pady=10, sticky="nsew")

        self.category = ctk.CTkLabel(self.menu, text="Category")
        self.category.grid(row=8, column=0, padx=10, pady=1)

        self.category_cmb = ctk.CTkComboBox(self.menu, state="readonly", values=["Animal Skinner Tomes",
                                                                                 "Any",
                                                                                 "Arcane Staff",
                                                                                 "Arena Sigil",
                                                                                 "Armored Horse",
                                                                                 "Artifact Armor",
                                                                                 "Artifact Magic",
                                                                                 "Bag",
                                                                                 "Battle Mount",
                                                                                 "Bridgewatch",
                                                                                 "Caerleon",
                                                                                 "Cape",
                                                                                 "City Resource",
                                                                                 "Cloth Armor",
                                                                                 "Cloth Helmet",
                                                                                 "Cloth Shoes",
                                                                                 "Consumable Cooked",
                                                                                 "Consumable Fish",
                                                                                 "Consumable Fishing Bait",
                                                                                 "Consumable Map",
                                                                                 "Consumable Potion",
                                                                                 "Consumable Vanity",
                                                                                 "Consumable Victory Emotes",
                                                                                 "Crossbow",
                                                                                 "Cursed Staff",
                                                                                 "Demolition Hammer",
                                                                                 "Direbear",
                                                                                 "Direboar",
                                                                                 "Direwolf",
                                                                                 "Event",
                                                                                 "Farmable Animal",
                                                                                 "Farmable Seed",
                                                                                 "Farming Journals",
                                                                                 "Fiber Harvester Tomes",
                                                                                 "Fiber Trophy",
                                                                                 "Fire Staff",
                                                                                 "Fisherman Backpack",
                                                                                 "Fisherman Boots",
                                                                                 "Fisherman Cape",
                                                                                 "Fisherman Garb",
                                                                                 "Fishing Rod",
                                                                                 "Fishing Trophy",
                                                                                 "Fort Sterling",
                                                                                 "Frost Staff",
                                                                                 "Furniture Banner",
                                                                                 "Furniture Bed",
                                                                                 "Furniture Chest",
                                                                                 "Furniture Decoration",
                                                                                 "Furniture Flag",
                                                                                 "Furniture Heretic",
                                                                                 "Furniture Keeper",
                                                                                 "Furniture Morgana",
                                                                                 "Furniture Repair Kit",
                                                                                 "Furniture Table",
                                                                                 "Furniture Unique",
                                                                                 "General Trophy",
                                                                                 "Harvester Backpack",
                                                                                 "Harvester Cap",
                                                                                 "Harvester Garb",
                                                                                 "Harvester Workboots",
                                                                                 "Hide Trophy",
                                                                                 "Holy Staff",
                                                                                 "Leather Armor",
                                                                                 "Leather Helmet",
                                                                                 "Leather Shoes",
                                                                                 "Lumberjack Backpack",
                                                                                 "Lumberjack Cap",
                                                                                 "Lumberjack Garb",
                                                                                 "Lumberjack Tomes",
                                                                                 "Lumberjack Workboots",
                                                                                 "Lymhurst",
                                                                                 "Map",
                                                                                 "Martlock",
                                                                                 "Material Essence",
                                                                                 "Material Other",
                                                                                 "Material Relic",
                                                                                 "Material Rune",
                                                                                 "Material Soul",
                                                                                 "Melee Artefact",
                                                                                 "Melee Axe",
                                                                                 "Melee Dagger",
                                                                                 "Melee Hammer",
                                                                                 "Melee Mace",
                                                                                 "Melee Quarterstaff",
                                                                                 "Melee Spear",
                                                                                 "Melee Sword",
                                                                                 "Melee War Glowes",
                                                                                 "Mercenary Trophy",
                                                                                 "Miner Backpack",
                                                                                 "Miner Cap",
                                                                                 "Miner Garb",
                                                                                 "Miner Workboots",
                                                                                 "Mule",
                                                                                 "Nature Staff",
                                                                                 "Offhand Artifact",
                                                                                 "Off-Hand Book",
                                                                                 "Off-Hand Horn",
                                                                                 "Off-Hand Orb",
                                                                                 "Off-Hand Shield",
                                                                                 "Off-Hand Torch",
                                                                                 "Off-Hand Totem",
                                                                                 "Ore Miner Tomes",
                                                                                 "Ore Trophy",
                                                                                 "Other Artifact",
                                                                                 "Ox",
                                                                                 "Pickaxe",
                                                                                 "Plate Armor",
                                                                                 "Plate Helmet",
                                                                                 "Plate Shoes",
                                                                                 "Product Animal",
                                                                                 "Product Cooked",
                                                                                 "Product Farming",
                                                                                 "Quarrier Backpack",
                                                                                 "Quarrier Cap",
                                                                                 "Quarrier Garb",
                                                                                 "Quarrier Tomes",
                                                                                 "Quarrier Workboots",
                                                                                 "Ranged Artifact",
                                                                                 "Ranged Bow",
                                                                                 "Rare Mount",
                                                                                 "Resource Cloth",
                                                                                 "Resource Fiber",
                                                                                 "Resource Hide",
                                                                                 "Resource Leather",
                                                                                 "Resource Metalbar",
                                                                                 "Resource Ore",
                                                                                 "Resource Other",
                                                                                 "Resource Planks",
                                                                                 "Resource Stone Block",
                                                                                 "Resource Stone",
                                                                                 "Resource Wood",
                                                                                 "Riding Horse",
                                                                                 "Royal Sigils",
                                                                                 "Sickle",
                                                                                 "Skinner Garb",
                                                                                 "Skinner Backpack",
                                                                                 "Skinner Cap",
                                                                                 "Skinner Workboots",
                                                                                 "Skinning Knife",
                                                                                 "Stag and Mose",
                                                                                 "Stone Hammer",
                                                                                 "Stone Trophy",
                                                                                 "Swamp Dragon",
                                                                                 "Swiftclaw",
                                                                                 "Thetford",
                                                                                 "Tome Of Insight",
                                                                                 "Wood Axe",
                                                                                 "Wood Trophy"])
        self.category_cmb.set("Bag")
        self.category_cmb.grid(row=9, column=0, padx=5, pady=10, sticky="nsew")

        self.itemlang = ctk.CTkLabel(self.menu, text="Item language")
        self.itemlang.grid(row=10, column=0, padx=10, pady=1)

        self.itemlang_cmb = ctk.CTkComboBox(self.menu, state="readonly", values=["English", "Russian", "German", "French", "Italian", "Spanish", "Portuguese",])
        self.itemlang_cmb.set("English")
        self.itemlang_cmb.grid(row=11, column=0, padx=5, pady=10, sticky="nsew")

        self.search_btn = ctk.CTkButton(self.menu, text="Search", command=self.save_settings)
        self.search_btn.grid(row=12, column=0, padx=10, pady=10, sticky="nsew")

    def save_settings(self):
        category_value = self.category_cmb.get()
        category_data = process_category(category_value)
        if category_data:
            print("Содержимое категории:", category_data)
    def destroy_sidemenu(self):
        self.menu.grid_forget()
        self.menu.destroy()
        self.menu = None

app = App()
app.mainloop()
