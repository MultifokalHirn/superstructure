
# from .utils import *

def check_structure(f):
    def wrapper(*args):
        potential_structure = args[0]
        if potential_structure is not None:
            assert(potential_structure.superstructure is not None)
            assert(potential_structure.negative is not None)
            assert(potential_structure.aspects is not None)
            return f(*args)
    return wrapper


class Negative:
    def __init__(self, whole=None, *args, **kwargs):

        # self._decorated = decorated
        self._whole = whole
        self._name = "Negative"
        self._superstructure = self
        self._negative = self
        self._instances = set()
        # self.aspects = set()

    @property
    def is_negative(self):
        return True

    @property
    def name(self):
        return self._name

    @property
    def superstructure(self):
        return self._superstructure

    @property
    def negative(self):
        return self._negative

    @property
    def top_structure(self):
        if self.superstructure is not self:
            return self.superstructure.top_structure
        else:
            return None

    # def instance(self):
    #     """
    #     Returns the singleton instance. Upon its first call, it creates a
    #     new instance of the decorated class and calls its `__init__` method.
    #     On all subsequent calls, the already created instance is returned.

    #     """
    #     try:
    #         return self._instance
    #     except AttributeError:
    #         self._instance = self._decorated()
    #         return self._instance

    # def __call__(self):
    #     raise TypeError('Singletons must be accessed through `instance()`.')

    # def __instancecheck__(self, inst):
    #     return isinstance(inst, self._decorated)

    def __repr__(self):
        return f'<{self._name}>'


class Structure(Negative):
    def __init__(self, name, whole=None, superstructure=None, negative=None):
        super().__init__(whole=whole)
        self._name = name
        if superstructure is not None:
            self.set_superstructure(superstructure)
        if negative is not None:
            self.set_negative(negative)

    @property
    def is_negative(self):
        return False

    @check_structure
    def set_superstructure(self, superstructure):
        self._superstructure = superstructure

    @check_structure
    def set_negative(self, negative):
        if negative is not self:
            self._negative = negative

    def check_integrity(self):
        pass

    def __repr__(self):
        if self.negative.is_negative:
            return f'<{self.superstructure.name} :: Structure {self._name}>'
        else:
            return f'<{self.superstructure.name} :: Structure {self._name} (<-> {self.negative._name})>'


class Whole:
    def __init__(self, name, meta_structure=Negative(), structures=set()):
        self.name = name
        self.state = "absolute"
        self.meta_structure = meta_structure
        self.structures = set([self.meta_structure])
        self.structures = self.structures.union(set(structures))

    def add(self, structure):
        self.structures.add(structure)

    def create(self, name):
        new_structure = Structure(name=name)
        self.structures.add(new_structure)

    def __repr__(self):
        size = len(self.structures) - 1
        return f'<Whole :: {self.name} [{self.state}] -- size {size}>'
