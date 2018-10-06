class ApiError(Exception):
    """There was an ambiguous error while handling your operation."""


class AuthorizeError(ApiError):
    """There was an error when authorizing your credentials."""


class UnauthorizedError(ApiError):
    """Your request is not authorized to do this action"""


class BadRequestError(ApiError):
    """HTTP 400. Your request is most likely malformed"""


class ForbiddenError(ApiError):
    """HTTP 403. Your request don't have required privileges"""


class NotFoundError(ApiError):
    """HTTP 404. Your request refers to something that does not exist"""


class QuotaLimitExceededError(ApiError):
    """HTTP 429. You exceeded your quota limits."""
