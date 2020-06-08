
from abc import ABCMeta as AllgemeineForm  # Form an sich
from abc import abstractmethod


class LogischeForm(metaclass=AllgemeineForm):
    """endliche Form, Sein an sich"""

    @property
    def name(self):
        pass

    @property
    def id(self):
        pass

    @property
    def besonderheit(self):
        pass

    @property
    def allgemeinheit(self):
        pass

    @property
    def einzelheit(self):
        pass
