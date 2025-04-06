import flet as ft


class CustomContolerBasePage(ft.Container):
    def __init__(
        self,
        content,
        alignment=None,
        padding=8,
        margin=0,
        
        border=None,
        border_radius=None,
        width=None,
        height=None,
        
        
    ):
        super().__init__()
        self.content = content
        self.alignment = alignment
        self.padding = padding
        self.margin = margin
        self.bgcolor= ft.Colors.BLUE_500
        self.border = border
        self.border_radius = border_radius
        self.width = width
        self.height = height
        self.expand = True


class CustomContainer(ft.Container):
    def __init__(
        self,
        content,
       
        padding=20,
        margin=0,
        bgcolor=None,
        border=None,
        border_radius=None,
        width=None,
        height=None,
       
    ):
        super().__init__()
        self.content = content
        self.alignment = ft.alignment.center
        self.padding = padding
        self.margin = margin
        self.bgcolor = bgcolor
        self.border = border
        self.border_radius = border_radius
        self.width = width
        self.height = height
        self.expand = False


class CustomTextField(ft.TextField):
    def __init__(
        self, label, hint_text=None, prefix_icon=None, error_style=None, width=250, password=None
    ):
        super().__init__()
        
        self.password = password
        self.label = label
        self.hint_text = hint_text
        self.hint_style = ft.TextStyle(color=ft.Colors.GREY_500)
        self.prefix_icon = prefix_icon
        self.error_style = error_style
        self.border_color = ft.Colors.GREY_400
        self.border_radius = 10
        self.width = width
        self.bgcolor = ft.Colors.WHITE
        self.text_style = ft.TextStyle(color=ft.Colors.BLACK)

        self.cursor_color = ft.Colors.BLACK

        self.focused_color = ft.Colors.BLACK54
        self.text_size = 14


class CustomCheckbox(ft.Checkbox):
    def __init__(
        self,
        label="",
        value=False,
        disabled=False,
        fill_color=None,
        check_color=None,
        width=None,
    ):
        super().__init__()

        self.label = label
        self.value = value
        self.disabled = disabled
        self.fill_color = fill_color
        self.check_color = check_color
        self.width = width

        self.scale = 1.0
        self.tooltip = None
