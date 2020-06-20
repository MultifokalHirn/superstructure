from .form import LogischeForm


class Begriff(LogischeForm):
    """probably not the perfect name, what is meant is a singular Thing of any sort; \
    important: a Begriff is always a _of_ some thing and a thing of a Bewusstsein.
    thus begriff.aufhebung is always just what is true for the Bewusstsein, not 'objectively'\
    objective reality is a spook"""

    @classmethod
    def allgemein(cls):
        obj = Begriff.__new__(Begriff)  # Does not call __init__
        super(
            Begriff, obj
        ).__init__()  # Don't forget to call any polymorphic base class initializers
        obj._name = f"Pure{type(obj).__name__}"
        obj._is_pure = True
        obj._aufhebung = None
        obj._negation = None
        obj._allgemeinheit = None

        return obj

    def __init__(
        self,
        name=None,
        aufhebung=None,
        allgemeinheit=None,
        negation=None,
        *args,
        **kwargs,
    ):
        self._is_pure = False
        if name is not None:
            self._name = name
        self._aufhebung = None
        self._negation = None
        self._allgemeinheit = None
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
    def is_pure(self):
        return self._is_pure

    @property
    def position(self):
        return self

    @property
    def negation(self):
        # if self.is_pure:
        #     return type(self._negation).allgemein()
        return self._negation

    @negation.setter
    def negation(self, begriff):
        "setting"
        self._negation = begriff

    @property
    def aufhebung(self):
        return self._aufhebung

    @aufhebung.setter
    def aufhebung(self, begriff):
        "setting"
        self._aufhebung = begriff

    @property
    def allgemeinheit(self):
        if self._allgemeinheit is None and not self.is_pure:
            self._allgemeinheit = type(self).allgemein()
        return self._allgemeinheit

    @allgemeinheit.setter
    def allgemeinheit(self, begriff):
        "setting"
        if not isinstance(begriff, Begriff):
            raise TypeError(
                f"Can only set Begriffe as Allgemeinheit, got {type(begriff)} ({begriff})"
            )
        self._allgemeinheit = begriff

    @property
    def related(self):
        return [
            begriff
            for begriff in {
                self.position,
                self.negation,
                self.aufhebung,
                self.allgemeinheit,
            }
            if begriff not in [self, None]
        ]


class Unknown(LogischeForm):
    """polar opposite of a Begriff"""

    def __init__(self):
        self._name = "Unknown"

    @property
    def name(self):
        return self._name

    @property
    def is_pure(self):
        return True

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
        return self

    @property
    def related(self):
        return set()

    def __eq__(self, other):
        """Overrides the LogischeForm implementation"""
        return isinstance(other, type(self))

    def __repr__(self):
        """Overrides the LogischeForm implementation"""
        return f"<{self.structure}>"


class Relation(Begriff):
    """Relation between Begriffe"""

    @classmethod
    def allgemein(cls):
        obj = Begriff.__new__(Begriff)  # Does not call __init__
        super(
            Begriff, obj
        ).__init__()  # Don't forget to call any polymorphic base class initializers
        obj._is_pure = True
        obj._name = f"Pure{cls.__name__}"
        obj._aufhebung = None
        obj._negation = None
        obj._allgemeinheit = None
        return obj

    def __init__(self, nodes=2, criterium=None, is_directed=True, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if nodes == 0:
            raise ValueError("Relation needs to have at least one node")
        self._nodes = nodes  # number of begriffe for relation
        self._is_directed = is_directed
        if criterium is None:
            raise ValueError(
                f"Trying to define relation {kwargs.get('name', 'UNKNOWN')} without criterium."
            )
        self._criterium = criterium  # function

    def criterium(self, *args, **kwargs):
        result = self._criterium(*args, **kwargs)
        if self.is_directed:
            return result
        else:
            args_reverse = args[::-1]
            return result and self._criterium(*args_reverse, **kwargs)

    @property
    def is_directed(self):
        if self.nodes == 1:
            return False
        else:
            return self._is_directed

    @property
    def nodes(self):
        return self._nodes
