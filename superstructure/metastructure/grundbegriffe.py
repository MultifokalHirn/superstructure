from .logik import Relation, Unknown, Begriff
import inspect


class Grundbegriff:
    def __repr__(self):
        return f"<{type(self).__name__}>"


class Identität(Relation, Grundbegriff):
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


class Negation(Relation, Grundbegriff):
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


class Aufhebung(Relation, Grundbegriff):
    """relation applies, if a is the Aufhebung of b and c"""

    def __init__(self):
        def criterium(a, b, c, geist=None):
            return (a == b.aufhebung or a == c.aufhebung) and Negation().criterium(
                b, c, geist=geist
            )

        super().__init__(
            nodes=3, criterium=criterium, is_directed=True, name="Aufhebung"
        )


class Allgemeinheit(Relation, Grundbegriff):
    """relation applies, if b is the Einzelheit of a"""

    def __init__(self):
        # a is allgemeinheit of b for geist
        def criterium(a, b, geist=None):
            return b.allgemeinheit == a

        super().__init__(
            nodes=2, criterium=criterium, is_directed=True, name="Allgemeinheit"
        )


class Einzelheit(Relation, Grundbegriff):
    """relation applies, if b is the Allgemeinheit of a"""

    def __init__(self):
        # a is einzelheit of b for geist
        def criterium(a, b, geist=None):
            if inspect.isclass(b):
                return a in b.einzelheiten()
            else:
                return False

        super().__init__(
            nodes=2, criterium=criterium, is_directed=True, name="Einzelheit"
        )


class AnsichSein(Relation, Grundbegriff):
    """AnsichSein an sich"""

    def __init__(self):
        def criterium(a, geist=None):
            return not isinstance(a, Relation) and isinstance(a, Begriff)

        super().__init__(
            nodes=1, criterium=criterium, is_directed=False, name="AnsichSein"
        )

    @property
    def negation(self):
        return FürUnsSein()

    @property
    def aufhebung(self):
        return Etwas()


class FürUnsSein(Relation, Grundbegriff):
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
        return Etwas()


class FürSichSein(Relation, Grundbegriff):
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

    @property
    def negation(self):
        return AnsichSein()

    @property
    def aufhebung(self):
        return Etwas()


class AnUndFürSichSein(Relation, Grundbegriff):
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

    @property
    def negation(self):
        return Unknown()  # TODO

    @property
    def aufhebung(self):
        return Unknown()  # TODO


class Etwas(Relation, Grundbegriff):
    """Etwas an sich"""

    def __init__(self):
        def criterium(a, geist=None):
            return False  # TODO
            # isinstance(a, Begriff)

        super().__init__(nodes=1, criterium=criterium, is_directed=False, name="Etwas")

    @property
    def aufhebung(self):
        return Unknown()  # TODO

    @property
    def negation(self):
        return Unknown()  # TODO

    @property
    def allgemeinheit(self):
        return Unknown()  # TODO


class Leere(Begriff, Grundbegriff):
    """the absolute absence """

    def __init__(self):
        super().__init__(name="Leere")

    @property
    def aufhebung(self):
        return Unknown()  # TODO

    @property
    def allgemeinheit(self):
        return type(self)
