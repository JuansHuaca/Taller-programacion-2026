from typing import Callable

# Recibe un dato y una función de validación
def validate_field(value: str, rule: Callable[[str], bool], error_msg: str):
    if not rule(value):
        from .exceptions import ValidationException
        raise ValidationException(error_msg)
    return True

# --- EJEMPLOS DE USO ---
# 3 Expresssiones Lambda:
is_not_empty = lambda s: len(s.strip()) > 0
min_length_five = lambda s: len(s) >= 5
has_at_symbol = lambda s: "@" in s

# 1 Method Reference (método nativo de string):
is_alphanumeric = str.isalnum