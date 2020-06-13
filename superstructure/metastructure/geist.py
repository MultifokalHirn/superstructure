from collections.abc import Iterable
from dotdict import DotDict

from .grundbegriffe import Allgemeinheit, AnsichSein, Einzelheit, FürUnsSein, Identität
from .logik import Relation, Unknown
from .form import LogischeForm


class Geist(LogischeForm):
    def __init__(
        self, name=None, aufhebung=None, allgemeinheit=None, einzelheit=None,
    ):
        self._name = name
        self._aufhebung = None
        self._negation = None
        self._allgemeinheit = None
        self._einzelheit = None
        if einzelheit is not None and allgemeinheit is not None:
            raise ValueError()
        if aufhebung is not None:
            self.aufhebung = aufhebung
        if allgemeinheit is not None:
            self.allgemeinheit = allgemeinheit
        if einzelheit is not None:
            self.einzelheit = einzelheit

    @property
    def name(self):
        return self._name

    @property
    def aufhebung(self):
        return self._aufhebung

    @property
    def negation(self):
        return self._negation

    @property
    def allgemeinheit(self):
        return self._allgemeinheit

    @property
    def einzelheit(self):
        return self._einzelheit

    @allgemeinheit.setter
    def allgemeinheit(self, value):
        "setting"
        self._allgemeinheit = value

    @aufhebung.setter
    def aufhebung(self, value):
        "setting"
        self._aufhebung = value

    @einzelheit.setter
    def einzelheit(self, value):
        "setting"
        self._einzelheit = value

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, type(self)):
            return self.name == other.name
        return False

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f"<Geist :: {self.name}>"


class Bewusstsein(Geist):
    def __init__(self, begriffe={}, verbose=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state = "coherent"  # should become singleton
        itself = Geist(name="self")
        self._begriffe = set([itself])
        self._vocabulary = {"self": itself}  # {name: begriff}
        self.verbose = verbose
        if len(begriffe) == 0:
            self.learn_grundbegriffe()
        if self.verbose:
            self.say("Nani?")  # insert witty introduction here

    @property
    def begriffe(self):
        return self._begriffe

    @property
    def vocabulary(self):
        return self._vocabulary

    @property
    def itself(self):
        return self.get("self")

    def get(self, info):
        """Bewusstsein returns their Begriff(e) of/in {info}:
        {name: begriff}
        """
        if isinstance(info, str):
            # case: info is a name
            begriff = self.vocabulary.get(info, Unknown())
            return DotDict(name=info, content=begriff)
        elif isinstance(info, Iterable):
            # case: info is a list of names
            return [self.get(name) for name in info]
        else:
            raise TypeError(
                f"geist :: Bewusstsein.get(a): a should be str or Iterable, got {type(info)}! ({info})"
            )

    def learn(self, name, begriff):
        if begriff in self.begriffe:
            if self.verbose:
                self.say(f"I already know {begriff}.")
            if self.get(name) != begriff:
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
                self.say(f"a {name} is not a {begriff}!!")

    def _update(self, name, begriff):
        # update a name in vocabulary
        if begriff not in self.begriffe:
            raise ValueError(
                f"Trying to update the word {name} to mean {begriff}, which {self.name} does not know "
            )
        else:
            self._vocabulary[name] = begriff

    def forget(self, name):
        if name not in self.vocabulary:
            raise ValueError(f"Trying to forget unknown begriff {name}")
        else:
            self._vocabulary[name] = None

    def learn_grundbegriffe(self):
        """should fill up the Bewusstseins vocabulary with most basic Begriffe, for example a self, relations such as Identität and so on"""
        self.learn(Identität().name, Identität())
        self.learn(Allgemeinheit().name, Allgemeinheit())
        self.learn(Einzelheit().name, Einzelheit())
        self.learn(AnsichSein().name, AnsichSein())
        self.learn(FürUnsSein().name, FürUnsSein())

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

    def relation_applies(self, relation, begriffe=[]):
        if relation.nodes != len(begriffe):
            begriffe_set = set(begriffe)
            if len(begriffe_set) < len(begriffe):
                return self.relation_applies(relation, begriffe_set)
            if self.verbose:
                self.say(
                    f"{relation} can only apply for {relation.nodes} Begriff{'e' if relation.nodes != 1 else ''}, "
                    f"thus it can not apply for {self.get(begriffe)}"
                )
            return False
        else:
            args = tuple(begriffe)
            return relation.criterium(*args, self)

    def determine_relations(self, *args):
        """yield relations the Bewusstsein thinks exist between a and b"""
        for relation in self.known_relations:
            if self.relation_applies(relation, begriffe=args):
                yield relation

    def say(self, sentence):
        if sentence:
            print(f'  {self.name}: "{sentence}"')

    def spill(self):
        """say out all knowledge, only for testing"""
        for name, begriff in self.vocabulary.items():
            self.say(f"I know {name} as {begriff}")

    def __repr__(self):
        size = len(self.vocabulary)
        return f"<Bewusstsein :: {self.name} -- vocabulary of {size}>"


def is_compatible(bewusstseins_inhalt, x):
    if isinstance(x, Relation):
        for begriff in bewusstseins_inhalt:
            return isinstance(begriff)
