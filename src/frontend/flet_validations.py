
class FletValidator:
    """Clase para realizar las validaciones del formulario"""

    @staticmethod
    def validate_username(username: str) -> bool:
        if not username.isalpha():
            return False
        return True

    @staticmethod
    def validate_password(password: str) -> str:
        """Valida la contraseña"""
        if not password:
            return "La contraseña es obligatoria"
        elif len(password) < 6:
            return "La contraseña debe tener al menos 6 caracteres"
        return None  # Sin errores
