import unittest

import pytest

from superstructure.metastructure.geist import Bewusstsein
from superstructure.metastructure.logik import Begriff, Unknown
from superstructure.metastructure.grundbegriffe import Identität


class TestBewusstsein(unittest.TestCase):
    def test_basic_bewusstsein(self):
        b = Bewusstsein(name="TestBewusstsein")
        a = Begriff(name="A")
        b.learn(a)

        self.assertTrue(
            b.relation_applies(Identität(), [b.begriff("A").allgemeinheit, Begriff.id])
        )
        self.assertEqual(b.begriff("A"), Unknown())
        self.assertFalse(b.other == b.self)
        with pytest.raises(ValueError, match=r".* can not be learned .*"):
            b.learn(a)
        # b.determine_relations()


if __name__ == "__main__":
    unittest.main()
