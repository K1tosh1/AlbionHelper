import customtkinter as ctk
from PIL import ImageTk, Image
import os, requests, json, ratelimit, time
import tkinter as tk
from tkinter import messagebox

class Albion_Helper(ctk.CTk):
    def __init__(self):
        ctk.CTk.__init__(self)
        self.title("Albion Helper")
        ctk.set_appearance_mode("system")
        self.iconbitmap("icon.ico")
        self.calculate_window_size()
        self.center_window()
        self.create_sidebar()
        self.search_history = []

    # SETUP WINDOW SIZE
    def calculate_window_size(self):
        self.update()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        width = int(screen_width * 0.7)
        height = int(screen_height * 0.7)
        self.geometry(f"{width}x{height}")

    # SETUP WINDOW CENTER
    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")


    # SIDEBAR AND MAIN CONTENT
    def create_sidebar(self):
        version = 1.1
        sidebar = ctk.CTkFrame(self, corner_radius=0)
        sidebar.configure(width=350, fg_color="#444F5A")
        sidebar.grid(row=0, column=0, sticky="ns")

        # LOGO
        image_path = "icon.png"
        image = Image.open(image_path)
        image = image.resize((100, 100))
        ctk_image = ImageTk.PhotoImage(image)
        image_label = ctk.CTkLabel(sidebar, image=ctk_image, text='')
        image_label.grid(row=0, column=0)
        ctk.CTkLabel(sidebar, text=f"Version: {version}").grid(row=1, column=0)
        server_label = ctk.CTkLabel(sidebar, text="Выбери категорию: ")
        server_label.grid(row=2, column=0, padx=10, pady=0)
        folder_path = "categories"
        file_names = os.listdir(folder_path)
        values = []
        for file_name in file_names:
            if file_name.endswith(".txt"):
                values.append(file_name)

        # CATEGORY COMBOBOX
        self.items_combobox = ctk.CTkComboBox(sidebar, height=15, width=150, values=values, state="readonly")
        self.items_combobox.set('Select Items')
        self.items_combobox.grid(row=3, column=0, padx=10, pady=10)

        #PREMIUM COMBOBOX
        self.premium_combobox = ctk.CTkComboBox(sidebar, height=15, width=150, values=['Да','Нет'], state="readonly")
        self.premium_combobox.set('Select Premium')
        self.premium_combobox.grid(row=4, column=0, padx=10, pady=10)
        ctk.CTkButton(sidebar, text="Поиск", command=self.search).grid(row=6, column=0, padx=10, pady=10)

        # CONTENT FRAME
        self.content = ctk.CTkScrollableFrame(self, corner_radius=0)
        self.content.configure(fg_color="#3E4149")
        self.content.grid(row=0, column=1, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    @ratelimit.limits(calls=180, period=60)
    def make_api_request(self, url):
        return requests.get(url).json()
    
    def show_error_message(self, message):
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Error", message)
        root.destroy()

    def search(self):
        for item_frame in self.content.winfo_children():
            item_frame.destroy()
        selected_category = self.items_combobox.get()
        royal_cities = ['Martlock', 'Fort Sterling', 'Thetford', 'Bridgewatch', 'Lymhurst', 'Caerleon']
        file_path = os.path.join("categories", selected_category)
        item_ids = []
        with open(file_path, "r") as file:
            for line in file:
                item_ids.append(line.strip())
        selected_premium = self.premium_combobox.get()
        tax = 0.0  # Initialize tax variable
        if selected_premium == "Да":
            tax = 0.4
        elif selected_premium == "Нет":
            tax = 0.8
        url = 'https://west.albion-online-data.com/api/v2/stats/prices/' + ','.join(item_ids) + '?locations=' + ','.join(royal_cities) + '&qualities=1'
        try:
            r = self.make_api_request(url)
        except ratelimit.RateLimitException as e:
            wait_time = e.period_remaining + 1
            wait_minutes = int(wait_time / 60)
            wait_seconds = int(wait_time % 60)
            message = f"API rate limit exceeded. Please wait for {wait_minutes} minutes and {wait_seconds} seconds."
            self.show_error_message(message)
            return
        with open("item_names.json", "r", encoding='utf-8') as json_file:
            item_names = json.load(json_file)
        images_folder = "img"
        for item_id in item_ids:
            print('Анализ: ' + item_id)
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
            profit = best_sell_price - best_buy_price
            profit_after_tax = int(profit * (1 - tax))
            item_name = item_names.get(item_id, item_id)
            image_path = os.path.join(images_folder, f"{item_id}.png")
            if os.path.exists(image_path):
                image = Image.open(image_path)
                image = image.resize((74, 74), Image.LANCZOS)
                item_image = ImageTk.PhotoImage(image)
            else:
                item_image = None
            if profit_after_tax > 0:
                item_frame = ctk.CTkFrame(self.content, corner_radius=10, border_width=1, border_color="#444F5A")
                item_frame.configure(fg_color="black")
                item_frame.pack(pady=5, padx=10, fill="x")
                if item_image:
                    item_image_label = ctk.CTkLabel(item_frame, image=item_image, text='')
                    item_image_label.grid(row=0, column=0, pady=5, padx=10)
                item_name_label = ctk.CTkLabel(item_frame, text=item_name, text_color="#dc8700", font=("Arial", 14))
                item_name_label.grid(row=0, column=1, pady=5, padx=10)
                item_buy = ctk.CTkLabel(item_frame, text=f"Лучшая цена покупки: {best_buy_price}$ в городе {best_buy_city}", text_color="#9b4244", font=("Arial", 12))
                item_buy.grid(row=0, column=2, pady=5, padx=10)
                item_sell = ctk.CTkLabel(item_frame, text=f"Лучшая цена продажи: {best_sell_price}$ в городе {best_sell_city}", text_color="#429b99", font=("Arial", 12))
                item_sell.grid(row=0, column=3, pady=5, padx=10)
                item_profit = ctk.CTkLabel(item_frame, text=f"Прибыль: {profit_after_tax}$", text_color="#20ab1e", font=("Arial", 12))
                item_profit.grid(row=0, column=4, pady=5, padx=10)

if __name__ == "__main__":
    app = Albion_Helper()
    app.mainloop()