import unittest

from hypothesis import example, given
from hypothesis.strategies import text

from superstructure.logik import Allgemeinheit, Einzelnheit
from superstructure.geist import Bewusstsein
from superstructure.singletons import AbstrakteAllgemeinheit, Identität


class TestBewusstsein(unittest.TestCase):
    @given(text())
    def create_new_structure(self, s):
        b = Bewusstsein(name="TestBewusstsein")
        print(b)
        # self.assertEqual(aa.allgemeinheit, Allgemeinheit)
        # self.assertEqual(aa1, aa2)


"""
(Ansichsein, Sein-für-Anderes) -> Etwas
(Inneres / Ding-An-Sich, Äußeres) ->  Ding

"""

if __name__ == "__main__":
    unittest.main()
