import click

from superstructure.hyperstructure.vernunft import (
    get_negations,
    get_relations_between_known_begriffe,
)
from superstructure.infrastructure.cli.utils import init, save_pickled
from superstructure.infrastructure.logo import print_logo


def main(name: str, verbose: bool):
    if verbose:
        click.echo("[verbose mode]\n")
    print_logo()
    bewusstsein = init(name=name, verbose=verbose)
    bewusstsein.summarize()
    bewusstsein.say(get_relations_between_known_begriffe(bewusstsein))
    bewusstsein.say(get_negations(bewusstsein))

    save_pickled(bewusstsein)
