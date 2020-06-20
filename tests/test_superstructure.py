import sys
import unittest

import better_exceptions

from superstructure.infrastructure.cli.commands import main


class TestSuperstructure(unittest.TestCase):
    def test_cli(self):
        main(name="TestSuperstructure", verbose=True)
        # main()


def patch(self, err, test):
    lines = better_exceptions.format_exception(*err)
    if sys.version_info[0] == 2:
        return u"".join(lines).encode("utf-8")
    return "".join(lines)


unittest.result.TestResult._exc_info_to_string = patch


if __name__ == "__main__":
    unittest.main()
