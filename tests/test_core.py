import unittest

from hypothesis import example, given
from hypothesis.strategies import text

from superstructure.logik import Allgemeinheit, Einzelnheit
from superstructure.singletons import AbstrakteAllgemeinheit, Identität


class TestCore(unittest.TestCase):
    @given(text())
    def create_new_structure(self, s):
        aa = AbstrakteAllgemeinheit()
        a = Allgemeinheit("Jetzt")
        self.assertEqual(aa.allgemeinheit, a.__class__)
        self.assertEqual(Identität, Identität)


"""
(Ansichsein, Sein-für-Anderes) -> Etwas
(Inneres / Ding-An-Sich, Äußeres) ->  Ding

"""

if __name__ == "__main__":
    unittest.main()
