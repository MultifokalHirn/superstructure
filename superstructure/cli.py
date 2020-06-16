import click

from superstructure.infrastructure.logo import print_logo
from superstructure.infrastructure.storage.pickled import load, save
from superstructure.metastructure.geist import Selbstbewusstsein
from superstructure.hyperstructure.vernunft import (
    say_all_relations_between_known_begriffe,
    say_negations,
)


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
    say_all_relations_between_known_begriffe(bewusstsein)
    say_negations(bewusstsein)
    save(bewusstsein)


if __name__ == "__main__":
    cli()
