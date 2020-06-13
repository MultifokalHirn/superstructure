import itertools

import click

from superstructure.infrastructure.logo import print_logo
from superstructure.infrastructure.storage.pickled import load, save
from superstructure.metastructure.geist import Bewusstsein


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
        bewusstsein = Bewusstsein(name=name, verbose=verbose)
    bewusstsein.spill()
    begriff_combos = list(
        itertools.product(
            [bewusstsein.get(name) for name in bewusstsein.vocabulary], repeat=2
        )
    )
    for (begriff_a, begriff_b) in begriff_combos:
        relations = [
            relation.name
            for relation in (
                bewusstsein.determine_relations(begriff_a.content, begriff_b.content)
            )
        ]
        if len(relations) > 0:
            if begriff_a.name == begriff_b.name:
                topic = begriff_a.name
            else:
                topic = f"{begriff_a.name} and {begriff_b.name}"
            print(f"{topic} : {relations}")
    save(bewusstsein)


if __name__ == "__main__":
    cli()
