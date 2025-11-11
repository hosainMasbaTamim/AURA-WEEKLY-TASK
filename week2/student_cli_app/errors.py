# all ther errors for the cli app

class BaseError(Exception):
    # a base exception 
    pass

class DuplicateError(Exception):
    # when credential already exists
    pass

class NotValidSession(Exception):
    # when session invalid
    pass