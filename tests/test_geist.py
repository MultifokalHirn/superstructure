import sys
import unittest

import better_exceptions

from superstructure.metastructure.geist import Selbstbewusstsein
from superstructure.metastructure.grundbegriffe import FürUnsSein, Identität
from superstructure.metastructure.logik import Begriff, Unknown


class TestBewusstsein(unittest.TestCase):
    def test_basic_bewusstsein(self):
        b = Selbstbewusstsein(name="TestBewusstsein")
        a = Begriff(name="A")
        b.learn(a.name, a)
        self.assertTrue(b.relation_applies(Identität(), ("A", "A")))
        self.assertEqual(b.get("B").content, Unknown())
        self.assertFalse(a == b.itself)
        for begriff in b.begriffe:
            self.assertTrue(b.relation_applies(FürUnsSein(), begriffe=(begriff,)))
        try:
            i = b.itself
            b.learn(b.itself.name, a)
            b.reflect()
        except ValueError:
            b.learn(i.name, i)
        else:
            self.assertFalse(True)
        b.reflect()


def patch(self, err, test):
    lines = better_exceptions.format_exception(*err)
    if sys.version_info[0] == 2:
        return u"".join(lines).encode("utf-8")
    return "".join(lines)


unittest.result.TestResult._exc_info_to_string = patch


if __name__ == "__main__":
    unittest.main()
