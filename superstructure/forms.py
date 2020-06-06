
from abc import ABCMeta as AllgemeineForm  # Form an sich
from abc import abstractmethod


class LogischeForm(metaclass=AllgemeineForm):
    """endliche Form, Sein an sich"""

    @abstractmethod
    @property
    def name(self):
        pass

    @abstractmethod
    @property
    def besonderheit(self):
        pass

    @abstractmethod
    @property
    def allgemeinheit(self):
        pass

    @abstractmethod
    @property
    def einzelheit(self):
        pass
