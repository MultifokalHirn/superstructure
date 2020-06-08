
from .forms import LogischeForm
from uuid import uuid4


class Begriff(LogischeForm):
    def __init__(self, name=None, synonyms=[], id=None):
        if id is None:
            self._id = uuid4()
        else:
            self._id = id
        self._name = name if name else "Reiner Begriff"
        self._synonyms = synonyms if synonyms else ["Sein"]

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def synonyms(self):
        return self._synonyms

    @property
    def names(self):
        return self.synonyms + [self.name]

    @property
    def besonderheit(self):
        return self

    @property
    def allgemeinheit(self):
        return self

    @property
    def einzelheit(self):
        return self

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, type(self)):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f'<Begriff :: {self.name}>'


class Relation(Begriff):
    """Relation of 2 Begriffe"""

    def __init__(self, name, criterium, synonyms=[], is_directed=True):
        super().__init__(name=name, synonyms=synonyms)
        self._is_directed = is_directed
        self._criterium = criterium  # lambda expression with ordered arguments

    @property
    def criterium(self):
        if self._is_directed:
            return self._criterium
        else:
            # TODO copy cireterium, switch the arguments and verunde (and) them
            return self._criterium

    def __repr__(self):
        return f'<Relation :: {self.name}>'


class Allgemeinheit(Begriff):
    """allgemeine Allgemeinheit"""

    def __init__(self, name, synonyms=[], instances=[]):
        super().__init__(name=name, synonyms=synonyms)
        self._instances = instances

    @property
    def instances(self):
        # einzelnheiten
        return self._instances

    def __repr__(self):
        return f'<Allgemeinheit :: {self.name}>'


class Einzelnheit(LogischeForm):
    """allgemeine Einzelnheit an und für sich"""

    def __init__(self, name, synonyms=[], allgemeinheit=None):
        super().__init__(name=name, synonyms=synonyms)
        self._allgemeinheit = allgemeinheit

    @property
    def allgemeinheit(self):
        return self._allgemeinheit

    def set_allgemeinheit(self, x):
        self._allgemeinheit = x

    def __repr__(self):
        return f'<Einzelnheit :: {self.name}>'
