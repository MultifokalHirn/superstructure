from .logik import Begriff, Relation, Unknown


class Grundbegriff:
    def __repr__(self):
        return f"<{self.structure}>"


class Identität(Grundbegriff, Relation):
    """identity"""

    def __init__(self):
        def criterium(a, b, geist=None):
            return a == b
            # TODO: variable input length *a
            # return len(set(a)) == 1

        super().__init__(
            nodes=2, criterium=criterium, is_directed=False, name="Identität"
        )

    @property
    def negation(self):
        return Negation()


class Selbstidentität(Grundbegriff, Relation):
    """selfidentity"""

    def __init__(self):
        def criterium(a, geist=None):
            return a == a

        super().__init__(
            nodes=1, criterium=criterium, is_directed=True, name="Selbstidentität"
        )

    # @property
    # def negation(self):
    #     return Negation()


class Negation(Grundbegriff, Relation):
    """relation applies, if b is the Negation of a"""

    def __init__(self):
        def criterium(a, b, geist=None):
            return a.negation == b

        super().__init__(
            nodes=2, criterium=criterium, is_directed=True, name="Negation"
        )

    @property
    def negation(self):
        return Identität()


class Aufhebung(Grundbegriff, Relation):
    """relation applies, if a is the Aufhebung of b and c"""

    def __init__(self):
        def criterium(a, b, c, geist=None):
            return (a == b.aufhebung or a == c.aufhebung) and Negation().criterium(
                b, c, geist=geist
            )

        super().__init__(
            nodes=3, criterium=criterium, is_directed=True, name="Aufhebung"
        )


class Allgemeinheit(Grundbegriff, Relation):
    """relation applies, if b is the Einzelheit of a"""

    def __init__(self):
        # a is allgemeinheit of b for geist
        def criterium(a, b, geist=None):
            return b.allgemeinheit == a

        super().__init__(
            nodes=2, criterium=criterium, is_directed=True, name="Allgemeinheit"
        )

    @property
    def negation(self):
        if self.is_pure:
            return Einzelheit.allgemein()
        else:
            return Einzelheit()


class Einzelheit(Grundbegriff, Relation):
    """relation applies, if b is the Allgemeinheit of a"""

    def __init__(self):
        # a is einzelheit of b for geist
        def criterium(a, b, geist=None):
            if b.is_pure:
                return a in b.einzelheiten()
            else:
                return a.allgemeinheit == b

        super().__init__(
            nodes=2, criterium=criterium, is_directed=True, name="Einzelheit"
        )

    @property
    def negation(self):
        if self.is_pure:
            return Allgemeinheit.allgemein()
        else:
            return Allgemeinheit()


class AnsichSein(Grundbegriff, Relation):
    """AnsichSein an sich"""

    def __init__(self):
        def criterium(a, geist=None):
            return isinstance(a, Begriff) and not isinstance(a, Relation)

        super().__init__(
            nodes=1, criterium=criterium, is_directed=False, name="AnsichSein"
        )

    @property
    def negation(self):
        return FürUnsSein()

    @property
    def aufhebung(self):
        return Etwas()


class FürUnsSein(Grundbegriff, Relation):
    """FürUnsSein an sich"""

    def __init__(self):
        # geist has a notion of a that is not Leere
        def criterium(a, geist=None):
            return a != Unknown() and a in geist.begriffe

        super().__init__(
            nodes=1, criterium=criterium, is_directed=False, name="FürUnsSein"
        )

    @property
    def negation(self):
        return AnsichSein()

    @property
    def aufhebung(self):
        if self.is_pure:
            return Etwas.allgemein()
        else:
            return Etwas()


class FürSichSein(Grundbegriff, Relation):
    """FürSichSein """

    def __init__(self):
        # geist has a notion of itself
        def criterium(a, geist=None):
            try:
                return FürUnsSein().criterium(a.itself, geist=a)
            except AttributeError:
                return False

        super().__init__(
            nodes=1, criterium=criterium, is_directed=False, name="FürSichSein"
        )

    # @property
    # def negation(self):
    #     return AnsichSein()

    # @property
    # def aufhebung(self):
    #     return Etwas()


class AnUndFürSichSein(Grundbegriff, Relation):
    """AnUndFürSichSein """

    def __init__(self):
        # geist has a notion of itself
        def criterium(a, geist=None):
            return FürSichSein().criterium(a, geist=geist) and AnsichSein().criterium(
                a, geist=geist
            )

        super().__init__(
            nodes=1, criterium=criterium, is_directed=False, name="AnUndFürSichSein"
        )

    # @property
    # def negation(self):
    #     return None  # TODO

    # @property
    # def aufhebung(self):
    #     return None  # TODO


class Etwas(Grundbegriff, Relation):
    """Etwas an sich"""

    def __init__(self):
        def criterium(a, geist=None):
            return False  # TODO
            # isinstance(a, Begriff)

        super().__init__(nodes=1, criterium=criterium, is_directed=False, name="Etwas")

    # @property
    # def aufhebung(self):
    #     return None  # TODO

    # @property
    # def negation(self):
    #     return None  # TODO

    # @property
    # def allgemeinheit(self):
    #     return None  # TODO
