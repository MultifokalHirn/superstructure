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

    def _retrieve_wissen(self):
        return [b.name for b in self._begriffe]

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
        return begriffe

    def __repr__(self):
        size = len(self.wissen)
        return f'<System :: {self.name} [{self.state}] -- size {size}>'
