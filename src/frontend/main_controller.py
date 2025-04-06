import flet as ft
from frontend.view.main_view import MainViewPage
from backend.app_context import AppContext


class MainController:
    def __init__(self, page: ft.Page):
        self.page = page
        self.app_context = AppContext()
        self.configure_view()
        self.build_ui()

    def configure_view(self):
        self.page.window.width = 330
        self.page.window.height = 560
        self.page.padding = 0
        self.page.window.frameless = True

    def build_ui(self):
        self.main_view = MainViewPage(page=self.page)
        self.page.add(self.main_view.build_ui())
