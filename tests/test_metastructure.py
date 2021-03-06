import sys
import unittest

import better_exceptions
import pytest

from superstructure.metastructure.form import LogischeForm
from superstructure.metastructure.geist import Bewusstsein, Forgotten, Selbstbewusstsein
from superstructure.metastructure.grundbegriffe import (
    AnsichSein,
    Aufhebung,
    Einzelheit,
    Etwas,
    FürUnsSein,
    Identität,
    Negation,
    Selbstidentität,
)

# from superstructure.metastructure.core import Begriff, Relation, Unknown
from superstructure.metastructure.core import Begriff, Relation, Unknown  # noqa


class TestForm(unittest.TestCase):
    def test_form(self):
        form = LogischeForm()
        self.assertTrue(
            len(list(LogischeForm.einzelheiten())) == 0
        )  # should be greater than, but current allgemeinheit solution breaks einzelheiten
        for a in [
            form.name,
            form.position,
            form.negation,
            form.allgemeinheit,
            form.aufhebung,
            form.related,
        ]:
            continue


# class TestBestimmung(unittest.TestCase):
#     def test_bestimmung(self):
#         bestimmteAllgemeinheit = Begriff("UnbestimmteAllgemeinheit", wesen=[],)
#         assertTrue(unbestimmteAllgemeinheit.is_bestimmt)
#         human = Begriff("UnbestimmteAllgemeinheit",)


class TestGeist(unittest.TestCase):
    def test_unknown_and_forgotten(self):
        self.assertTrue(Unknown().is_pure)
        self.assertTrue(Forgotten().is_pure)
        self.assertEqual(Forgotten(), Unknown())
        self.assertNotEqual(str(Forgotten()), str(Unknown()))
        self.assertSetEqual(Unknown().related, set())
        self.assertEqual(Unknown().position, Forgotten().aufhebung)
        self.assertEqual(Unknown().position, Unknown().negation)
        self.assertEqual(Unknown().allgemeinheit, Unknown())
        self.assertEqual(Forgotten().position, Forgotten().negation)

    def test_basic_bewusstsein(self):
        b = Bewusstsein(verbose=True, name="TestBewusstsein",)
        b.summarize(omit_grundbegriffe=False)
        b.summarize(omit_grundbegriffe=True)
        with pytest.raises(TypeError):
            b.get(None)

        a = Begriff(name="A")
        self.assertFalse(b.knows(a))
        b.learn(a.name, a)
        self.assertTrue(b.knows(a))
        self.assertEqual(b.get(a.name).begriff, a)
        b.handle(a.name, a)

        b.forget(a.name)
        self.assertEqual(b.get(a.name).begriff, Forgotten())
        b.handle(a.name, a)
        b.summarize(omit_grundbegriffe=True)
        self.assertEqual(b.get(a.name).begriff, a)

        self.assertEqual(b.get("SomethingUnknown").begriff, Unknown())
        with pytest.raises(TypeError):
            b.say(None)
        b.summarize(omit_grundbegriffe=False)
        b.summarize(omit_grundbegriffe=True)

    def test_selbstbewusstsein(self):
        b = Selbstbewusstsein(name="TestSelbstbewusstsein", verbose=True)
        a = Begriff(name="A")
        b.learn(a.name, a)
        b.handle(a.name, b.itself)
        a = Begriff(name="A", negation=b.itself)
        b.update_begriff(a)

        self.assertTrue(len(b.known_relations(nodes=0)) == 0)

        self.assertTrue(
            b.relation_applies(
                relation=Negation(), begriffe=("PureAllgemeinheit", "PureEinzelheit")
            )
        )

        self.assertTrue(
            b.relation_applies(
                relation=Identität(), begriffe=("A", "A"), accept_identicals=True
            )
        )
        self.assertTrue(
            b.relation_applies(
                relation=Selbstidentität(), begriffe=("A", "A"), accept_identicals=True
            )
        )

        self.assertEqual(b.get("SomethingUnknown").begriff, Unknown())
        self.assertEqual(
            [
                known_begriff.begriff
                for known_begriff in b.get(["A", "SomethingUnknown"])
            ],
            [a, Unknown()],
        )
        self.assertFalse(a == b.itself)
        for begriff in b.begriffe:
            self.assertTrue(
                b.relation_applies(
                    FürUnsSein(), begriffe=(begriff,), accept_identicals=False
                )
            )
        self.assertFalse(
            b.relation_applies(
                Einzelheit(),
                begriffe=(b.itself, Bewusstsein.allgemein()),
                accept_identicals=False,
            )
        )  # must be True, but einzelheiten is currently broken
        unknown_begriff = Begriff(
            name="SomethingUnknown",
            negation=a,
            allgemeinheit=Begriff.allgemein(),
            aufhebung=Begriff.allgemein(),
        )

        with pytest.raises(ValueError):
            b.update_meaning(a.name, unknown_begriff)

        with pytest.raises(ValueError):
            b.update_begriff(unknown_begriff)

        with pytest.raises(TypeError):
            _ = Begriff(
                name="SomethingBroken",
                negation=a,
                allgemeinheit=Begriff,
                aufhebung=Begriff.allgemein(),
            )

        with pytest.raises(TypeError):
            b.learn("Begriff", Begriff, force=True)

        with pytest.raises(TypeError):
            b.knows(self)

        with pytest.raises(ValueError):
            begriff_with_unknown_related_begriff = Begriff(
                name="BegriffWithUnknownRelatedBegriff",
                negation=a,
                allgemeinheit=Begriff(name="UnknownRelatedBegriff"),
                aufhebung=Begriff.allgemein(),
            )
            b.learn(
                "BegriffWithUnknownRelatedBegriff",
                begriff_with_unknown_related_begriff,
                force=False,
            )

        self.assertTrue(b.can_accept(b))
        self.assertFalse(b.can_accept(unknown_begriff))
        b.learn(b.itself.name, a)  # should not be an issue
        b.summarize(omit_grundbegriffe=False)
        b.summarize(omit_grundbegriffe=True)
        itself = b.itself
        some_begriff = Begriff(name="SomeBegriff")
        with pytest.raises(ValueError):
            b.learn(b.name, some_begriff, force=True)
            b.reflect()
            b.summarize()
            raise ValueError()  # this should actually raise one!
        b.learn(itself.name, itself)
        with pytest.raises(ValueError):
            b.forget("SomethingUnknown")


