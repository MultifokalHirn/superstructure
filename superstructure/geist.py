from .singletons.an_sich import Leere

from .logik import Begriff, Relation
from .utils import is_compatible


class Bewusstsein:
    def __init__(self, name, begriffe={}):
        self.name = name
        self.state = "coherent"  # should become singleton
        self._begriffe = {}  # {id: Begriff}
        self._wissen = {}  # {name: [ids]}
        if len(begriffe) == 0:
            self.generate_basic_begriffe()
        self._update_wissen()

    @property
    def wissen(self):
        # should beorganized like dict, where begriffe can be searched by their name
        if len(self._wissen.keys()) == 0:
            self._update_wissen()
        return self._wissen

    def begriff(self, name):
        """Bewusstsein returns their Begriff of {name}"""
        ids = self.wissen.get(name, [])
        result = []
        for id in ids:
            result.append(self._begriffe[id])
        if len(result) == 0:
            return Leere()
        elif len(result) == 1:
            return result[0]
        else:
            raise ValueError(f"{self} has multiple begriffe of {name}")

    def _update_wissen(self):
        """create a hashmap from names to Begriff objects"""
        # print("_update_wissen....")
        wissen = {"me": [0]}
        for id, begriff in self._begriffe.items():
            for name in begriff.names:
                wissen[name] = wissen.get(name, []) + [id]
        self._wissen = wissen

    def handle(self, name, begriff):
        # if contents of information can be integrated into _begriffe without raising a "incoherent" state,
        subjective_begriff = self.begriff(name)
        if begriff != subjective_begriff:
            if is_compatible(self.wissen, begriff):
                self.update(begriff)
            else:
                self.say(f"a {name} is not a {begriff}!!")

    def update(self, begriff):
        # TODO should maybe take name and begriff
        if begriff.name not in self.wissen:
            raise ValueError(f"Trying to update unknown begriff {begriff.name}")
        else:
            for id in self.wissen[begriff.name]:
                self._begriffe[id] = begriff

    def forget(self, begriff):
        # TODO should maybe take name and begriff
        if not begriff.name not in self.wissen:
            raise ValueError(f"Trying to forget unknown begriff {begriff.name}")
        else:
            self._begriffe[begriff.id] = None
            # self._begriffe[begriff.id] = Leere()

    def learn(self, begriff):
        # TODO should maybe take name and begriff
        # print("learn....")
        if begriff.name in self.wissen.keys():
            raise ValueError(
                f"{begriff.name} can not be learned since its already known"
            )
        else:
            self._begriffe[begriff.id] = begriff

    def generate_basic_begriffe(self):
        """should fill up the Bewusstseins wissen with most basic Begriffe, for example a self, relations such as Identität and so on"""
        # TODO
        s = Begriff(name="self", id=0)
        self.learn(s)

    @property
    def known_relations(self):
        """list the relations the Bewusstsein has a Begriff of"""
        return [
            begriff
            for begriff in self._begriffe.values()
            if isinstance(begriff, Relation)
        ]

    def relation_applies(self, relation, a, b):
        # TODO it should be structurally impossible for a Bewusstsein to evaluate begriffe that are not its inhalt, with relations it does not know
        return relation.condition(a, b)

    def determine_relations(self, a, b):
        """yield relations the Bewusstsein thinks exist between a and b"""
        for relation in self.known_relations:
            if self.relation_applies(relation, a, b):
                yield relation

    def say(self, sentence):
        if sentence:
            print(f'  {self.name}: "{sentence}"')

    def spill(self):
        """say out all knowledge, only for testing"""
        for name, ids in self.wissen.items():
            for id in ids:
                self.say(f"I know {name} as {self._begriffe.get(id, None)}")

    def __repr__(self):
        size = len(self.wissen)
        return f"<Bewusstsein :: {self.name} [{self.state}] -- size {size}>"
