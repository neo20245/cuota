import flet as ft

def create_titlebar(page: ft.Page):
    page.padding=0
    titlebar = ft.Container(
        content=ft.Row(
            [
                # Área de arrastre con el título centrado
                ft.WindowDragArea(
                    ft.Container(
                        content=ft.Text(
                            "Cuota UCI",
                            text_align=ft.TextAlign.CENTER,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.WHITE,

                        ),
                        alignment=ft.alignment.center,
                        bgcolor=ft.Colors.INDIGO_500,
                        expand=True,
                        margin=0,
                        padding=0

                    ),
                    expand=True,

                ),
                # Botones minimizar y cerrar
                ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.icons.MINIMIZE,
                            icon_color=ft.Colors.WHITE,
                            icon_size=20,
                            tooltip="Minimizar",
                            on_click=lambda _: page.window.minimize(),
                        ),
                        ft.IconButton(
                            icon=ft.icons.CLOSE,
                            icon_color=ft.Colors.WHITE,
                            icon_size=20,
                            tooltip="Cerrar",
                            on_click=lambda _: page.window.close(),
                        ),
                    ],
                    spacing=0,
                    alignment=ft.MainAxisAlignment.END,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                )
            ],

            spacing=0,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor=ft.colors.INDIGO_500,  # Color general de la barra de título
        height=40,
        padding=0,
        margin=0
    )

    return titlebar
