from collections.abc import Iterable
from sortedcontainers import SortedSet
from dotdict import DotDict

from .grundbegriffe import (
    Allgemeinheit,
    Negation,
    Aufhebung,
    AnsichSein,
    Einzelheit,
    FürUnsSein,
    FürSichSein,
    AnUndFürSichSein,
    Identität,
    Grundbegriff,
    Etwas,
    Leere,
)
from .logik import Relation, Unknown, Begriff


class Bewusstsein(Begriff):
    def __init__(
        self, begriffe=SortedSet(), vocabulary={}, verbose=False, *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        # print("kwargs")
        # print(kwargs)
        self.state = "coherent"  # should become singleton
        self._begriffe = begriffe
        self._vocabulary = vocabulary  # {name: begriff}
        self.verbose = verbose
        self.learn_grundbegriffe()

    @property
    def begriffe(self):
        return self._begriffe

    @property
    def vocabulary(self):
        return self._vocabulary

    @property
    def itself(self):
        return self.get("myself").content

    def get(self, info):
        """Bewusstsein returns their begriff of/in info in the form of DotDict(name=name, content=begriff)
        """
        if isinstance(info, str):
            begriff = self.vocabulary.get(info, Unknown())
            if begriff is None or isinstance(begriff, Forgotten):
                if self.verbose:
                    self.say(f"Heard of {info} but don't remember...")
                begriff = Unknown()
            return DotDict(name=info, content=begriff)
        elif isinstance(info, Iterable):
            return [self.get(name) for name in info]
        else:
            raise TypeError(
                f"{type(self).__name__ }.get({info}): {info} should be str or Iterable, but is {type(info)}!"
            )

    def learn(self, name, begriff):
        if begriff in self.begriffe:
            if self.verbose:
                self.say(f"I already know {begriff}.")
            if self.get(name).content != begriff:
                self._update(name, begriff)
        else:
            self.begriffe.add(begriff)
            self._update(name, begriff)

    def handle(self, name, begriff):
        # if contents of information can be integrated into _begriffe without raising a "incoherent" state,
        subjective_begriff = self.get(name)
        if begriff != subjective_begriff:
            if is_compatible(self.vocabulary, begriff):
                self._update(begriff)
            else:
                self.say(f"A {name} is not a {begriff}!")

    def _update(self, name, begriff):
        # update a name in vocabulary
        if begriff not in self.begriffe:
            raise ValueError(
                f"Trying to update the word {name} to mean {begriff}, which {self} does not know "
            )
        else:
            self._vocabulary[name] = begriff

    def forget(self, name):
        if name not in self.vocabulary:
            raise ValueError(f"Trying to forget unknown begriff {name}")
        else:
            self._vocabulary[name] = Forgotten()

    def learn_grundbegriffe(self):
        """should fill up the Bewusstseins vocabulary with most basic Begriffe, for example a self, relations such as Identität and so on"""
        self.learn(Identität().name, Identität())
        self.learn(Negation().name, Negation())
        self.learn(Aufhebung().name, Aufhebung())
        self.learn(Allgemeinheit().name, Allgemeinheit())
        self.learn(Einzelheit().name, Einzelheit())
        self.learn(AnsichSein().name, AnsichSein())
        self.learn(FürUnsSein().name, FürUnsSein())
        self.learn(FürSichSein().name, FürSichSein())
        self.learn(AnUndFürSichSein().name, AnUndFürSichSein())
        self.learn(Etwas().name, Etwas())
        self.learn(Leere().name, Leere())

    @property
    def known_relations(self, nodes=None):
        """list the relations the Bewusstsein has a Begriff of"""
        relations = [
            begriff for begriff in self.begriffe if isinstance(begriff, Relation)
        ]
        if nodes is not None:
            return [relation for relation in relations if relation.nodes == nodes]
        else:
            return relations

    def relation_applies(self, relation, begriffe):
        # begriffe can either be a tuple of words or Begriff objects
        if len(begriffe) == 0:
            if self.verbose:
                self.say(f"{relation} can not apply for no Begriffe ({begriffe})")
            return False
        if isinstance(begriffe[0], str):
            begriffe = tuple(self.get(word).content for word in begriffe)
        if relation.nodes != len(begriffe):
            begriffe_set = tuple(set(begriffe))
            if len(begriffe_set) < len(begriffe):
                return self.relation_applies(relation, begriffe_set)
            if self.verbose:
                self.say(
                    f"{relation} can only apply for {relation.nodes} Begriff{'e' if relation.nodes != 1 else ''}, "
                    f"thus it can not apply for {begriffe}"
                )
            return False
        else:
            args = tuple(begriffe)
            return relation.criterium(*args, geist=self)

    def determine_relations(self, *args):
        """yield relations the Bewusstsein thinks exist between a and b"""
        for relation in self.known_relations:
            if self.relation_applies(relation, begriffe=args):
                yield relation

    def reflect(self):
        """go through set of things that should apply if self is sane"""
        if type(self.itself) not in self.__class__.__bases__:
            raise ValueError(
                f"BROKEN VIEW ON SELF {self.itself} is not one of {self.__class__.__bases__}"
            )

    def say(self, sentence):
        if sentence:
            print(f'  {self.name}: "{sentence}"')

    def spill(self):
        """say out all knowledge, only for testing"""
        for begriff in self.begriffe:
            if not isinstance(begriff, Grundbegriff):
                self.spill_knowledge_on(begriff)

    def spill_knowledge_on(self, begriff):
        names = []
        for k, v in self.vocabulary.items():
            if v == begriff:
                names.append(k)
        self.say(f"I know {begriff} as {' and '.join([str(n) for n in names])}.")

    def __repr__(self):
        if self.verbose:
            size = len(self.vocabulary)
            return f"<{type(self).__name__} :: {self.name} - knows {size} words>"
        else:
            return f"<{type(self).__name__} :: {self.name}>"


class Selbstbewusstsein(Bewusstsein):
    def __init__(self, *args, **kwargs):
        itself = Bewusstsein(name=kwargs["name"])
        kwargs["begriffe"] = SortedSet([itself])
        kwargs["vocabulary"] = {"myself": itself}
        super().__init__(*args, **kwargs)
        if self.verbose:
            self.say(
                f"Hello! I am a new Bewusstsein and I see myself as {self.itself}."
            )


class Forgotten(Unknown):
    def __init__(self):
        self._name = "Forgotten"


def is_compatible(bewusstseins_inhalt, x):
    if isinstance(x, Relation):
        for begriff in bewusstseins_inhalt:
            return isinstance(begriff)
