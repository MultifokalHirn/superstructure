from ..logik import Allgemeinheit, Begriff, Relation
from .utils import Singleton


class Identität(Relation):
    """Identität an sich"""

    def __init__(self):
        criterium = lambda a, b: a == b  # TODO
        super().__init__(
            name="Identität", synonyms=set(), is_directed=False, criterium=criterium
        )
        self._id = "Identität"

    def __repr__(self):
        return f"<{self.name}>"


class Leere(Begriff):
    def __init__(self):
        super().__init__(name="Leere", synonyms=set(["Die Leere"]))
        self._id = "Leere"

    @property
    def besonderheit(self):
        return self

    @property
    def allgemeinheit(self):
        return self

    @property
    def einzelheit(self):
        return self

    def __repr__(self):
        return f"<{self.name}>"


# @Singleton
class AbstrakteAllgemeinheit(Allgemeinheit):
    def __init__(self):
        super().__init__(name="Abstrakte Allgemeinheit")
        self._id = "AbstrakteAllgemeinheit"

    @property
    def besonderheit(self):
        """an sich"""
        return Begriff

    @property
    def allgemeinheit(self):
        """an sich"""
        return Allgemeinheit

    @property
    def einzelheit(self):
        """an sich"""
        return self

    def __repr__(self):
        return f"<{self.name}>"
