from .grundbegriffe import Allgemeinheit, AnsichSein, Einzelheit, FürUnsSein, Identität
from .logik import Begriff, Relation, Unknown
from .utils import is_compatible


class Bewusstsein:
    def __init__(self, name, begriffe={}):
        self._name = name
        self.state = "coherent"  # should become singleton
        self._begriffe = {}  # {id: Begriff}
        self._wissen = {}  # {name: [ids]}
        self._other = Unknown()
        if len(begriffe) == 0:
            self.generate_basic_begriffe()
        else:
            self._update_wissen()

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self.name

    @property
    def wissen(self):
        if len(self._wissen.keys()) == 0:
            self._update_wissen()
        return self._wissen

    @property
    def self(self):
        return self.begriff("self")

    @property
    def other(self):
        return self._other

    def _set_other(self, other):
        if self.other == other:
            return
        self._other = other

    def begriff(self, word):
        """Bewusstsein returns their Begriff of {word}"""
        ids = self.wissen.get(word, [])
        result = []
        for id in ids:
            result.append(self._begriffe[id])
        if len(result) == 0:
            return self.other
        elif len(result) == 1:
            return result[0]
        else:
            raise ValueError(f"{self} has multiple begriffe of {word}: {result}")

    def _update_wissen(self):
        """create a hashmap from names to Begriff objects"""
        # print("_update_wissen....")
        wissen = {}
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
            self._update_wissen()

    def forget(self, begriff):
        # TODO should maybe take name and begriff
        if not begriff.name not in self.wissen:
            raise ValueError(f"Trying to forget unknown begriff {begriff.name}")
        else:
            # self._begriffe[begriff.id] = None
            self._begriffe[begriff.id] = self.other
            self._update_wissen()

    def learn(self, begriff, verbose=False):
        # TODO should maybe take name and begriff
        # print("learn....")
        if begriff.name in self.wissen.keys():
            raise ValueError(
                f"{begriff.name} can not be learned since its already known"
            )
        else:
            self._begriffe[begriff.id] = begriff
            self._update_wissen()

    def get(self, begriff_id):
        return self._begriffe.get(begriff_id, Unknown())

    def generate_basic_begriffe(self):
        """should fill up the Bewusstseins wissen with most basic Begriffe, for example a self, relations such as Identität and so on"""
        # TODO
        self._set_other(Unknown())
        s = Begriff(name="self")
        self.learn(s)
        self.learn(Identität())
        self.learn(Allgemeinheit())
        self.learn(Einzelheit())
        self.learn(AnsichSein())
        self.learn(FürUnsSein())
        self._update_wissen()

    @property
    def known_relations(self, nodes=None):
        """list the relations the Bewusstsein has a Begriff of"""
        relations = [
            begriff
            for begriff in self._begriffe.values()
            if isinstance(begriff, Relation)
        ]
        if nodes is not None:
            return [relation for relation in relations if relation.nodes == nodes]
        else:
            return relations

    def relation_applies(self, relation, begriff_ids=[], verbose=True):
        # TODO it should be structurally impossible for a Bewusstsein to evaluate begriffe that are not its inhalt, with relations it does not know
        if relation.nodes != len(begriff_ids):
            if verbose:
                self.say(
                    f"{relation} can only apply for {relation.nodes} Begriff{'e' if relation.nodes != 1 else ''}, thus it can not apply for {begriff_ids}"
                )
            return False
        else:
            begriffe = [self.get(begriff_id) for begriff_id in begriff_ids] + [self]
            args = tuple(begriffe)
            # print(f"relation.criterium({args})")
            # print(f"({relation.criterium(*args)})")
            return relation.criterium(*args)

    def determine_relations(self, a, b):
        """yield relations the Bewusstsein thinks exist between a and b"""
        for relation in self.known_relations:
            if self.relation_applies(relation, begriff_ids=[a, b], verbose=False):
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
        size = len(self._begriffe)
        return f"<Bewusstsein :: {self.name} -- knows {size} Begriffe>"
