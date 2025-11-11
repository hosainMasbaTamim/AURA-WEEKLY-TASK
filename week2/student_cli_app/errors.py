# all ther errors for the cli app

class BaseError(Exception):
    # a base exception 
    pass

class DuplicateError(Exception):
    # when credential already exists
    pass