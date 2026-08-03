import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AppException(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        logger.error(f"[AppException]: {message}")

class DomainException(AppException):
    pass

class EntityNotFoundException(DomainException):
    pass

class ValidationException(DomainException):
    pass