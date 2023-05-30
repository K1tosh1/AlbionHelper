import customtkinter
from CTkMessagebox import CTkMessagebox
import requests

class Albion_Helper(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("dark")
        self.title("Albion Helper")
        self.selected_server = None

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        window_width = int(screen_width * 0.7)
        window_height = int(screen_height * 0.7)

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Left sidebar
        sidebar_width = 380
        sidebar = customtkinter.CTkFrame(self, width=sidebar_width, fg_color="#222831")
        sidebar.grid(row=0, column=0, sticky="ns")

        category = customtkinter.CTkComboBox(sidebar, values=['Сумки'], state = 'readonly',command=self.get_category)
        category.set(value="Выбери категорию")
        category.grid(row=0, column=0, pady=5,padx=5, sticky="nsew")

        server = customtkinter.CTkComboBox(sidebar, values=['Западный','Восточный'], state = 'readonly', command=self.get_server)
        server.set(value="Выбери сервер")
        server.grid(row=1, column=0, pady=5, padx=5,sticky="nsew")

        premium = customtkinter.CTkComboBox(sidebar, values=['Да','Нет'], state = 'readonly', command=self.get_premium)
        premium.set(value="Премиум")
        premium.grid(row=2, column=0, pady=5, padx=5,sticky="nsew")

        btn_search = customtkinter.CTkButton(sidebar, text="Поиск")
        btn_search.grid(row=3, column=0, padx=15, pady=15, sticky='nsew')


        # Main content area
        content = customtkinter.CTkScrollableFrame(self, fg_color="#393E46")
        content.grid(row=0, column=1, sticky="nsew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def get_server(self, value):
        self.selected_server = value
        if self.selected_server == "Западный":
            url = "https://west.albion-online-data.com/api/v2/stats/prices/"
            print(url)
        elif self.selected_server == "Восточный":
            url = "https://east.albion-online-data.com/api/v2/stats/prices/"
            print(url)
        return url

    def get_category(self, value):
        self.selected_category = value
        if self.selected_category == "Сумки":
            item_ids = ['T2_BAG','T3_BAG','T4_BAG','T4_BAG@1','T4_BAG@2','T4_BAG@3','T4_BAG@4','T5_BAG','T5_BAG@1','T5_BAG@2','T5_BAG@3','T5_BAG@4',
                        'T6_BAG','T6_BAG@1','T6_BAG@2','T6_BAG@3','T6_BAG@4','T7_BAG','T7_BAG@1','T7_BAG@2','T7_BAG@3','T7_BAG@4','T8_BAG','T8_BAG@1',
                        'T8_BAG@2','T8_BAG@3','T8_BAG@4','T4_BAG_INSIGHT','T4_BAG_INSIGHT@1','T4_BAG_INSIGHT@2','T4_BAG_INSIGHT@3','T4_BAG_INSIGHT@4',
                        'T5_BAG_INSIGHT','T5_BAG_INSIGHT@1','T5_BAG_INSIGHT@2','T5_BAG_INSIGHT@3','T5_BAG_INSIGHT@4','T6_BAG_INSIGHT','T6_BAG_INSIGHT@1',
                        'T6_BAG_INSIGHT@2','T6_BAG_INSIGHT@3','T6_BAG_INSIGHT@4','T7_BAG_INSIGHT','T7_BAG_INSIGHT@1','T7_BAG_INSIGHT@2','T7_BAG_INSIGHT@3',
                        'T7_BAG_INSIGHT@4','T8_BAG_INSIGHT','T8_BAG_INSIGHT@1','T8_BAG_INSIGHT@2','T8_BAG_INSIGHT@3','T8_BAG_INSIGHT@4']
            print(item_ids)
            return item_ids

    def get_premium(self, value):
        self.selected_premium = value
        if self.selected_premium == "Да":
            tax = 0.4
            print(tax)
        elif self.selected_premium == "Нет":
            tax = 0.8
            print(tax)
        return tax


if __name__ == "__main__":
    app = Albion_Helper()
    app.mainloop()
