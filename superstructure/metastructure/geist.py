from collections.abc import Iterable

from dotdict import DotDict
from sortedcontainers import SortedSet, SortedDict

from .grundbegriffe import (
    Allgemeinheit,
    AnUndFürSichSein,
    AnsichSein,
    Aufhebung,
    Einzelheit,
    Etwas,
    FürSichSein,
    FürUnsSein,
    Grundbegriff,
    Identität,
    Leere,
    Negation,
    Selbstidentität,
)
from .logik import Begriff, Relation, Unknown


class Bewusstsein(Begriff):
    def __init__(
        self,
        begriffe=SortedSet(),
        vocabulary=SortedDict(),
        learn_grundbegriffe=True,
        verbose=False,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        # print("kwargs")
        # print(kwargs)
        self.state = "coherent"  # should become singleton
        self._begriffe = begriffe
        self._vocabulary = vocabulary  # {name: begriff}
        self.verbose = verbose
        if learn_grundbegriffe:
            self.learn_grundbegriffe()

    @property
    def begriffe(self):
        return self._begriffe

    @property
    def vocabulary(self):
        return self._vocabulary

    @property
    def itself(self):
        return self.get(self.name).begriff

    def get(self, info):
        """Bewusstsein returns their begriff of/in info in the form of DotDict(name=name, begriff=begriff)
        """
        if isinstance(info, str):
            begriff = self.vocabulary.get(info, Unknown())
            if begriff is None or isinstance(begriff, Forgotten):
                if self.verbose:
                    self.say(f"Heard of {info} but don't remember...")
                begriff = Unknown()
            return DotDict(name=info, begriff=begriff)
        elif isinstance(info, Iterable):
            return [self.get(name) for name in info]
        else:
            raise TypeError(
                f"{self.structure}.get({info}): {info} should be str or Iterable, but is {type(info)}!"
            )

    def knows(self, begriff):
        if begriff in [Forgotten(), Unknown()]:
            return False
        else:
            return begriff in self.begriffe

    def learn(self, name, begriff, force=False):
        if begriff in self.begriffe:
            if self.verbose:
                self.say(f"I already know {begriff}.")
            if name not in self.vocabulary:
                self._update(name, begriff, force=force)
        else:
            self.begriffe.add(begriff)
            self._update(begriff.name, begriff, force=force)
            if begriff.name != name:
                self._update(name, begriff, force=force)

    def handle(self, name, begriff):
        # if begriffs of information can be added to known begriffe without raising an "incoherent" state,
        if begriff in self.begriffe:
            self._update(name=name, begriff=begriff)
        subjective_begriff = self.get(name).begriff
        if begriff != subjective_begriff:
            if name in self.vocabulary and self.knows(subjective_begriff):
                self.say(f"{name} is not {begriff}, it is {subjective_begriff}!")
            else:
                if self.can_accept(begriff):
                    self.learn(name=name, begriff=begriff, force=True)
                else:
                    if self.verbose:
                        self.say(f"{begriff} is not compatible with what I know!")

    def _update(self, name, begriff, force=False):
        # update a name in vocabulary
        if begriff not in self.begriffe:
            raise ValueError(
                f"Trying to update the word {name} to mean {begriff}, which {self} does not know "
            )
        else:
            # case begriff is known
            if (
                force
                or (name not in self.vocabulary)
                or self.get(name).content == Forgotten()
            ):
                self._vocabulary[name] = begriff

    def forget(self, name):
        if name not in self.vocabulary:
            raise ValueError(f"Trying to forget unknown begriff {name}")
        else:
            begriff = self._vocabulary[name]
            self._vocabulary[name] = Forgotten()
            if begriff not in self.vocabulary.values():
                self.begriffe.remove(begriff)

    def can_accept(self, begriff):
        # checks if begriff can be integrated into known begriffe, without creating incoherence
        for known_begriff in self.begriffe:
            if begriff == known_begriff:
                return True
            if (
                begriff.negation == known_begriff
                and known_begriff.negation != Unknown()
            ):
                return False
        return True

    def learn_grundbegriffe(self):
        """should fill up the Bewusstseins vocabulary with most basic Begriffe, for example a self, relations such as Identität and so on"""
        self.learn(Identität().name, Identität())
        self.learn(Selbstidentität().name, Selbstidentität())
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

    def relation_applies(self, relation, begriffe, accept_identicals=False):
        # begriffe can either be a tuple of words or Begriff objects

        if isinstance(begriffe[0], str):
            words = set(begriffe)
            begriffe = tuple(self.get(word).begriff for word in begriffe)
        else:
            words = {begriff.name for begriff in begriffe}

        if relation.nodes > len(begriffe) or len(begriffe) == 0:
            if self.verbose:
                self.say(
                    f"{relation} applies for {relation.nodes} Begriff{'e' if relation.nodes != 1 else ''}, not {len(begriffe)}."
                    f"Thus it can not apply for {begriffe}."
                )
            return False
        if relation.nodes == len(begriffe):
            args = tuple(begriffe)
            return relation.criterium(*args, geist=self)
        if accept_identicals and relation.nodes == len(words):
            begriffe_set = tuple(set(begriffe))
            if len(begriffe_set) < len(begriffe):
                return self.relation_applies(
                    relation, begriffe_set, accept_identicals=accept_identicals
                )

        return False

    def determine_relations(self, *args, accept_identicals=False):
        """yield relations the Bewusstsein thinks exist between a and b"""
        for relation in self.known_relations:
            if self.relation_applies(
                relation, begriffe=args, accept_identicals=accept_identicals
            ):
                yield relation

    def reflect(self):
        """go through set of things that should apply if self is sane"""
        if type(self.itself) not in self.__class__.__bases__:
            raise ValueError(
                f"BROKEN VIEW ON SELF {self.itself} is not one of {self.__class__.__bases__}"
            )

    def say(self, stuff):
        if isinstance(stuff, str):
            print(f'  {self.name}: "{stuff}"')
        elif isinstance(stuff, list):
            for sentence in stuff:
                self.say(sentence)
            print("")
        else:
            raise ValueError(
                f"{self.structure}.say() only with str or list, not {type(stuff)}. (got {stuff})"
            )

    def summarize(self, omit_grundbegriffe: bool = True):
        """say out all knowledge, only for testing"""
        self.introduce()
        for begriff in self.begriffe:
            if omit_grundbegriffe and isinstance(begriff, Grundbegriff):
                continue
            self.say_knowledge_on(begriff)
        print("")

    def say_knowledge_on(self, begriff):
        names = self.get_names(begriff)
        self.say(f"I know {begriff} as {' and '.join([str(n) for n in names])}.")

    def get_names(self, begriff):
        names = []
        for k, v in self.vocabulary.items():
            if v == begriff:
                names.append(k)
        return names

    def introduce(self):
        self.say(
            f"Hello, I am a {self.itself.structure} named {self.itself.name}, but to you I am {self}."
        )

    def __repr__(self):
        if self.verbose:
            size = len(self.vocabulary)
            return f"<{self.structure} '{self.name}' - knows {size} words and itself as {self.itself}>"
        else:
            return f"<{self.structure} '{self.name}'>"


class Selbstbewusstsein(Bewusstsein):
    def __init__(self, *args, **kwargs):
        itself = Bewusstsein(name=kwargs["name"])
        kwargs["begriffe"] = SortedSet([itself])
        kwargs["vocabulary"] = {itself.name: itself}
        super().__init__(*args, **kwargs)
        if self.verbose:
            self.introduce()


class Forgotten(Unknown):
    def __init__(self):
        self._name = "Forgotten"

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, type(self)) or isinstance(self, type(other)):
            return True
        else:
            # TODO: test this properly!! seems dangerous
            return super().__eq__(other)
