class AppContext:
    def __init__(self):
        self._user = ""
        self._password = ""
        self._is_connected = False

    # Propiedad: user
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        if not isinstance(value, str):
            raise ValueError("El usuario debe ser una cadena de texto.")
        self._user = value

    # Propiedad: password
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise ValueError("La contraseña debe ser una cadena de texto.")
        self._password = value

    # Propiedad: is_connected
    @property
    def is_connected(self):
        return self._is_connected

    @is_connected.setter
    def is_connected(self, value):
        if not isinstance(value, bool):
            raise ValueError("El estado de conexión debe ser booleano.")
        self._is_connected = value

    # Método para resetear
    def reset(self):
        self._user = ""
        self._password = ""
        self._is_connected = False

    # Método para alternar conexión
    def toggle_connection(self):
        self._is_connected = not self._is_connected

    # Propiedad de solo lectura
    @property
    def is_authenticated(self):
        return bool(self._user and self._password)
