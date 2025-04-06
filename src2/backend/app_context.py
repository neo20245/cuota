
class AppContext:
    def __init__(self):
        self._user: str = ""
        self._password: str = ""
        self._is_connected: bool = False

    # Propiedad: user
    @property
    def user(self) -> str:
        return self._user

    @user.setter
    def user(self, value: str) :
        if not isinstance(value, str):
            raise ValueError("El usuario debe ser una cadena de texto.")
        self._user = value

    # Propiedad: password
    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError("La contraseña debe ser una cadena de texto.")
        self._password = value

    # Propiedad: is_connected
    @property
    def is_connected(self) -> bool:
        return self._is_connected

    @is_connected.setter
    def is_connected(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError("El estado de conexión debe ser booleano.")
        self._is_connected = value

    # Método: toggle_connection
    def toggle_connection(self) -> None:
        self._is_connected = not self._is_connected

    # Propiedad: is_authenticated (solo lectura)
    @property
    def is_authenticated(self) -> bool:
        return bool(self._user and self._password)
