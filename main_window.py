import customtkinter

class Albion_Helper(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("light")
        self.title("Albion Helper")

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        window_width = int(screen_width * 0.7)
        window_height = int(screen_height * 0.7)

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Left sidebar
        sidebar_width = 200
        sidebar = customtkinter.CTkFrame(self, width=sidebar_width, fg_color="gray")
        sidebar.grid(row=0, column=0, sticky="ns")

        # Market button in the sidebar
        market_button = customtkinter.CTkButton(sidebar, text="Market", fg_color="gray", border_width=1, border_color='lightgray')
        market_button.pack(pady=10)

        # Main content area
        content = customtkinter.CTkFrame(self, fg_color="white")
        content.grid(row=0, column=1, sticky="nsew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


if __name__ == "__main__":
    app = Albion_Helper()
    app.mainloop()
