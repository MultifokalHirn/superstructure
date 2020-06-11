import sys
import unittest

import better_exceptions
from superstructure.metastructure.geist import Bewusstsein
from superstructure.metastructure.grundbegriffe import Einzelheit
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
        j = Begriff(name="J", allgemeinheit_id=i.id)
        i.einzelheit = j.id
        b.learn(i)
        b.learn(j)
        # self.assertEqual(i.allgemeinheit, Begriff().id)
        self.assertEqual(j.allgemeinheit, i.id)
        self.assertTrue(b.relation_applies(Einzelheit(), [j.id, i.id]))


if __name__ == "__main__":
    unittest.main()
