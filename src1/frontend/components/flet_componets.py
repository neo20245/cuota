import flet as ft


class CustomContainerPage(ft.Container):
    def __init__(self, content, **kargs):
        super().__init__()

        self.content = content
        self.bgcolor = ft.Colors.BLACK54
        self.alignment = ft.alignment.center
        self.padding = 4
        self.margin = 0


# Clase personalizada para contenedores
class CustomContainer(ft.Container):
    def __init__(self, content, **kargs):
        super().__init__()

        self.content = content
        self.bgcolor = ft.Colors.WHITE  # Contenido que se mostrará en el contenedor
        self.alignment = ft.alignment.center
        self.padding = 4
        self.margin = 0

        # Espacio alrededor del contenedor


class CustomIconButton(ft.IconButton):
    def __init__(self, icon):
        super().__init__()
        self.icon = icon
        self.icon_color = ft.Colors.WHITE
        self.icon_size = 20


# Clase personalizada para texto
class CustomText(ft.Text):
    def __init__(self, value, **kwargs):
        super().__init__()

        self.value = value
        self.color = ft.Colors.WHITE  # Color del texto
        self.size = 16  # Tamaño del texto
        self.weight = ft.FontWeight.NORMAL

        # Peso de la fuente


class CustomTextField(ft.TextField):
    def __init__(
        self,
        label="",
        width=200,
        height=40,
        icon=None,
        prefix_icon=None,
        suffix_icon=None,
        password=False,
        hint_text=None,
        **kwargs,
    ):
        # Inicialización mejorada para asegurar que funcione correctamente con todos los parámetros de Flet
        super().__init__()
        self.width = width
        self.height = height
        self.label = label
        self.color = ft.Colors.BLACK54


class CustomCheckBox(ft.Checkbox):
    def __init__(self, label="", value=False, **kwargs):
        super().__init__()

        self.label = label
        self.value = value
        self.fill_color = ft.colors.BLUE
        self.check_color = ft.colors.WHITE
        self.scale = 1.0
        self.tooltip = None

        # Apply any additional kwargs
