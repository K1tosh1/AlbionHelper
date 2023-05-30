import customtkinter
from CTkMessagebox import CTkMessagebox

class Albion_Helper(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("dark")
        self.title("Albion Helper")

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

        category = customtkinter.CTkComboBox(sidebar, values=['Сумки','Плащи','Тканевая броня','Тканевый шлем','Тканевая обувь','Кожаная броня','Кожаный шлем','Кожаная обувь','Латная броня','Латный шлем','Латная обувь'])
        category.set(value="Выбери категорию")
        category.grid(row=0, column=0, pady=5,padx=5, sticky="nsew")

        server = customtkinter.CTkComboBox(sidebar, values=['Западный','Восточный'])
        server.set(value="Выбери сервер")
        server.grid(row=1, column=0, pady=5, padx=5,sticky="nsew")

        premium = customtkinter.CTkComboBox(sidebar, values=['Да','Нет'])
        premium.set(value="Премиум")
        premium.grid(row=2, column=0, pady=5, padx=5,sticky="nsew")

        btn_search = customtkinter.CTkButton(sidebar, text="Поиск")
        btn_search.grid(row=3, column=0, padx=15, pady=15, sticky='nsew')


        # Main content area
        content = customtkinter.CTkScrollableFrame(self, fg_color="#393E46")
        content.grid(row=0, column=1, sticky="nsew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.show_info()

    # FUNCTIONS AREA:
    def show_info(self):
        CTkMessagebox(title="Информация", message="Тут надо будет написать важную хуйню")
        


if __name__ == "__main__":
    app = Albion_Helper()
    app.mainloop()
