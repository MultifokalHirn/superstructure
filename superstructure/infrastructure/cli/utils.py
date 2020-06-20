from superstructure.infrastructure.storage.pickled import data_store, load, save
from superstructure.metastructure.geist import Bewusstsein, Selbstbewusstsein


def init(name: str, verbose: bool, path=data_store) -> Bewusstsein:
    bewusstsein = load(name=name, path=path)
    if bewusstsein is not None:
        if verbose:
            print(f"{bewusstsein} woke up!")
        return bewusstsein
    else:
        return Selbstbewusstsein(name=name, verbose=verbose)


def save_pickled(bewusstsein: Bewusstsein, path=data_store) -> None:
    save(bewusstsein, path=path)
