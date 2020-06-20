# import weakref
from abc import ABCMeta as AllgemeineForm  # Form an sich
from sys import intern


class LogischeForm(metaclass=AllgemeineForm):
    """endliche Form, Sein an sich"""

    _instances = set()

    def __init__(self):
        # print(f"{type(self)} adding instances")
        # self._instances.add(weakref.ref(self))
        # self.is_pure = True
        return

    @property
    def structure(self):
        return type(self).__name__

    @property
    def is_pure(self):
        pass

    @property
    def name(self):
        pass

    @property
    def position(self):
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
    def related(self):
        return set()

    @classmethod
    def einzelheiten(cls):
        dead = set()
        for ref in cls._instances:
            obj = ref()
            if obj is not None:
                yield obj
            else:
                dead.add(ref)
        cls._instances -= dead

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, type(self)) or isinstance(self, type(other)):
            return (
                intern(self.name)
                is intern(other.name)
                # and self.related == other.related  # this is important
            )
        else:
            # TODO: test this properly!! seems dangerous
            return super().__eq__(other)
            # raise ValueError(
            #             f"object comparison: {self} ({type(self)}) and {other} {type(other)} are of different types!"
            #         )
            # return False

    def __hash__(self):
        return hash(self._name)

    def __lt__(self, other):
        return self.name < other.name

    # def __bool__(self):
    #     """whether this has a positive instance, is an sich"""
    #     return False

    def __repr__(self):
        return f"<{type(self).__name__} '{self.name}'>"
