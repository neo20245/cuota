import flet as ft
from frontend.view.main_view import MainViewPage


class MainController:
    def __init__(self, page: ft.Page):
        self.page = page
        self.configure_view()
        self.build_ui()

    def configure_view(self):
        self.page.window.width = 350
        self.page.window.height = 600
        self.page.padding=0
        self.page.window.frameless=True
    def build_ui(self):
        main_view= MainViewPage()
        self.page.add(main_view)  # Agrega la vista principal a la página (incluyendo la barra de título personalizada)
