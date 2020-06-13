from .logik import Begriff, Relation


class Identität(Relation):
    """Identität an sich"""

    def __init__(self):
        criterium = lambda a, b, geist: a == b
        super().__init__(
            nodes=2, criterium=criterium, is_directed=False, name="Identität"
        )

    def __repr__(self):
        return f"<{self.name}>"


class Allgemeinheit(Relation):
    """relation applies, if b is the Einzelheit of a"""

    def __init__(self):
        # a is einzelheit of b for geist
        criterium = lambda a, b, geist: a.einzelheit == b
        super().__init__(
            nodes=2, criterium=criterium, is_directed=True, name="Allgemeinheit"
        )

    def __repr__(self):
        return f"<{self.name}>"


class Einzelheit(Relation):
    """relation applies, if b is the Allgemeinheit of a"""

    def __init__(self):
        # a is einzelheit of b for geist
        criterium = lambda a, b, geist: a.allgemeinheit == b
        super().__init__(
            nodes=2, criterium=criterium, is_directed=True, name="Einzelheit"
        )

    def __repr__(self):
        return f"<{self.name}>"


class AnsichSein(Relation):
    """AnsichSein an sich"""

    def __init__(self):
        criterium = lambda a, geist: isinstance(a, Begriff)
        super().__init__(
            nodes=1, criterium=criterium, is_directed=False, name="AnsichSein"
        )

    @property
    def einzelheit(self):
        return "FürUnsSein"

    @property
    def aufhebung(self):
        return "Etwas"

    def __repr__(self):
        return f"<{self.name}>"


class FürUnsSein(Relation):
    """FürUnsSein an sich"""

    def __init__(self):
        # geist has a notion of a that is not Leere
        criterium = lambda a, geist: a in geist.begriffe
        super().__init__(
            nodes=1, criterium=criterium, is_directed=False, name="FürUnsSein"
        )

    @property
    def allgemeinheit(self):
        return "AnsichSein"

    @property
    def aufhebung(self):
        return "Etwas"

    def __repr__(self):
        return f"<{self.name}>"


class Etwas(Relation):
    """Etwas an sich"""

    def __init__(self):
        criterium = lambda a, geist: False  # TODO
        super().__init__(nodes=1, criterium=criterium, is_directed=False, name="Etwas")

    @property
    def aufhebung(self):
        return self  # TODO

    @property
    def allgemeinheit(self):
        return self  # TODO

    @property
    def einzelheit(self):
        return self  # TODO

    def __repr__(self):
        return f"<{self.name}>"


class Leere(Begriff):
    """the absolute absence """

    def __init__(self):
        super().__init__(name="leere")

    @property
    def aufhebung(self):
        return self  # TODO

    @property
    def allgemeinheit(self):
        return self  # TODO

    @property
    def einzelheit(self):
        return self  # TODO

    def __repr__(self):
        return f"<{self.name}>"
