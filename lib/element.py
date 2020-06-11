class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    def __set__(self, obj, value):
        pass

    def __get__(self, obj, owner):
        pass