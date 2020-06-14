import sys
import unittest

import better_exceptions
from superstructure.metastructure.geist import Bewusstsein
from superstructure.metastructure.grundbegriffe import Negation
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
        j = Begriff(name="J", negation=i)
        i.negation = j
        b.learn(i.name, i)
        b.learn(j.name, j)
        i = b.get(i.name).content
        j = b.get(j.name).content
        self.assertEqual(j.negation, i)
        self.assertEqual(i.negation, j)
        self.assertTrue(b.relation_applies(Negation(), [j, i]))
        self.assertTrue(b.relation_applies(Negation(), [i, j]))


if __name__ == "__main__":
    unittest.main()
