from singletons.an_sich import Leere

from .logik import Begriff, Relation
from .utils import is_compatible


class Bewusstsein:
    def __init__(self, name, begriffe=set()):
        self.name = name
        self.state = "coherent"  # should become singleton
        if len(begriffe) == 0:
            self._begriffe = self.generate_basic_begriffe()
        self._wissen = self._retrieve_wissen()

    @property
    def wissen(self):
        # should beorganized like dict, where begriffe can be searched by their name
        if len(self._wissen) == 0:
            self._wissen = self._retrieve_wissen()
        return self._wissen

    def begriff(self, name):
        # should beorganized like dict, where begriffe can be searched by their name
        result = self.wissen.get(name, [])
        if len(result) == 0:
            return Leere.instance()
        elif len(result) == 1:
            return result[0]
        else:
            raise ValueError(f"{self} has multiple begriffe of {name}")

    def _retrieve_wissen(self):
        wissen = {}
        for begriff in self._begriffe:
            for name in begriff.names:
                wissen[name] = wissen.get(name, set()).update(begriff.id)
        return wissen

    def handle(self, information):
        # if contents of information can be integrated into _begriffe without raising a "incoherent" state,
        for x in information:
            if is_compatible(self.wissen, x):
                self.update(x)

    def update(self, begriff):
        if not begriff.name not in self.wissen:
            raise ValueError(f"Trying to update unknown begriff {begriff.name}")
        else:
            pass
            # self._begriffe.remove(begriff)
            # self._begriffe[begriff.name] = begriff

    def forget(self, begriff):
        if not begriff.name not in self.wissen:
            raise ValueError(f"Trying to forget unknown begriff {begriff.name}")
        else:
            self._begriffe.remove(begriff)

    def learn(self, begriff):
        if not begriff.name in self.wissen:
            raise ValueError(f"{begriff.name} can not be learned since its already known")
        else:
            self._begriffe.add(begriff)

    def generate_basic_begriffe(self):
        begriffe = set()
        Begriff(name="self", )
        return begriffe

    @property
    def known_relations(self):
        return [begriff for begriff in self._begriffe if isinstance(begriff, Relation)]

    def relation_applies(self, relation, a, b):
        # TODO it should be structurally impossible for a Bewusstsein to evaluate begriffe that are not its inhalt, with relations it does not know
        return relation.condition(a, b)

    def determine_relations(self, a, b):
        for relation in self.known_relations:
            if self.relation_applies(relation, a, b):
                yield relation

    def __repr__(self):
        size = len(self.wissen)
        return f'<Bewusstsein :: {self.name} [{self.state}] -- size {size}>'
