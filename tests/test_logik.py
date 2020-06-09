import unittest

from hypothesis import given
from hypothesis.strategies import text

from superstructure.logik import Begriff

from superstructure.grundbegriffe import Einzelheit
from superstructure.geist import Bewusstsein


class TestLogik(unittest.TestCase):
    @given(text())
    def test_basic_logik(self, s):
        b = Bewusstsein(name="TestBewusstsein")
        i = Begriff(name="I")
        j = Begriff(name="J", allgemeinheit_id=i.id)
        i.set_einzelheit(j.id)
        b.learn(i)
        b.learn(j)
        self.assertEqual(i.allgemeinheit, Begriff.id)
        self.assertEqual(j.allgemeinheit, i.id)
        self.assertTrue(b.relation_applies(Einzelheit, [b.get(i.einzelheit), j]))


if __name__ == "__main__":
    unittest.main()
