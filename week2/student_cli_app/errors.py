# this file holdes user defined errors

class BaseError(Exception):
    pass

class NotValidSession(BaseError):
    pass

class NotValidDepartment(BaseError):
    pass
