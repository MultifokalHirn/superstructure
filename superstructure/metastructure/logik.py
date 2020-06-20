from .form import LogischeForm


class Begriff(LogischeForm):
    """probably not the perfect name, what is meant is a singular Thing of any sort; \
    important: a Begriff is always a _of_ some thing and a thing of a Bewusstsein.
    thus begriff.aufhebung is always just what is true for the Bewusstsein, not 'objectively'\
    objective reality is a spook"""

    def __init__(
        self, name=None, aufhebung=None, allgemeinheit=None, negation=None,
    ):
        self._name = name
        self._aufhebung = None
        self._negation = None
        self._allgemeinheit = type(self)
        if aufhebung is not None:
            self.aufhebung = aufhebung
        if allgemeinheit is not None:
            self.allgemeinheit = allgemeinheit
        if negation is not None:
            self.negation = negation
        super().__init__()

    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self

    @property
    def negation(self):
        return self._negation

    @property
    def aufhebung(self):
        return self._aufhebung

    @property
    def allgemeinheit(self):
        return self._allgemeinheit

    @negation.setter
    def negation(self, begriff):
        "setting"
        self._negation = begriff

    @aufhebung.setter
    def aufhebung(self, begriff):
        "setting"
        self._aufhebung = begriff

    @allgemeinheit.setter
    def allgemeinheit(self, begriff):
        "setting"
        self._allgemeinheit = begriff


class Unknown(LogischeForm):
    """polar opposite of a Begriff"""

    def __init__(self):
        self._name = "Unknown"

    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self

    @property
    def negation(self):
        return self

    @property
    def aufhebung(self):
        return self

    @property
    def allgemeinheit(self):
        return type(self)

    def __eq__(self, other):
        """Overrides the LogischeForm implementation"""
        return isinstance(other, type(self))

    def __repr__(self):
        """Overrides the LogischeForm implementation"""
        return f"<{self.structure}>"


class Relation(Begriff):
    """Relation between Begriffe"""

    def __init__(self, nodes=2, criterium=None, is_directed=True, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if nodes == 0:
            raise ValueError("Relation needs to have at least one node")
        self._nodes = nodes  # number of begriffe for relation
        self._is_directed = is_directed
        if criterium is None:
            raise ValueError(f"Trying to define relation {self} without criterium.")
        self._criterium = criterium  # function

    def criterium(self, *args, **kwargs):
        if self.is_directed:
            return self._criterium(*args, **kwargs)
        else:
            # TODO copy criterium, switch the arguments and ver-unde (and) them
            return self._criterium(*args, **kwargs) and self._criterium(
                *args[::-1], **kwargs
            )

    @property
    def is_directed(self):
        if self.nodes == 1:
            return False
        else:
            return self._is_directed

    @property
    def nodes(self):
        return self._nodes
