import werkzeug.exceptions


class UnderConstruction(werkzeug.exceptions.HTTPException):
    code = 901
    description = "This website is still being constructed"
