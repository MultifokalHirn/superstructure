from ..logik import Allgemeinheit, LogischeForm, Relation
from .utils import Singleton


@Singleton
class Leere(LogischeForm):
    def __init__(self):
        self._name = "Leere"
        self._synonyms = ["Die Leere"]

    @property
    def name(self):
        return self._name

    @property
    def synonyms(self):
        return self._synonyms

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
        return f'<{self._name}>'


@Singleton
class ReinerBegriff(LogischeForm):
    def __init__(self):
        self._name = "Reiner Begriff"
        self._synonyms = ["Der reine Begriff", "Sein"]

    @property
    def name(self):
        return self._name

    @property
    def synonyms(self):
        return self._synonyms

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
        return f'<Sein>'


@Singleton
class AbstrakteAllgemeinheit(Allgemeinheit):
    def __init__(self):
        self._name = "Abstrakte Allgemeinheit"

    @property
    def name(self):
        """an sich"""
        return self._name

    @property
    def synonyms(self):
        """an sich"""
        return set()

    @property
    def besonderheit(self):
        """an sich"""
        return LogischeForm

    @property
    def allgemeinheit(self):
        """an sich"""
        return Allgemeinheit

    @property
    def einzelheit(self):
        """an sich"""
        return self

    def __repr__(self):
        return f'<{self._name}>'


@Singleton
class Identität(Relation):
    def __init__(self):
        self._name = "Identität"

    @property
    def name(self):
        """an sich"""
        return self._name

    @property
    def synonyms(self):
        """an sich"""
        return set()

    @property
    def a(self):
        return self

    @property
    def b(self):
        return self

    @property
    def besonderheit(self):
        """an sich"""
        return self

    @property
    def allgemeinheit(self):
        """an sich"""
        return Relation

    @property
    def einzelheit(self):
        """an sich"""
        return Leere

    def __repr__(self):
        return f'<{self._name}>'
