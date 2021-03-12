class FamilyWalletException(Exception):
    pass

class InvalidInputException(FamilyWalletException):
    pass

class UnknowUserException(FamilyWalletException):
    pass
