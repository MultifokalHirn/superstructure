from abc import ABCMeta as AllgemeineForm  # Form an sich


class LogischeForm(metaclass=AllgemeineForm):
    """endliche Form, Sein an sich"""

    @property
    def name(self):
        pass

    @property
    def id(self):
        return self.__name__

    @property
    def negation(self):
        pass

    @property
    def aufhebung(self):
        pass

    @property
    def allgemeinheit(self):
        pass

    @property
    def einzelheit(self):
        pass
