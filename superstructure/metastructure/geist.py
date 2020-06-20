from collections.abc import Iterable
from copy import copy
from dotdict import DotDict
from sortedcontainers import SortedDict, SortedSet

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
        self.is_coherent = True
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
        if begriff in [Unknown(), Forgotten(), None]:
            return False
        if not isinstance(begriff, Begriff):
            raise TypeError(f"Can only know Begriffe, got {type(begriff)} ({begriff})")
        if begriff in [Forgotten(), Unknown()]:
            return False
        else:
            return begriff in self.begriffe

    def patch_begriffe(decorated):  # noqa
        def magic(self, *args, **kwargs):
            should_patch = decorated(self, *args, **kwargs)
            if not should_patch:
                return
            # self.say("patching!!")
            is_coherent = True
            # check if pureBegriffe exist of which come information can be generated through their particulars
            begriffe = copy(self._begriffe)
            for purebegriff in [begriff for begriff in begriffe if begriff.is_pure]:
                if not self.knows(purebegriff):
                    continue
                if not self.knows(purebegriff.negation):
                    for begriff in [
                        begriff for begriff in self.begriffe if not begriff.is_pure
                    ]:
                        if begriff.allgemeinheit.name == purebegriff.name:
                            if (
                                self.knows(begriff.negation)
                                and not begriff.negation.is_pure
                            ):
                                patched_begriff = copy(purebegriff)
                                new_negation = begriff.negation.allgemein()
                                patched_begriff._negation = new_negation
                                new_negation._negation = patched_begriff
                                if self.knows(new_negation):
                                    self._begriffe.remove(new_negation)
                                self._begriffe.add(new_negation)
                                self._begriffe.remove(purebegriff)
                                self._begriffe.add(patched_begriff)
                                self._vocabulary[patched_begriff.name] = patched_begriff
                                self._vocabulary[new_negation.name] = new_negation
            begriffe = copy(self._begriffe)
            for begriff in begriffe:
                if not self.knows(begriff):
                    continue
                if self.knows(begriff.negation):
                    if begriff.negation.negation != begriff:
                        if begriff.negation.negation is None:
                            patched_begriff = copy(begriff.negation)
                            patched_begriff.negation = begriff
                            self._begriffe.remove(begriff.negation)
                            self._begriffe.add(patched_begriff)
                            self._vocabulary[patched_begriff.name] = patched_begriff
                        else:
                            is_coherent = False
            # check if begriffe reference unknown begriffe
            begriffe = copy(self._begriffe)
            for begriff in begriffe:
                if not self.knows(begriff):
                    continue
                if begriff.negation not in [
                    Unknown(),
                    Forgotten(),
                    None,
                ] and not self.knows(begriff.negation):
                    patched_begriff = copy(begriff)
                    patched_begriff._negation = None
                    self._begriffe.remove(begriff)
                    self._begriffe.add(patched_begriff)
                    self._vocabulary[patched_begriff.name] = patched_begriff
            self.is_coherent = is_coherent

        return magic

    @patch_begriffe
    def learn(self, name, begriff, force=True) -> bool:
        if not isinstance(begriff, Begriff):
            raise TypeError(f"Can only learn Begriffe, got {type(begriff)} ({begriff})")
        if begriff in self.begriffe:
            if self.verbose:
                self.say(f"I already know {begriff}.")
                # self.say(f"update_meaning of {name} to {begriff}.")
            self.update_meaning(name, begriff, force=force)
        else:
            for related_begriff in begriff.related:
                if related_begriff not in self.begriffe:
                    if force and (
                        isinstance(related_begriff, Begriff) or related_begriff.is_pure
                    ):
                        self._begriffe.add(related_begriff)
                        self.update_meaning(related_begriff.name, related_begriff)
                    else:
                        raise ValueError(
                            f"Trying to learn {begriff} with unknown related Begriff {related_begriff}!"
                        )
            self._begriffe.add(begriff)
            self.update_meaning(begriff.name, begriff, force=force)
            if begriff.name != name:
                self.update_meaning(name, begriff, force=force)
            if self.verbose:
                self.say(f"I just learned {begriff} as {name}!")
            return True

    @patch_begriffe
    def update_begriff(self, begriff, force=False) -> bool:
        for known_begriff in self.begriffe:
            if known_begriff.name == begriff.name:
                self._begriffe.remove(known_begriff)
                self._begriffe.add(begriff)
                self.update_meaning(known_begriff.name, begriff)
                return True
        raise ValueError(f"Trying to update unknown Begriff {begriff}. ")

    def handle(self, name, begriff):
        # if begriffs of information can be added to known begriffe without raising an "incoherent" state,
        if begriff in self.begriffe:
            self.update_meaning(name=name, begriff=begriff)
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

    @patch_begriffe
    def update_meaning(self, name, begriff, force=False) -> bool:
        # update a name in vocabulary
        if begriff not in self.begriffe:
            raise ValueError(
                f"Trying to update the word {name} to mean {begriff}, which {self} does not know."
            )
        else:
            # case begriff is known
            if (
                force
                or (name not in self.vocabulary)
                or self.get(name).content == Forgotten()
            ):
                self._vocabulary[name] = begriff
                return True

    @patch_begriffe
    def forget(self, name):
        if name not in self.vocabulary:
            raise ValueError(f"Trying to forget unknown begriff {name}")
        else:
            begriff = self._vocabulary[name]
            self._vocabulary[name] = Forgotten()
            if begriff not in self.vocabulary.values():
                self.begriffe.remove(begriff)
                return True

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
        return True  # TODO needs to default to False, but logic is missing

    def learn_grundbegriffe(self):
        """should fill up the Bewusstseins vocabulary with most basic Begriffe, for example a self, relations such as Identität and so on"""
        reiner_begriff = Begriff.allgemein()
        self.learn(reiner_begriff.name, reiner_begriff, force=True)
        self.learn(Identität().name, Identität(), force=True)
        self.learn(Selbstidentität().name, Selbstidentität(), force=True)
        self.learn(Negation().name, Negation(), force=True)
        self.learn(Aufhebung().name, Aufhebung(), force=True)
        self.learn(Allgemeinheit().name, Allgemeinheit(), force=True)
        self.learn(Einzelheit().name, Einzelheit(), force=True)
        self.learn(AnsichSein().name, AnsichSein(), force=True)
        self.learn(FürUnsSein().name, FürUnsSein(), force=True)
        self.learn(FürSichSein().name, FürSichSein(), force=True)
        self.learn(AnUndFürSichSein().name, AnUndFürSichSein(), force=True)
        self.learn(Etwas().name, Etwas(), force=True)
        self.learn("Leere", Begriff(name="Leere"), force=True)

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
        for relation in self.known_relations():
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
            raise TypeError(
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

    # def __repr__(self):
    #     if self.verbose:
    #         size = len(self.vocabulary)
    #         return f"<{self.structure} '{self.name}' - knows {size} words and itself as {self.itself}>"
    #     else:
    #         return f"<{self.structure} '{self.name}'>"


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
        super().__init__()
        self._name = "Forgotten"

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, type(self)) or isinstance(self, type(other)):
            return True
        else:
            # TODO: test this properly!! seems dangerous
            return super().__eq__(other)
