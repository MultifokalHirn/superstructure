import unittest

import pytest
from hypothesis import given
from hypothesis.strategies import text

from superstructure.geist import Bewusstsein
from superstructure.logik import Begriff, Unknown
from superstructure.grundbegriffe import Identität


class TestBewusstsein(unittest.TestCase):
    @given(text())
    def test_basic_bewusstsein(self, s):
        b = Bewusstsein(name="TestBewusstsein")
        a = Begriff(name="A")
        b.learn(a)

        self.assertTrue(
            b.relation_applies(Identität, [b.begriff("A").allgemeinheit, Begriff.id])
        )
        self.assertEqual(b.begriff(s), Unknown())
        self.assertFalse(b.other == b.self)
        with pytest.raises(ValueError, match=r".* can not be learned .*"):
            b.learn(a)
        # b.determine_relations()


if __name__ == "__main__":
    unittest.main()
