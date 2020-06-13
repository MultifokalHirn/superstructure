import sys
import unittest

import better_exceptions
from superstructure.metastructure.geist import Bewusstsein
from superstructure.metastructure.grundbegriffe import Einzelheit, Allgemeinheit
from superstructure.metastructure.logik import Begriff


def patch(self, err, test):
    lines = better_exceptions.format_exception(*err)
    if sys.version_info[0] == 2:
        return u"".join(lines).encode("utf-8")
    return "".join(lines)


unittest.result.TestResult._exc_info_to_string = patch


class TestLogik(unittest.TestCase):
    def test_basic_logik(self):
        b = Bewusstsein(name="TestBewusstsein")
        i = Begriff(name="I")
        j = Begriff(name="J", allgemeinheit=i)
        i.einzelheit = j
        b.learn(i.name, i)
        b.learn(j.name, j)
        i = b.get(i.name).content
        j = b.get(j.name).content
        self.assertEqual(j.allgemeinheit, i)
        self.assertEqual(i.einzelheit, j)
        self.assertTrue(b.relation_applies(Einzelheit(), [j, i]))
        self.assertTrue(b.relation_applies(Allgemeinheit(), [i, j]))
        b.reflect()


if __name__ == "__main__":
    unittest.main()
