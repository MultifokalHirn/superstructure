import sys
import unittest
import pytest
import better_exceptions
from superstructure.metastructure.logik import Begriff, Unknown
from superstructure.metastructure.geist import Selbstbewusstsein
from superstructure.hyperstructure.vernunft import (
    get_relations_between_known_begriffe,
    get_negations,
)


class TestVernunft(unittest.TestCase):
    def test_vernunft(self):
        bewusstsein_a = Selbstbewusstsein(name="TestBewusstsein", verbose=True)
        sun = Begriff(name="Sun")
        bewusstsein_a.learn(sun.name, sun)
        bewusstsein_a.learn("Sonne", sun)
        bewusstsein_b = Selbstbewusstsein(
            name="TestBewusstsein", verbose=False, learn_grundbegriffe=False
        )
        for bewusstsein in [bewusstsein_a, bewusstsein_b]:
            bewusstsein.say(
                get_relations_between_known_begriffe(
                    bewusstsein, accept_identicals=True
                )
            )
            bewusstsein.say(
                get_relations_between_known_begriffe(
                    bewusstsein, accept_identicals=False
                )
            )
            bewusstsein.say(get_negations(bewusstsein))
            with pytest.raises(TypeError):
                bewusstsein.learn(Unknown().name, Unknown())


def patch(self, err, test):
    lines = better_exceptions.format_exception(*err)
    if sys.version_info[0] == 2:
        return u"".join(lines).encode("utf-8")
    return "".join(lines)


unittest.result.TestResult._exc_info_to_string = patch


if __name__ == "__main__":
    unittest.main()
