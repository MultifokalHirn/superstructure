import unittest

from superstructure.metastructure.logik import Begriff

from superstructure.metastructure.grundbegriffe import Einzelheit
from superstructure.metastructure.geist import Bewusstsein


class TestLogik(unittest.TestCase):
    def test_basic_logik(self):
        b = Bewusstsein(name="TestBewusstsein")
        i = Begriff(name="I")
        j = Begriff(name="J", allgemeinheit_id=i.id)
        i.einzelheit = j.id
        b.learn(i)
        b.learn(j)
        # self.assertEqual(i.allgemeinheit, Begriff().id)
        self.assertEqual(j.allgemeinheit, i.id)
        self.assertTrue(b.relation_applies(Einzelheit(), [j.id, i.id]))


if __name__ == "__main__":
    unittest.main()
