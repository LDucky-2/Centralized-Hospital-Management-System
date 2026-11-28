from http import HTTPStatus


class AppError(Exception):
    status_code = HTTPStatus.INTERNAL_SERVER_ERROR

    def __init__(self, message: str, code: str | None = None) -> None:
        super().__init__(message)
        self.message = message
        self.code = code


class BadRequestError(AppError):
    status_code = HTTPStatus.BAD_REQUEST


class UnauthorizedError(AppError):
    status_code = HTTPStatus.UNAUTHORIZED


class TokenReuseError(UnauthorizedError):
    def __init__(self, message: str, account_id=None) -> None:
        super().__init__(message, code="token_reuse")
        self.account_id = account_id


class ForbiddenError(AppError):
    status_code = HTTPStatus.FORBIDDEN


class NotFoundError(AppError):
    status_code = HTTPStatus.NOT_FOUND


class UnprocessableError(AppError):
    status_code = HTTPStatus.UNPROCESSABLE_ENTITY


class ConflictError(AppError):
    status_code = HTTPStatus.CONFLICT
