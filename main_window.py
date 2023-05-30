import customtkinter
from tkinter import messagebox
import requests
from PIL import Image, ImageTk


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

        # Left sidebar
        sidebar_width = 380
        sidebar = customtkinter.CTkFrame(self, width=sidebar_width, fg_color="#222831")
        sidebar.grid(row=0, column=0, sticky="ns")

        label_category = customtkinter.CTkLabel(sidebar, text="Категория")
        label_category.grid(row=0, column=0)
        category = customtkinter.CTkComboBox(sidebar, values=['Сумки'], state = 'readonly',command=self.get_category)
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

        btn_search = customtkinter.CTkButton(sidebar, text="Поиск", command=self.search)
        btn_search.grid(row=7, column=0, padx=15, pady=15, sticky='nsew')


        # Main content area
        self.content = customtkinter.CTkScrollableFrame(self, fg_color="#393E46")
        self.content.grid(row=0, column=1, sticky="nsew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def get_server(self, value):
        self.selected_server = value
        if self.selected_server == "Западный":
            url = "https://west.albion-online-data.com/api/v2/stats/prices/"
            self.url = url
            print(url)
        elif self.selected_server == "Восточный":
            url = "https://east.albion-online-data.com/api/v2/stats/prices/"
            self.url = url
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
    
    def search(self):
        print("Выбранный сервер:", self.selected_server)
        print("Выбранная категория:", self.selected_category)
        print("Премиум аккаунт:", self.selected_premium)
        tax = self.get_premium(self.selected_premium)
        if self.selected_server is None or self.selected_category is None or self.selected_premium is None:
            messagebox.showerror("Ошибка", "Выберите категорию, премиум статус и сервер!")

        item_ids = self.get_category(self.selected_category)

        strategy = []

        royal_cities = ['Martlock','Fort Sterling','Thetford','Bridgewatch','Lymhurst']

        r = requests.get(self.url + ','.join(item_ids) + '?locations=' + ','.join(royal_cities) + '&qualities=1').json()

        for item_id in item_ids:
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

            strategy.append([item_id, best_buy_city, best_buy_price, best_sell_city, best_sell_price, best_sell_price - best_buy_price, raw_profit, fees, raw_profit - fees, (raw_profit - fees) / best_buy_price])

        # Sort the strategy list by profit (index 6, which is raw_profit)
        strategy.sort(key=lambda x: x[6], reverse=True)

        # Loop through the sorted strategy list
        for index, item in enumerate(strategy):
            item_id, best_buy_city, best_buy_price, best_sell_city, best_sell_price, profit, raw_profit, fees, net_profit, profit_percentage = item

            item_frame = customtkinter.CTkFrame(self.content, height=74, border_width=1, border_color='#FEFDCA')
            item_frame.grid(row=index, column=0, pady=10, padx=10, sticky="nsew")

            image_path = f"img/{item_id}.png"
            image = Image.open(image_path)
            image = image.resize((74, 74), Image.LANCZOS)
            tk_image = ImageTk.PhotoImage(image)

            # Create a label widget to display the image
            item_image = customtkinter.CTkLabel(item_frame, image=tk_image, text='')
            item_image.image = tk_image  # Keep a reference to prevent garbage collection
            item_image.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

            # Configure grid weights to make item_frame expand horizontally
            self.content.grid_rowconfigure(index, weight=1)
            self.content.grid_columnconfigure(0, weight=1)

            item_name = customtkinter.CTkLabel(item_frame, text='Предмет: '+item_id)
            item_name.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

            item_buy_city = customtkinter.CTkLabel(item_frame, text='Купить в '+str(best_buy_city))
            item_buy_city.grid(row=0, column=2, pady=5, sticky="nsew")
            item_buy_price = customtkinter.CTkLabel(item_frame, text='за '+str(best_buy_price)+'$')
            item_buy_price.grid(row=0, column=3, pady=5, padx=5, sticky="nsew")
            item_sell_city = customtkinter.CTkLabel(item_frame, text='Продать в '+str(best_sell_city))
            item_sell_city.grid(row=0, column=4, pady=5, sticky="nsew")
            item_sell_price = customtkinter.CTkLabel(item_frame, text='за '+str(best_sell_price)+'$')
            item_sell_price.grid(row=0, column=5, pady=5, padx=5, sticky="nsew")
            
            # Create item_profit label and set the text color based on profit
            item_profit_text = 'Профит: ' + str(int(net_profit)) + '$' 
            item_profit = customtkinter.CTkLabel(item_frame, text=item_profit_text)
            item_profit.grid(row=0, column=6, pady=10, padx=10, sticky="nsew")
            
            if net_profit > 0:
                item_profit.configure(text_color='green')
            else:
                item_profit.configure(text_color='red')





if __name__ == "__main__":
    app = Albion_Helper()
    app.mainloop()