import itertools

import click

from superstructure.infrastructure.logo import print_logo
from superstructure.infrastructure.storage.pickled import load, save
from superstructure.metastructure.geist import Selbstbewusstsein


@click.command()
@click.option("--name", default="Weltgeist", help="Which Bewusstsein are we loading?")
@click.option("--verbose", is_flag=True, help="Will print verbose messages.")
def cli(name, verbose):
    if verbose:
        click.echo("[verbose mode]\n")
    print_logo()
    bewusstsein = load(name=name)
    if bewusstsein is not None:
        print(f"{bewusstsein} woke up!")
    else:
        bewusstsein = Selbstbewusstsein(name=name, verbose=verbose)
    bewusstsein.spill()
    word_combos = itertools.product(
        [bewusstsein.get(name).name for name in bewusstsein.vocabulary], repeat=2
    )

    word_combos = set(frozenset(k) for k, _ in itertools.groupby(word_combos))
    print(f"Checking Relations between the Begriffe known to {bewusstsein}")
    for combo in word_combos:
        combo = tuple(combo)
        if len(combo) == 1:
            (word_a, word_b) = (combo[0], combo[0])
        else:
            (word_a, word_b) = (combo[0], combo[1])
        relations = [
            relation.name
            for relation in (
                bewusstsein.determine_relations(
                    bewusstsein.get(word_a).content, bewusstsein.get(word_b).content,
                )
            )
        ]
        if len(relations) > 0:
            if word_a == word_b:
                topic = word_a
            else:
                topic = f"{word_a} and {word_b}"
            bewusstsein.say(f"{topic}: {relations}")
    save(bewusstsein)


if __name__ == "__main__":
    cli()
