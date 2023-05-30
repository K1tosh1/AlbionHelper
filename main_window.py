import customtkinter
from CTkMessagebox import CTkMessagebox
import requests
from PIL import Image, ImageTk
import json
import concurrent.futures
import threading
import webbrowser

class Loader(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Albion Helper")
        self.resizable(False, False)
        customtkinter.set_appearance_mode("dark")
        self.overrideredirect(True)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        window_width = 300
        window_height = 120

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        AppName = customtkinter.CTkLabel(self, text="Albion Helper")
        AppName.grid(row=0, column=0, padx=10, pady=10)
        AppName.configure(font=("Arial", 20))

        loading = customtkinter.CTkLabel(self, text="Загрузка...")
        loading.grid(row=2, column=0, padx=10, pady=10)

        progressbar = customtkinter.CTkProgressBar(self, orientation="horizontal", mode='indeterminate')
        progressbar.grid(row=1, column=0, pady=5, padx=5, sticky="nsew")

        self.grid_columnconfigure(0, weight=1)

        progressbar.start()

        self.after(4500, self.show_albion_helper)

    def show_albion_helper(self):
        self.destroy()
        Albion_Helper()

class Albion_Helper(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("dark")
        self.title("Albion Helper")
        self.selected_server = None
        self.selected_category = None
        self.selected_premium = None
        self.url = None

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        window_width = int(screen_width * 0.9)
        window_height = int(screen_height * 0.9)

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        sidebar_width = 380
        sidebar = customtkinter.CTkFrame(self, width=sidebar_width)
        sidebar.grid(row=0, column=0, sticky="ns")

        label_category = customtkinter.CTkLabel(sidebar, text="Категория")
        label_category.grid(row=0, column=0)
        category = customtkinter.CTkComboBox(sidebar, values=['Аксессуары','Тканевая броня'], state = 'readonly',command=self.get_category)
        category.set(value="Выбери категорию")
        category.grid(row=2, column=0, pady=5,padx=5, sticky="nsew")

        label_server = customtkinter.CTkLabel(sidebar, text="Сервер")
        label_server.grid(row=3, column=0)
        server = customtkinter.CTkComboBox(sidebar, values=['Западный','Восточный'], state = 'readonly', command=self.get_server)
        server.set(value="Выбери сервер")
        server.grid(row=4, column=0, pady=5, padx=5,sticky="nsew")

        label_premium = customtkinter.CTkLabel(sidebar, text="Премиум")
        label_premium.grid(row=5, column=0)
        premium = customtkinter.CTkComboBox(sidebar, values=['Да','Нет'], state = 'readonly', command=self.get_premium)
        premium.set(value="Премиум")
        premium.grid(row=6, column=0, pady=5, padx=5,sticky="nsew")

        btn_search = customtkinter.CTkButton(sidebar, text="Поиск", command=self.search_in_background)
        btn_search.grid(row=7, column=0, padx=15, pady=15, sticky='nsew')

        self.content = customtkinter.CTkScrollableFrame(self, border_width=1, border_color='#FEFDCA')
        self.content.grid(row=0, column=1, padx=15, pady=15, sticky="nsew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.check_version()

    def check_version(self):
        current_version = '1.0'
        url = "https://raw.githubusercontent.com/K1tosh1/AlbionHelper/main/version.txt"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                remote_version = response.text.strip()
                if remote_version == current_version.strip():
                    print("Версия установлена")
                else:
                    print("Обнаружена новая версия")
                    msg = CTkMessagebox(title="Обновление", message="Мы нашли новую версию, вы хотите перейти на страницу загрузки?",
                        icon="question", option_2="Да", option_1="Нет")
                    response = msg.get()
                    if response=="Да":
                        webbrowser.open('https://github.com/K1tosh1/AlbionHelper/releases')
                        app.destroy()       
            else:
                print("Не удалось получить версию по ссылке")
        except requests.exceptions.RequestException as e:
            print("Ошибка при выполнении запроса:", str(e))
        self.mainloop()
    
    def get_server(self, value):
        self.selected_server = value
        if self.selected_server == "Западный":
            url = "https://west.albion-online-data.com/api/v2/stats/prices/"
            self.url = url
        elif self.selected_server == "Восточный":
            url = "https://east.albion-online-data.com/api/v2/stats/prices/"
            self.url = url
        return url

    def get_category(self, value):
        self.selected_category = value
        if self.selected_category == "Аксессуары":
            item_ids = ['T2_BAG','T3_BAG','T4_BAG','T4_BAG@1','T4_BAG@2','T4_BAG@3','T4_BAG@4','T5_BAG','T5_BAG@1','T5_BAG@2','T5_BAG@3','T5_BAG@4',
                        'T6_BAG','T6_BAG@1','T6_BAG@2','T6_BAG@3','T6_BAG@4','T7_BAG','T7_BAG@1','T7_BAG@2','T7_BAG@3','T7_BAG@4','T8_BAG','T8_BAG@1',
                        'T8_BAG@2','T8_BAG@3','T8_BAG@4','T4_BAG_INSIGHT','T4_BAG_INSIGHT@1','T4_BAG_INSIGHT@2','T4_BAG_INSIGHT@3','T4_BAG_INSIGHT@4',
                        'T5_BAG_INSIGHT','T5_BAG_INSIGHT@1','T5_BAG_INSIGHT@2','T5_BAG_INSIGHT@3','T5_BAG_INSIGHT@4','T6_BAG_INSIGHT','T6_BAG_INSIGHT@1',
                        'T6_BAG_INSIGHT@2','T6_BAG_INSIGHT@3','T6_BAG_INSIGHT@4','T7_BAG_INSIGHT','T7_BAG_INSIGHT@1','T7_BAG_INSIGHT@2','T7_BAG_INSIGHT@3',
                        'T7_BAG_INSIGHT@4','T8_BAG_INSIGHT','T8_BAG_INSIGHT@1','T8_BAG_INSIGHT@2','T8_BAG_INSIGHT@3','T8_BAG_INSIGHT@4',
                        'T2_CAPE','T3_CAPE','T4_CAPE','T4_CAPE@1','T4_CAPE@2','T4_CAPE@3','T4_CAPE@4','T5_CAPE','T5_CAPE@1','T5_CAPE@2','T5_CAPE@3','T5_CAPE@4',
                        'T6_CAPE','T6_CAPE@1','T6_CAPE@2','T6_CAPE@3','T6_CAPE@4','T7_CAPE','T7_CAPE@1','T7_CAPE@2','T7_CAPE@3','T7_CAPE@4','T8_CAPE','T8_CAPE@1',
                        'T8_CAPE@2','T8_CAPE@3','T8_CAPE@4','T4_CAPEITEM_DEMON','T4_CAPEITEM_DEMON@1','T4_CAPEITEM_DEMON@2','T4_CAPEITEM_DEMON@3','T4_CAPEITEM_DEMON@4',
                        'T5_CAPEITEM_DEMON','T5_CAPEITEM_DEMON@1','T5_CAPEITEM_DEMON@2','T5_CAPEITEM_DEMON@3','T5_CAPEITEM_DEMON@4','T6_CAPEITEM_DEMON','T6_CAPEITEM_DEMON@1',
                        'T6_CAPEITEM_DEMON@2','T6_CAPEITEM_DEMON@3','T6_CAPEITEM_DEMON@4','T7_CAPEITEM_DEMON','T7_CAPEITEM_DEMON@1','T7_CAPEITEM_DEMON@2','T7_CAPEITEM_DEMON@3',
                        'T7_CAPEITEM_DEMON@4','T8_CAPEITEM_DEMON','T8_CAPEITEM_DEMON@1','T8_CAPEITEM_DEMON@2','T8_CAPEITEM_DEMON@3','T8_CAPEITEM_DEMON@4',
                        'T4_CAPEITEM_FW_CAERLEON','T4_CAPEITEM_FW_CAERLEON@1','T4_CAPEITEM_FW_CAERLEON@2','T4_CAPEITEM_FW_CAERLEON@3','T4_CAPEITEM_FW_CAERLEON@4',
                        'T5_CAPEITEM_FW_CAERLEON','T5_CAPEITEM_FW_CAERLEON@1','T5_CAPEITEM_FW_CAERLEON@2','T5_CAPEITEM_FW_CAERLEON@3','T5_CAPEITEM_FW_CAERLEON@4',
                        'T6_CAPEITEM_FW_CAERLEON','T6_CAPEITEM_FW_CAERLEON@1','T6_CAPEITEM_FW_CAERLEON@2','T6_CAPEITEM_FW_CAERLEON@3','T6_CAPEITEM_FW_CAERLEON@4',
                        'T7_CAPEITEM_FW_CAERLEON','T7_CAPEITEM_FW_CAERLEON@1','T7_CAPEITEM_FW_CAERLEON@2','T7_CAPEITEM_FW_CAERLEON@3','T7_CAPEITEM_FW_CAERLEON@4',
                        'T8_CAPEITEM_FW_CAERLEON','T8_CAPEITEM_FW_CAERLEON@1','T8_CAPEITEM_FW_CAERLEON@2','T8_CAPEITEM_FW_CAERLEON@3','T8_CAPEITEM_FW_CAERLEON@4',
                        'T4_CAPEITEM_FW_BRIDGEWATCH','T4_CAPEITEM_FW_BRIDGEWATCH@1','T4_CAPEITEM_FW_BRIDGEWATCH@2','T4_CAPEITEM_FW_BRIDGEWATCH@3','T4_CAPEITEM_FW_BRIDGEWATCH@4',
                        'T5_CAPEITEM_FW_BRIDGEWATCH','T5_CAPEITEM_FW_BRIDGEWATCH@1','T5_CAPEITEM_FW_BRIDGEWATCH@2','T5_CAPEITEM_FW_BRIDGEWATCH@3','T5_CAPEITEM_FW_BRIDGEWATCH@4',
                        'T6_CAPEITEM_FW_BRIDGEWATCH','T6_CAPEITEM_FW_BRIDGEWATCH@1','T6_CAPEITEM_FW_BRIDGEWATCH@2','T6_CAPEITEM_FW_BRIDGEWATCH@3','T6_CAPEITEM_FW_BRIDGEWATCH@4',
                        'T7_CAPEITEM_FW_BRIDGEWATCH','T7_CAPEITEM_FW_BRIDGEWATCH@1','T7_CAPEITEM_FW_BRIDGEWATCH@2','T7_CAPEITEM_FW_BRIDGEWATCH@3','T7_CAPEITEM_FW_BRIDGEWATCH@4',
                        'T8_CAPEITEM_FW_BRIDGEWATCH','T8_CAPEITEM_FW_BRIDGEWATCH@1','T8_CAPEITEM_FW_BRIDGEWATCH@2','T8_CAPEITEM_FW_BRIDGEWATCH@3','T8_CAPEITEM_FW_BRIDGEWATCH@4',
                        'T4_CAPEITEM_FW_FORTSTERLING','T4_CAPEITEM_FW_FORTSTERLING@1','T4_CAPEITEM_FW_FORTSTERLING@2','T4_CAPEITEM_FW_FORTSTERLING@3','T4_CAPEITEM_FW_FORTSTERLING@4',
                        'T5_CAPEITEM_FW_FORTSTERLING','T5_CAPEITEM_FW_FORTSTERLING@1','T5_CAPEITEM_FW_FORTSTERLING@2','T5_CAPEITEM_FW_FORTSTERLING@3','T5_CAPEITEM_FW_FORTSTERLING@4',
                        'T6_CAPEITEM_FW_FORTSTERLING','T6_CAPEITEM_FW_FORTSTERLING@1','T6_CAPEITEM_FW_FORTSTERLING@2','T6_CAPEITEM_FW_FORTSTERLING@3','T6_CAPEITEM_FW_FORTSTERLING@4',
                        'T7_CAPEITEM_FW_FORTSTERLING','T7_CAPEITEM_FW_FORTSTERLING@1','T7_CAPEITEM_FW_FORTSTERLING@2','T7_CAPEITEM_FW_FORTSTERLING@3','T7_CAPEITEM_FW_FORTSTERLING@4',
                        'T8_CAPEITEM_FW_FORTSTERLING','T8_CAPEITEM_FW_FORTSTERLING@1','T8_CAPEITEM_FW_FORTSTERLING@2','T8_CAPEITEM_FW_FORTSTERLING@3','T8_CAPEITEM_FW_FORTSTERLING@4',
                        'T4_CAPEITEM_FW_LYMHURST','T4_CAPEITEM_FW_LYMHURST@1','T4_CAPEITEM_FW_LYMHURST@2','T4_CAPEITEM_FW_LYMHURST@3','T4_CAPEITEM_FW_LYMHURST@4',
                        'T5_CAPEITEM_FW_LYMHURST','T5_CAPEITEM_FW_LYMHURST@1','T5_CAPEITEM_FW_LYMHURST@2','T5_CAPEITEM_FW_LYMHURST@3','T5_CAPEITEM_FW_LYMHURST@4',
                        'T6_CAPEITEM_FW_LYMHURST','T6_CAPEITEM_FW_LYMHURST@1','T6_CAPEITEM_FW_LYMHURST@2','T6_CAPEITEM_FW_LYMHURST@3','T6_CAPEITEM_FW_LYMHURST@4',
                        'T7_CAPEITEM_FW_LYMHURST','T7_CAPEITEM_FW_LYMHURST@1','T7_CAPEITEM_FW_LYMHURST@2','T7_CAPEITEM_FW_LYMHURST@3','T7_CAPEITEM_FW_LYMHURST@4',
                        'T8_CAPEITEM_FW_LYMHURST','T8_CAPEITEM_FW_LYMHURST@1','T8_CAPEITEM_FW_LYMHURST@2','T8_CAPEITEM_FW_LYMHURST@3','T8_CAPEITEM_FW_LYMHURST@4',
                        'T4_CAPEITEM_FW_MARTLOCK','T4_CAPEITEM_FW_MARTLOCK@1','T4_CAPEITEM_FW_MARTLOCK@2','T4_CAPEITEM_FW_MARTLOCK@3','T4_CAPEITEM_FW_MARTLOCK@4',
                        'T5_CAPEITEM_FW_MARTLOCK','T5_CAPEITEM_FW_MARTLOCK@1','T5_CAPEITEM_FW_MARTLOCK@2','T5_CAPEITEM_FW_MARTLOCK@3','T5_CAPEITEM_FW_MARTLOCK@4',
                        'T6_CAPEITEM_FW_MARTLOCK','T6_CAPEITEM_FW_MARTLOCK@1','T6_CAPEITEM_FW_MARTLOCK@2','T6_CAPEITEM_FW_MARTLOCK@3','T6_CAPEITEM_FW_MARTLOCK@4',
                        'T7_CAPEITEM_FW_MARTLOCK','T7_CAPEITEM_FW_MARTLOCK@1','T7_CAPEITEM_FW_MARTLOCK@2','T7_CAPEITEM_FW_MARTLOCK@3','T7_CAPEITEM_FW_MARTLOCK@4',
                        'T8_CAPEITEM_FW_MARTLOCK','T8_CAPEITEM_FW_MARTLOCK@1','T8_CAPEITEM_FW_MARTLOCK@2','T8_CAPEITEM_FW_MARTLOCK@3','T8_CAPEITEM_FW_MARTLOCK@4',
                        'T4_CAPEITEM_FW_THETFORD','T4_CAPEITEM_FW_THETFORD@1','T4_CAPEITEM_FW_THETFORD@2','T4_CAPEITEM_FW_THETFORD@3','T4_CAPEITEM_FW_THETFORD@4',
                        'T5_CAPEITEM_FW_THETFORD','T5_CAPEITEM_FW_THETFORD@1','T5_CAPEITEM_FW_THETFORD@2','T5_CAPEITEM_FW_THETFORD@3','T5_CAPEITEM_FW_THETFORD@4',
                        'T6_CAPEITEM_FW_THETFORD','T6_CAPEITEM_FW_THETFORD@1','T6_CAPEITEM_FW_THETFORD@2','T6_CAPEITEM_FW_THETFORD@3','T6_CAPEITEM_FW_THETFORD@4',
                        'T7_CAPEITEM_FW_THETFORD','T7_CAPEITEM_FW_THETFORD@1','T7_CAPEITEM_FW_THETFORD@2','T7_CAPEITEM_FW_THETFORD@3','T7_CAPEITEM_FW_THETFORD@4',
                        'T8_CAPEITEM_FW_THETFORD','T8_CAPEITEM_FW_THETFORD@1','T8_CAPEITEM_FW_THETFORD@2','T8_CAPEITEM_FW_THETFORD@3','T8_CAPEITEM_FW_THETFORD@4',
                        'T4_CAPEITEM_HERETIC','T4_CAPEITEM_HERETIC@1','T4_CAPEITEM_HERETIC@2','T4_CAPEITEM_HERETIC@3','T4_CAPEITEM_HERETIC@4',
                        'T5_CAPEITEM_HERETIC','T5_CAPEITEM_HERETIC@1','T5_CAPEITEM_HERETIC@2','T5_CAPEITEM_HERETIC@3','T5_CAPEITEM_HERETIC@4',
                        'T6_CAPEITEM_HERETIC','T6_CAPEITEM_HERETIC@1','T6_CAPEITEM_HERETIC@2','T6_CAPEITEM_HERETIC@3','T6_CAPEITEM_HERETIC@4',
                        'T7_CAPEITEM_HERETIC','T7_CAPEITEM_HERETIC@1','T7_CAPEITEM_HERETIC@2','T7_CAPEITEM_HERETIC@3','T7_CAPEITEM_HERETIC@4',
                        'T8_CAPEITEM_HERETIC','T8_CAPEITEM_HERETIC@1','T8_CAPEITEM_HERETIC@2','T8_CAPEITEM_HERETIC@3','T8_CAPEITEM_HERETIC@4',
                        'T4_CAPEITEM_KEEPER','T4_CAPEITEM_KEEPER@1','T4_CAPEITEM_KEEPER@2','T4_CAPEITEM_KEEPER@3','T4_CAPEITEM_KEEPER@4',
                        'T5_CAPEITEM_KEEPER','T5_CAPEITEM_KEEPER@1','T5_CAPEITEM_KEEPER@2','T5_CAPEITEM_KEEPER@3','T5_CAPEITEM_KEEPER@4',
                        'T6_CAPEITEM_KEEPER','T6_CAPEITEM_KEEPER@1','T6_CAPEITEM_KEEPER@2','T6_CAPEITEM_KEEPER@3','T6_CAPEITEM_KEEPER@4',
                        'T7_CAPEITEM_KEEPER','T7_CAPEITEM_KEEPER@1','T7_CAPEITEM_KEEPER@2','T7_CAPEITEM_KEEPER@3','T7_CAPEITEM_KEEPER@4',
                        'T8_CAPEITEM_KEEPER','T8_CAPEITEM_KEEPER@1','T8_CAPEITEM_KEEPER@2','T8_CAPEITEM_KEEPER@3','T8_CAPEITEM_KEEPER@4',
                        'T4_CAPEITEM_MORGANA','T4_CAPEITEM_MORGANA@1','T4_CAPEITEM_MORGANA@2','T4_CAPEITEM_MORGANA@3','T4_CAPEITEM_MORGANA@4',
                        'T5_CAPEITEM_MORGANA','T5_CAPEITEM_MORGANA@1','T5_CAPEITEM_MORGANA@2','T5_CAPEITEM_MORGANA@3','T5_CAPEITEM_MORGANA@4',
                        'T6_CAPEITEM_MORGANA','T6_CAPEITEM_MORGANA@1','T6_CAPEITEM_MORGANA@2','T6_CAPEITEM_MORGANA@3','T6_CAPEITEM_MORGANA@4',
                        'T7_CAPEITEM_MORGANA','T7_CAPEITEM_MORGANA@1','T7_CAPEITEM_MORGANA@2','T7_CAPEITEM_MORGANA@3','T7_CAPEITEM_MORGANA@4',
                        'T8_CAPEITEM_MORGANA','T8_CAPEITEM_MORGANA@1','T8_CAPEITEM_MORGANA@2','T8_CAPEITEM_MORGANA@3','T8_CAPEITEM_MORGANA@4',
                        'T4_CAPEITEM_UNDEAD','T4_CAPEITEM_UNDEAD@1','T4_CAPEITEM_UNDEAD@2','T4_CAPEITEM_UNDEAD@3','T4_CAPEITEM_UNDEAD@4',
                        'T5_CAPEITEM_UNDEAD','T5_CAPEITEM_UNDEAD@1','T5_CAPEITEM_UNDEAD@2','T5_CAPEITEM_UNDEAD@3','T5_CAPEITEM_UNDEAD@4',
                        'T6_CAPEITEM_UNDEAD','T6_CAPEITEM_UNDEAD@1','T6_CAPEITEM_UNDEAD@2','T6_CAPEITEM_UNDEAD@3','T6_CAPEITEM_UNDEAD@4',
                        'T7_CAPEITEM_UNDEAD','T7_CAPEITEM_UNDEAD@1','T7_CAPEITEM_UNDEAD@2','T7_CAPEITEM_UNDEAD@3','T7_CAPEITEM_UNDEAD@4',
                        'T8_CAPEITEM_UNDEAD','T8_CAPEITEM_UNDEAD@1','T8_CAPEITEM_UNDEAD@2','T8_CAPEITEM_UNDEAD@3','T8_CAPEITEM_UNDEAD@4']
        elif self.selected_category == "Тканевая броня":
            item_ids = ['T2_ARMOR_CLOTH_SET1','T3_ARMOR_CLOTH_SET1','T4_ARMOR_CLOTH_SET1','T4_ARMOR_CLOTH_SET1@1','T4_ARMOR_CLOTH_SET1@2','T4_ARMOR_CLOTH_SET1@3','T4_ARMOR_CLOTH_SET1@4',
                        'T5_ARMOR_CLOTH_SET1','T5_ARMOR_CLOTH_SET1@1','T5_ARMOR_CLOTH_SET1@2','T5_ARMOR_CLOTH_SET1@3','T5_ARMOR_CLOTH_SET1@4',
                        'T6_ARMOR_CLOTH_SET1',' T6_ARMOR_CLOTH_SET1@1','T6_ARMOR_CLOTH_SET1@2','T6_ARMOR_CLOTH_SET1@3','T6_ARMOR_CLOTH_SET1@4',
                        'T7_ARMOR_CLOTH_SET1','T7_ARMOR_CLOTH_SET1@1','T7_ARMOR_CLOTH_SET1@2','T7_ARMOR_CLOTH_SET1@3','T7_ARMOR_CLOTH_SET1@4',
                        'T8_ARMOR_CLOTH_SET1','T8_ARMOR_CLOTH_SET1@1','T8_ARMOR_CLOTH_SET1@2','T8_ARMOR_CLOTH_SET1@3','T8_ARMOR_CLOTH_SET1@4',
                        'T4_ARMOR_CLOTH_SET2','T4_ARMOR_CLOTH_SET2@1','T4_ARMOR_CLOTH_SET2@2','T4_ARMOR_CLOTH_SET2@3','T4_ARMOR_CLOTH_SET2@4',
                        'T5_ARMOR_CLOTH_SET2','T5_ARMOR_CLOTH_SET2@1','T5_ARMOR_CLOTH_SET2@2','T5_ARMOR_CLOTH_SET2@3','T5_ARMOR_CLOTH_SET2@4',
                        'T6_ARMOR_CLOTH_SET2','T6_ARMOR_CLOTH_SET2@1','T6_ARMOR_CLOTH_SET2@2','T6_ARMOR_CLOTH_SET2@3','T6_ARMOR_CLOTH_SET2@4',
                        'T7_ARMOR_CLOTH_SET2','T7_ARMOR_CLOTH_SET2@1','T7_ARMOR_CLOTH_SET2@2','T7_ARMOR_CLOTH_SET2@3','T7_ARMOR_CLOTH_SET2@4',
                        'T8_ARMOR_CLOTH_SET2','T8_ARMOR_CLOTH_SET2@1','T8_ARMOR_CLOTH_SET2@2','T8_ARMOR_CLOTH_SET2@3','T8_ARMOR_CLOTH_SET2@4',
                        'T4_ARMOR_CLOTH_SET3','T4_ARMOR_CLOTH_SET3@1','T4_ARMOR_CLOTH_SET3@2','T4_ARMOR_CLOTH_SET3@3','T4_ARMOR_CLOTH_SET3@4',
                        'T5_ARMOR_CLOTH_SET3','T5_ARMOR_CLOTH_SET3@1','T5_ARMOR_CLOTH_SET3@2','T5_ARMOR_CLOTH_SET3@3','T5_ARMOR_CLOTH_SET3@4',
                        'T6_ARMOR_CLOTH_SET3','T6_ARMOR_CLOTH_SET3@1','T6_ARMOR_CLOTH_SET3@2','T6_ARMOR_CLOTH_SET3@3','T6_ARMOR_CLOTH_SET3@4',
                        'T7_ARMOR_CLOTH_SET3','T7_ARMOR_CLOTH_SET3@1','T7_ARMOR_CLOTH_SET3@2','T7_ARMOR_CLOTH_SET3@3','T7_ARMOR_CLOTH_SET3@4',
                        'T8_ARMOR_CLOTH_SET3','T8_ARMOR_CLOTH_SET3@1','T8_ARMOR_CLOTH_SET3@2','T8_ARMOR_CLOTH_SET3@3','T8_ARMOR_CLOTH_SET3@4',
                        'T4_ARMOR_CLOTH_KEEPER','T4_ARMOR_CLOTH_KEEPER@1','T4_ARMOR_CLOTH_KEEPER@2','T4_ARMOR_CLOTH_KEEPER@3','T4_ARMOR_CLOTH_KEEPER@4',
                        'T5_ARMOR_CLOTH_KEEPER','T5_ARMOR_CLOTH_KEEPER@1','T5_ARMOR_CLOTH_KEEPER@2','T5_ARMOR_CLOTH_KEEPER@3','T5_ARMOR_CLOTH_KEEPER@4',
                        'T6_ARMOR_CLOTH_KEEPER','T6_ARMOR_CLOTH_KEEPER@1','T6_ARMOR_CLOTH_KEEPER@2','T6_ARMOR_CLOTH_KEEPER@3','T6_ARMOR_CLOTH_KEEPER@4',
                        'T7_ARMOR_CLOTH_KEEPER','T7_ARMOR_CLOTH_KEEPER@1','T7_ARMOR_CLOTH_KEEPER@2','T7_ARMOR_CLOTH_KEEPER@3','T7_ARMOR_CLOTH_KEEPER@4',
                        'T8_ARMOR_CLOTH_KEEPER','T8_ARMOR_CLOTH_KEEPER@1','T8_ARMOR_CLOTH_KEEPER@2','T8_ARMOR_CLOTH_KEEPER@3','T8_ARMOR_CLOTH_KEEPER@4',
                        'T4_ARMOR_CLOTH_HELL','T4_ARMOR_CLOTH_HELL@1','T4_ARMOR_CLOTH_HELL@2','T4_ARMOR_CLOTH_HELL@3','T4_ARMOR_CLOTH_HELL@4',
                        'T5_ARMOR_CLOTH_HELL','T5_ARMOR_CLOTH_HELL@1','T5_ARMOR_CLOTH_HELL@2','T5_ARMOR_CLOTH_HELL@3','T5_ARMOR_CLOTH_HELL@4',
                        'T6_ARMOR_CLOTH_HELL','T6_ARMOR_CLOTH_HELL@1','T6_ARMOR_CLOTH_HELL@2','T6_ARMOR_CLOTH_HELL@3','T6_ARMOR_CLOTH_HELL@4',
                        'T7_ARMOR_CLOTH_HELL','T7_ARMOR_CLOTH_HELL@1','T7_ARMOR_CLOTH_HELL@2','T7_ARMOR_CLOTH_HELL@3','T7_ARMOR_CLOTH_HELL@4',
                        'T8_ARMOR_CLOTH_HELL','T8_ARMOR_CLOTH_HELL@1','T8_ARMOR_CLOTH_HELL@2','T8_ARMOR_CLOTH_HELL@3','T8_ARMOR_CLOTH_HELL@4']
        elif self.selected_category == 'Тканевый шлем':
            item_ids = ['T2_HEAD_CLOTH_SET1','T3_HEAD_CLOTH_SET1','T4_HEAD_CLOTH_SET1','T4_HEAD_CLOTH_SET1@1','T4_HEAD_CLOTH_SET1@2','T4_HEAD_CLOTH_SET1@3','T4_HEAD_CLOTH_SET1@4',
                        'T5_HEAD_CLOTH_SET1','T5_HEAD_CLOTH_SET1@1','T5_HEAD_CLOTH_SET1@2','T5_HEAD_CLOTH_SET1@3','T5_HEAD_CLOTH_SET1@4',
                        'T6_HEAD_CLOTH_SET1','T6_HEAD_CLOTH_SET1@1','T6_HEAD_CLOTH_SET1@2','T6_HEAD_CLOTH_SET1@3','T6_HEAD_CLOTH_SET1@4',
                        'T7_HEAD_CLOTH_SET1','T7_HEAD_CLOTH_SET1@1','T7_HEAD_CLOTH_SET1@2','T7_HEAD_CLOTH_SET1@3','T7_HEAD_CLOTH_SET1@4',
                        'T8_HEAD_CLOTH_SET1','T8_HEAD_CLOTH_SET1@1','T8_HEAD_CLOTH_SET1@2','T8_HEAD_CLOTH_SET1@3','T8_HEAD_CLOTH_SET1@4',
                        'T4_HEAD_CLOTH_SET2','T4_HEAD_CLOTH_SET2@1','T4_HEAD_CLOTH_SET2@2','T4_HEAD_CLOTH_SET2@3','T4_HEAD_CLOTH_SET2@4',
                        'T5_HEAD_CLOTH_SET2','T5_HEAD_CLOTH_SET2@1','T5_HEAD_CLOTH_SET2@2','T5_HEAD_CLOTH_SET2@3','T5_HEAD_CLOTH_SET2@4',
                        'T6_HEAD_CLOTH_SET2','T6_HEAD_CLOTH_SET2@1','T6_HEAD_CLOTH_SET2@2','T6_HEAD_CLOTH_SET2@3','T6_HEAD_CLOTH_SET2@4',
                        'T7_HEAD_CLOTH_SET2','T7_HEAD_CLOTH_SET2@1','T7_HEAD_CLOTH_SET2@2','T7_HEAD_CLOTH_SET2@3','T7_HEAD_CLOTH_SET2@4',
                        'T8_HEAD_CLOTH_SET2','T8_HEAD_CLOTH_SET2@1','T8_HEAD_CLOTH_SET2@2','T8_HEAD_CLOTH_SET2@3','T8_HEAD_CLOTH_SET2@4',
                        'T4_HEAD_CLOTH_SET3','T4_HEAD_CLOTH_SET3@1','T4_HEAD_CLOTH_SET3@2','T4_HEAD_CLOTH_SET3@3','T4_HEAD_CLOTH_SET3@4',
                        'T5_HEAD_CLOTH_SET3','T5_HEAD_CLOTH_SET3@1','T5_HEAD_CLOTH_SET3@2','T5_HEAD_CLOTH_SET3@3','T5_HEAD_CLOTH_SET3@4',
                        'T6_HEAD_CLOTH_SET3','T6_HEAD_CLOTH_SET3@1','T6_HEAD_CLOTH_SET3@2','T6_HEAD_CLOTH_SET3@3','T6_HEAD_CLOTH_SET3@4',
                        'T7_HEAD_CLOTH_SET3','T7_HEAD_CLOTH_SET3@1','T7_HEAD_CLOTH_SET3@2','T7_HEAD_CLOTH_SET3@3','T7_HEAD_CLOTH_SET3@4',
                        'T8_HEAD_CLOTH_SET3','T8_HEAD_CLOTH_SET3@1','T8_HEAD_CLOTH_SET3@2','T8_HEAD_CLOTH_SET3@3','T8_HEAD_CLOTH_SET3@4',
                        'T4_HEAD_CLOTH_KEEPER','T4_HEAD_CLOTH_KEEPER@1','T4_HEAD_CLOTH_KEEPER@2','T4_HEAD_CLOTH_KEEPER@3','T4_HEAD_CLOTH_KEEPER@4',
                        'T5_HEAD_CLOTH_KEEPER','T5_HEAD_CLOTH_KEEPER@1','T5_HEAD_CLOTH_KEEPER@2','T5_HEAD_CLOTH_KEEPER@3','T5_HEAD_CLOTH_KEEPER@4',
                        'T6_HEAD_CLOTH_KEEPER','T6_HEAD_CLOTH_KEEPER@1','T6_HEAD_CLOTH_KEEPER@2','T6_HEAD_CLOTH_KEEPER@3','T6_HEAD_CLOTH_KEEPER@4',
                        'T7_HEAD_CLOTH_KEEPER','T7_HEAD_CLOTH_KEEPER@1','T7_HEAD_CLOTH_KEEPER@2','T7_HEAD_CLOTH_KEEPER@3','T7_HEAD_CLOTH_KEEPER@4',
                        'T8_HEAD_CLOTH_KEEPER','T8_HEAD_CLOTH_KEEPER@1','T8_HEAD_CLOTH_KEEPER@2','T8_HEAD_CLOTH_KEEPER@3','T8_HEAD_CLOTH_KEEPER@4',
                        'T4_HEAD_CLOTH_HELL','T4_HEAD_CLOTH_HELL@1','T4_HEAD_CLOTH_HELL@2','T4_HEAD_CLOTH_HELL@3','T4_HEAD_CLOTH_HELL@4',
                        'T5_HEAD_CLOTH_HELL','T5_HEAD_CLOTH_HELL@1','T5_HEAD_CLOTH_HELL@2','T5_HEAD_CLOTH_HELL@3','T5_HEAD_CLOTH_HELL@4',
                        'T6_HEAD_CLOTH_HELL','T6_HEAD_CLOTH_HELL@1','T6_HEAD_CLOTH_HELL@2','T6_HEAD_CLOTH_HELL@3','T6_HEAD_CLOTH_HELL@4',
                        'T7_HEAD_CLOTH_HELL','T7_HEAD_CLOTH_HELL@1','T7_HEAD_CLOTH_HELL@2','T7_HEAD_CLOTH_HELL@3','T7_HEAD_CLOTH_HELL@4',
                        'T8_HEAD_CLOTH_HELL','T8_HEAD_CLOTH_HELL@1','T8_HEAD_CLOTH_HELL@2','T8_HEAD_CLOTH_HELL@3','T8_HEAD_CLOTH_HELL@4']
        return item_ids

    def get_premium(self, value):
        self.selected_premium = value
        if self.selected_premium == "Да":
            tax = 0.4
        elif self.selected_premium == "Нет":
            tax = 0.8
        return tax
    
    def search(self, positive_profit_only=False):
        if self.selected_server is None or self.selected_category is None or self.selected_premium is None:
            CTkMessagebox(self, title="Ошибка", message="Вы должны выбрать значения в:\n\nКатегория\nСервер\nПремиум", icon="cancel")
            return
        tax = self.get_premium(self.selected_premium)
        item_ids = self.get_category(self.selected_category)
        with open('item_names.json', 'r', encoding='utf-8') as file:
            translations = json.load(file)

        strategy = []

        royal_cities = ['Martlock','Fort Sterling','Thetford','Bridgewatch','Lymhurst']

        r = requests.get(self.url + ','.join(item_ids) + '?locations=' + ','.join(royal_cities) + '&qualities=1').json()

        def process_item(item_id):
            print('Анализ: '+item_id)
            best_buy_price = 9999999
            best_buy_city = ''
            best_sell_price = 0
            best_sell_city = ''

            for royal_city in royal_cities:
                r_filter = list(filter(lambda r: (r['item_id'] == item_id) & (r['city'] == royal_city), r))[0]
                tmp_buy_price = r_filter['sell_price_min']
                if tmp_buy_price == 0:
                    tmp_buy_price = 99999999
                tmp_sell_price = r_filter['buy_price_max']
                if r_filter['sell_price_min'] < best_buy_price:
                    best_buy_price = tmp_buy_price
                    best_buy_city = royal_city
                if r_filter['buy_price_max'] > best_sell_price:
                    best_sell_price = tmp_sell_price
                    best_sell_city = royal_city

            raw_profit = (best_sell_price - best_buy_price)*100
            fees = best_sell_price * tax

            return [item_id, best_buy_city, best_buy_price, best_sell_city, best_sell_price, best_sell_price - best_buy_price, raw_profit, fees, raw_profit - fees, (raw_profit - fees) / best_buy_price]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = executor.map(process_item, item_ids)
            for result in results:
                if result is not None:
                    strategy.append(result)

            strategy.sort(key=lambda x: x[6], reverse=True)

        for index, item in enumerate(strategy):
            item_id, best_buy_city, best_buy_price, best_sell_city, best_sell_price, profit, raw_profit, fees, net_profit, profit_percentage = item

            if positive_profit_only and net_profit <= 0:
                continue
            item_frame = customtkinter.CTkFrame(self.content, height=74, border_width=1, border_color='#FEFDCA')
            item_frame.grid(row=index, column=0, pady=10, padx=10, sticky="nsew")

            image_path = f"img/{item_id}.png"
            image = Image.open(image_path)
            image = image.resize((74, 74), Image.LANCZOS)
            tk_image = ImageTk.PhotoImage(image)

            item_image = customtkinter.CTkLabel(item_frame, image=tk_image, text='')
            item_image.image = tk_image
            item_image.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

            self.content.grid_rowconfigure(index, weight=1)
            self.content.grid_columnconfigure(0, weight=1)
            if item_id in translations:
                translated_item_id = translations[item_id]
            else:
                translated_item_id = item_id
            item_name = customtkinter.CTkLabel(item_frame, text=translated_item_id)
            item_name.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

            item_buy_city = customtkinter.CTkLabel(item_frame, text='Купить в '+str(best_buy_city))
            item_buy_city.grid(row=0, column=2, pady=5, sticky="nsew")

            item_buy_price = customtkinter.CTkLabel(item_frame, text='за '+str(best_buy_price)+'$')
            item_buy_price.grid(row=0, column=3, pady=5, padx=5, sticky="nsew")

            item_sell_city = customtkinter.CTkLabel(item_frame, text='Продать в '+str(best_sell_city))
            item_sell_city.grid(row=0, column=4, pady=5, sticky="nsew")

            item_sell_price = customtkinter.CTkLabel(item_frame, text='за '+str(best_sell_price)+'$')
            item_sell_price.grid(row=0, column=5, pady=5, padx=5, sticky="nsew")

            item_profit_text = 'Прибыль: ' + str(int(net_profit)) + '$'
            item_profit = customtkinter.CTkLabel(item_frame, text=item_profit_text)
            item_profit.grid(row=0, column=6, pady=10, padx=10, sticky="nsew")

            if net_profit > 0:
                item_profit.configure(text_color='green')
            else:
                item_profit.configure(text_color='red')

    def search_in_background(self):
        t = threading.Thread(target=self.search, args=(True,))
        t.start()
        
if __name__ == "__main__":
    app = Loader()
    app.mainloop()