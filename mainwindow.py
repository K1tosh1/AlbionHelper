import customtkinter as ctk

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
        self.body.grid(row=0, column=1, sticky="nsew")
        self.grid_columnconfigure(1, weight=1)

        self.dsbutton = ctk.CTkButton(self.sidemenu, text='Discord server')
        self.dsbutton.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.marketbutton = ctk.CTkButton(self.sidemenu, text='Albion Market', command=self.toggle_sidemenu)
        self.marketbutton.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.grid_rowconfigure(0, weight=1)

        self.menu = None

    def toggle_sidemenu(self):
        if self.menu is None:
            self.create_sidemenu()
        else:
            self.destroy_sidemenu()

    def create_sidemenu(self):
        self.menu = ctk.CTkFrame(self)
        self.menu.grid(row=0, column=2, sticky="nsew")
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

        self.category_cmb = ctk.CTkComboBox(self.menu, state="readonly", values=["Bag"])
        self.category_cmb.set("Bag")
        self.category_cmb.grid(row=9, column=0, padx=5, pady=10, sticky="nsew")

        self.itemlang = ctk.CTkLabel(self.menu, text="Item language")
        self.itemlang.grid(row=10, column=0, padx=10, pady=1)

        self.itemlang_cmb = ctk.CTkComboBox(self.menu, state="readonly", values=["English"])
        self.itemlang_cmb.set("English")
        self.itemlang_cmb.grid(row=11, column=0, padx=5, pady=10, sticky="nsew")

    def destroy_sidemenu(self):
        self.menu.grid_forget()
        self.menu.destroy()
        self.menu = None

app = App()
app.mainloop()
