
# from .utils import *
from .forms import LogischeForm


def check_form(f):
    def wrapper(*args):
        potential_form = args[0]
        if potential_form is not None:
            assert(potential_form.name is not None)
            return f(*args)
    return wrapper


class Relation(LogischeForm):
    """abstraktes Verhältnissein"""

    def __init__(self, name, synonyms=set(), a=None, b=None, is_directed=True):
        super().__init__()
        self._name = name
        self._synonyms = synonyms
        self.a = a
        self.b = b
        self.is_directed = is_directed

    @property
    def name(self):
        return self._name

    @property
    def synonyms(self):
        return self._synonyms


class Allgemeinheit(LogischeForm):
    """allgemeine Allgemeinheit"""

    def __init__(self, name, synonyms=set(), instances=set()):
        super().__init__()
        self._name = name
        self._synonyms = synonyms
        self._instances = instances

    @property
    def name(self):
        return self._name

    @property
    def synonyms(self):
        return self._synonyms

    @property
    def instances(self):
        # einzelnheiten
        return self._instances


class Einzelnheit(LogischeForm):
    """allgemeine Einzelnheit an und für sich"""

    def __init__(self, name, synonyms=set(), allgemeinheit=None):
        super().__init__()
        self._name = name
        self._synonyms = synonyms
        self._allgemeinheit = allgemeinheit

    @property
    def name(self):
        return self._name

    @property
    def synonyms(self):
        return self._synonyms

    @property
    def allgemeinheit(self):
        return self._allgemeinheit

    @check_form
    def set_allgemeinheit(self, x):
        self._allgemeinheit = x
