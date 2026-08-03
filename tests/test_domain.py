import pytest
from taller.domain.exceptions import EntityNotFoundException, ValidationException
from taller.domain.validators import validate_field, is_not_empty, min_length_five

def test_validation_success():
    assert validate_field("Hola Mundo", is_not_empty, "Texto vacío") == True

def test_validation_lambda_failure():
    with pytest.raises(ValidationException):
        validate_field("123", min_length_five, "Muy corto")

def test_method_reference_validation():
    assert validate_field("Usuario123", str.isalnum, "Debe ser alfanumérico") == True

def test_exception_hierarchy():
    exc = EntityNotFoundException("No existe")
    assert isinstance(exc, Exception)

def test_validation_at_symbol():
    has_at = lambda s: "@" in s
    with pytest.raises(ValidationException):
        validate_field("correo_sin_arroba", has_at, "Falta el @")
