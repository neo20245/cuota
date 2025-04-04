class TitleBar:
    def build_ui(self):
        return ft.Container(
            content=ft.Row(
                [
                    ft.PopupMenuButton(
                        items=[
                            ft.PopupMenuItem(text="Item 1"),
                            ft.PopupMenuItem(
                                icon=ft.Icons.POWER_INPUT, text="Check power"
                            ),
                        ],
                        tooltip="Menú",
                        icon=ft.Icons.MENU,
                    ),
                    ft.WindowDragArea(
                        ft.Container(content=CustomText("           Cuota Uci       "))
                    ),
                    ft.Container(
                        content=ft.Row(
                            [
                                CustomIconButton(
                                    icon=ft.Icons.MINIMIZE
                                ),  # Botón de configuración
                                CustomIconButton(
                                    icon=ft.Icons.CLOSE
                                ),  # Botón de información
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            # Alineación de los botones a la derecha
                        )
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  # Espacio entre los elementos
            ),
            bgcolor="#050944",
            width=350,
            height=30,
        )
