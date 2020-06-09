
from .forms import LogischeForm
from uuid import uuid4


class Begriff(LogischeForm):
    """probably not the perfect term, what is meant is a singular Thing of any sort; important: a Begriff is always a _of_ some thing and a thing of a Bewusstsein. thus begriff.besonderheit is always just what is true for the Bewusstseinm not 'objectively', which does not exist"""

    def __init__(self, name=None, synonyms=[], besonderheit_id=None, allgemeinheit_id=None, einzelheit_id=None):
        self._id = uuid4()
        self._name = name
        self._synonyms = synonyms
        self._besonderheit = LogischeForm.id
        self._allgemeinheit = LogischeForm.id
        self._einzelheit = self._id
        self.besonderheit = besonderheit_id
        self.allgemeinheit = allgemeinheit_id
        self.einzelheit = einzelheit_id

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name.lower()

    @property
    def synonyms(self):
        return [s.lower() for s in self._synonyms]

    @property
    def names(self):
        return self.synonyms + [self.name]

    @property
    def besonderheit(self):
        return self._besonderheit

    @property
    def allgemeinheit(self):
        try:
            return self._allgemeinheit
        except BaseException:
            return self.__class__.id

    @property
    def einzelheit(self):
        return self._einzelheit

    @allgemeinheit.setter
    def allgemeinheit(self, value):
        'setting'
        self._allgemeinheit = value

    @besonderheit.setter
    def besonderheit(self, value):
        'setting'
        self._besonderheit = value

    @einzelheit.setter
    def einzelheit(self, value):
        'setting'
        self._einzelheit = value

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, type(self)):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f'<Begriff :: {self.name}>'


class Unknown(LogischeForm):
    """polar opposite of a Begriff"""

    def __init__(self):
        self._name = "Unknown"

    @property
    def id(self):
        return self.name

    @property
    def name(self):
        return self._name.lower()

    @property
    def synonyms(self):
        return []

    @property
    def names(self):
        return [self.name]

    @property
    def besonderheit(self):
        return self.id

    @property
    def allgemeinheit(self):
        return self.id

    @property
    def einzelheit(self):
        return self.id

    def __eq__(self, other):
        """Overrides the default implementation"""
        return isinstance(other, type(self))

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"<{self.name}>"


class Relation(Begriff):
    """Relation between Begriffe"""

    def __init__(self, nodes=2, criterium=None, is_directed=True, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if nodes == 0:
            raise ValueError("Relation needs to have at least one node")
        self._nodes = nodes  # number of begriffe for relation
        self._is_directed = is_directed
        self._criterium = criterium  # lambda expression with ordered arguments

    @property
    def criterium(self):
        if self.is_directed:
            return self._criterium
        else:
            # TODO copy criterium, switch the arguments and ver-unde (and) them
            return self._criterium

    @property
    def is_directed(self):
        if self.nodes == 1:
            return False
        else:
            return self._is_directed

    @property
    def nodes(self):
        return self._nodes

    def __repr__(self):
        return f'<Relation :: {self.name}>'
