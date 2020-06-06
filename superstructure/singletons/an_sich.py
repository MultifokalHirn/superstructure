from .utils import Singleton
from ..logik import LogischeForm


@Singleton
class ReinerBegriff(LogischeForm):
    def __init__(self):
        self._name = "Reiner Begriff"
        self._synonyms = ["Der reine Begriff", "Sein"]

    @property
    def name(self):
        return self._name

    @property
    def synonyms(self):
        return self._synonyms

    @property
    def besonderheit(self):
        return self

    @property
    def allgemeinheit(self):
        return self

    @property
    def einzelheit(self):
        return self
