from .logik import Begriff, Relation


class Identität(Relation):
    """Identität an sich"""

    def __init__(self):
        criterium = lambda a, b, geist: a == b
        super().__init__(
            nodes=2, criterium=criterium, is_directed=False, name="Identität"
        )

    @property
    def id(self):
        return self.name

    def __repr__(self):
        return f"<{self.name}>"


class Allgemeinheit(Relation):
    """relation applies, if b is the Einzelheit of a"""

    def __init__(self):
        # a is einzelheit of b for geist
        criterium = lambda a, b, geist: a.einzelheit == b.id
        super().__init__(
            nodes=2, criterium=criterium, is_directed=True, name="Allgemeinheit"
        )

    @property
    def id(self):
        return self.name

    def __repr__(self):
        return f"<{self.name}>"


class Einzelheit(Relation):
    """relation applies, if b is the Allgemeinheit of a"""

    def __init__(self):
        # a is einzelheit of b for geist
        criterium = lambda a, b, geist: a.allgemeinheit == b.id
        super().__init__(
            nodes=2, criterium=criterium, is_directed=True, name="Einzelheit"
        )

    @property
    def id(self):
        return self.name

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
    def id(self):
        return self.name

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
        criterium = lambda a, geist: any(
            [geist.get(name) is not Leere() for name in a.names]
        )
        super().__init__(
            nodes=1, criterium=criterium, is_directed=False, name="FürUnsSein"
        )

    @property
    def id(self):
        return self.name

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
    def id(self):
        return self.name

    @property
    def aufhebung(self):
        return self.id  # TODO

    @property
    def allgemeinheit(self):
        return self.id  # TODO

    @property
    def einzelheit(self):
        return self.id  # TODO

    def __repr__(self):
        return f"<{self.name}>"


class Leere(Begriff):
    """the absolute absence """

    def __init__(self):
        super().__init__(name="leere")

    @property
    def id(self):
        return self.name

    @property
    def aufhebung(self):
        return self.id  # TODO

    @property
    def allgemeinheit(self):
        return self.id  # TODO

    @property
    def einzelheit(self):
        return self.id  # TODO

    def __repr__(self):
        return f"<{self.name}>"
