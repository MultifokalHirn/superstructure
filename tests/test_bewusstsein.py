import unittest

from hypothesis import example, given
from hypothesis.strategies import text

from superstructure.geist import Bewusstsein
from superstructure.singletons import Leere


class TestBewusstsein(unittest.TestCase):
    @given(text())
    def test_basic_bewusstsein(self, s):
        b = Bewusstsein(name="TestBewusstsein")
        self.assertEqual(b.begriff("self"), b.begriff("sein"))
        self.assertEqual(b.begriff(s), Leere())


"""
(Ansichsein, Sein-für-Anderes) -> Etwas
(Inneres / Ding-An-Sich, Äußeres) ->  Ding

"""

if __name__ == "__main__":
    unittest.main()
