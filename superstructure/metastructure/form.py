from abc import ABCMeta as AllgemeineForm  # Form an sich
from sys import intern


class LogischeForm(metaclass=AllgemeineForm):
    """endliche Form, Sein an sich"""

    @property
    def name(self):
        pass

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

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, type(self)) or isinstance(self, type(other)):
            return intern(self.name) is intern(other.name)
        else:
            # TODO: test this properly!! seems dangerous
            return super().__eq__(other)
            # raise ValueError(
            #             f"object comparison: {self} ({type(self)}) and {other} {type(other)} are of different types!"
            #         )
            # return False

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f"<{type(self).__name__} :: {self.name}>"
