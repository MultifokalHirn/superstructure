import sys
import unittest
from subprocess import CalledProcessError  # nosec

import better_exceptions
import pytest

from superstructure.infrastructure.logo import (
    print_hegel,
    print_logo,
)
from superstructure.infrastructure.storage.pickled import load, save
from superstructure.infrastructure.cli.utils import init, save_pickled
from superstructure.metastructure.geist import Selbstbewusstsein


class TestLogo(unittest.TestCase):
    def test_logo(self):
        print_logo()
        with pytest.raises(CalledProcessError):
            print_hegel()
        for terminal_width in [100, 80, 60, 40]:
            print_hegel(terminal_width=terminal_width)


class TestStorage(unittest.TestCase):
    def test_pickled(self):
        name = "TestBewusstsein"

        path = "tests/fixtures/pickled_data"
        bewusstsein = load(name=name, path=path)
        if bewusstsein is None:
            bewusstsein = Selbstbewusstsein(name=name, verbose=True)
        save(bewusstsein, path=path)

        path = "tests/fixtures/does_not_exist"
        bewusstsein = load(name=name, path=path)
        if bewusstsein is None:
            bewusstsein = Selbstbewusstsein(name=name, verbose=True)
        with pytest.raises(FileNotFoundError):
            save(bewusstsein, path=path)


class TestCLI(unittest.TestCase):
    def test_cli(self):

        name = "TestBewusstsein"
        path = "tests/fixtures/pickled_data"
        bewusstsein = init(name=name, verbose=True, path=path)
        bewusstsein = init(name=name, verbose=False, path=path)
        save_pickled(bewusstsein, path=path)

        name = "DoesNotExist"
        bewusstsein = init(name=name, verbose=False, path=path)
        self.assertTrue(bewusstsein is not None)
        with pytest.raises(ValueError):
            save_pickled(None, path=path)

        path = "tests/fixtures/does_not_exist"
        bewusstsein = init(name=name, verbose=True, path=path)
        with pytest.raises(FileNotFoundError):
            save_pickled(bewusstsein, path=path)


def patch(self, err, test):
    lines = better_exceptions.format_exception(*err)
    if sys.version_info[0] == 2:
        return u"".join(lines).encode("utf-8")
    return "".join(lines)


unittest.result.TestResult._exc_info_to_string = patch


if __name__ == "__main__":
    unittest.main()
