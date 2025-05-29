from enum import Enum
from http import HTTPStatus


class ResponseCodeEnum(Enum):
    """
    Enum for the response codes.
    """
    SUCCESS = (0, "Success", HTTPStatus.OK)
    TRANSLATION_NOT_FOUND = (404, "Translation Not Found", HTTPStatus.NOT_FOUND)
    TRANSLATION_FILE_NOT_FOUND = (405, "Translation File", HTTPStatus.NOT_FOUND)
    INTERNAL_ERROR = (500, "Internal Server Error", HTTPStatus.INTERNAL_SERVER_ERROR)

    def __init__(self, code: int,
                 message: str,
                 http_status_code: HTTPStatus):
        self.code = code
        self.message = message
        self.http_status_code = http_status_code

    @classmethod
    def get_by_code(cls, code: int):
        """Return the enum member by its code, or None if not found."""
        for member in cls:
            if member.code == code:
                return member
        return None
