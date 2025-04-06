import flet as ft
from frontend.main_controller import MainController
from backend.app_context  import AppContext


app_context = AppContext()

if __name__ == "__main__":
    ft.app(target=MainController, context=app_context)
