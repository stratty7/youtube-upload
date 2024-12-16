class OpplastException(Exception):
    """General exception class for youtube-upload"""


class VideoIDError(OpplastException):
    """Error for when Video ID is not found"""


class ExceedsCharactersAllowed(OpplastException):
    """Exception for when given string is too long"""
