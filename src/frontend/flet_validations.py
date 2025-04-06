
class FletValidator:
    """Clase para realizar las validaciones del formulario"""

    @staticmethod
    def validate_username(username: str) -> bool:
        if not username.isalpha():
            return False
        return True

    @staticmethod
    def validate_password(password: str) -> bool:
        return len(password) >= 8                              # Mínimo 8 caracteres
                                    # No puede contener espacios
