import sys
import unittest

import better_exceptions
import pytest
from superstructure.metastructure.geist import Bewusstsein
from superstructure.metastructure.grundbegriffe import Identität
from superstructure.metastructure.logik import Begriff, Unknown


class TestBewusstsein(unittest.TestCase):
    def test_basic_bewusstsein(self):
        b = Bewusstsein(name="TestBewusstsein")
        a = Begriff(name="A")
        b.learn(a)
        self.assertTrue(
            b.relation_applies(Identität(), [b.get("A").allgemeinheit, Begriff.id])
        )
        self.assertEqual(b.get("A"), Unknown())
        self.assertFalse(b.other == b.self)
        with pytest.raises(ValueError, match=r".* can not be learned .*"):
            b.learn(a)
        # b.determine_relations()


def patch(self, err, test):
    lines = better_exceptions.format_exception(*err)
    if sys.version_info[0] == 2:
        return u"".join(lines).encode("utf-8")
    return "".join(lines)


unittest.result.TestResult._exc_info_to_string = patch


if __name__ == "__main__":
    unittest.main()