class TestLogik(unittest.TestCase):
    def test_basic_core(self):
        b = Bewusstsein(name="TestBewusstsein", verbose=False)

        h = Begriff(name="H")
        i = Begriff(name="I", aufhebung=h)
        j = Begriff(name="J", aufhebung=h)
        self.assertTrue(i == i)
        self.assertTrue(i == i.position)
        self.assertTrue(h == i.aufhebung)
        self.assertFalse(i == j)
        self.assertFalse(j == Unknown())
        begriffe = [j, i]
        begriffe = sorted(begriffe)
        self.assertTrue(begriffe[0] == i)
        i._negation = j
        j._negation = i
        b.learn(i.name, i)
        b.learn(j.name, j)
        b.say_knowledge_on(j.name)
        i = b.get(i.name).begriff
        j = b.get(j.name).begriff
        self.assertEqual(j.negation, i)
        self.assertEqual(i.negation, j)
        self.assertTrue(b.relation_applies(Negation(), [j, i]))
        self.assertTrue(b.relation_applies(Negation(), [i, j]))

        with pytest.raises(ValueError):
            _ = Relation()

        def my_criterium(geist=None):
            return True

        with pytest.raises(ValueError):
            _ = Relation(nodes=0, criterium=my_criterium)

        r = Relation(name="TestRelation", nodes=1, criterium=my_criterium)
        b.learn(r.name, r)
        self.assertTrue(
            b.relation_applies(Aufhebung(), (Etwas(), AnsichSein(), FürUnsSein(),))
        )
        self.assertTrue(
            b.relation_applies(Aufhebung(), (Etwas(), FürUnsSein(), AnsichSein(),))
        )


def patch(self, err, test):
    lines = better_exceptions.format_exception(*err)
    if sys.version_info[0] == 2:
        return "".join(lines).encode("utf-8")
    return "".join(lines)


unittest.result.TestResult._exc_info_to_string = patch


if __name__ == "__main__":
    unittest.main()
