import flet as ft
from frontend.components.flet_componets import CustomContainer, CustomText
from frontend.view.title_bar_view import TitleBar
from frontend.view.main_view import MainViewPage


class MainController:
    def __init__(self, page: ft.Page):
        self.page = page
        self.configure_view()
        self.build_ui()

    def configure_view(self):
        self.page.window.width = 350
        self.page.window.height = 600
        self.page.window.page.padding = 0

        self.page.window.page.bgcolor = ft.Colors.BLACK45
        self.page.window.frameless = True  # Sin bordes

    def build_ui(self):
        self.page.add(
            ft.Container(content=TitleBar().build_ui()),
            MainViewPage().build_ui(),
        )  # Text la barra de título personalizada)
