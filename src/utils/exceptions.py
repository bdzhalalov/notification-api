from starlette import status


class BaseError(Exception):
    message: str
    code: int

    def __init__(self, message: str, code: int)-> None:
        super().__init__(message)
        self.message = message
        self.code = code

    def to_dict(self)-> dict:
        return {"message": self.message, "code": self.code}


class NotFoundError(BaseError):
    def __init__(self):
        super().__init__("Not found", status.HTTP_404_NOT_FOUND)


class InvalidUpdateFieldsError(BaseError):
    def __init__(self, message: str):
        super().__init__(message, status.HTTP_422_UNPROCESSABLE_CONTENT)


class InternalServerError(BaseError):
    def __init__(self):
        super().__init__("Internal server error", status.HTTP_500_INTERNAL_SERVER_ERROR)
