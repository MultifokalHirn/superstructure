import sys
import unittest

import better_exceptions
from superstructure.metastructure.geist import Bewusstsein
from superstructure.metastructure.grundbegriffe import Identität
from superstructure.metastructure.logik import Begriff, Unknown


class TestBewusstsein(unittest.TestCase):
    def test_basic_bewusstsein(self):
        b = Bewusstsein(name="TestBewusstsein")
        a = Begriff(name="A")
        b.learn(a.name, a)
        self.assertTrue(
            b.relation_applies(Identität(), [b.get("A").content, b.get("A").content])
        )
        self.assertEqual(b.get("B").content, Unknown())
        self.assertFalse(a == b.itself)
        b.learn(b.name, b)
        # b.determine_relations()


def patch(self, err, test):
    lines = better_exceptions.format_exception(*err)
    if sys.version_info[0] == 2:
        return u"".join(lines).encode("utf-8")
    return "".join(lines)


unittest.result.TestResult._exc_info_to_string = patch


if __name__ == "__main__":
    unittest.main()
