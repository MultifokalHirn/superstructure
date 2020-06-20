import os

import dill as pickle  # nosec

from superstructure.metastructure.form import LogischeForm

data_store = "pickled_data"


def _get_bewusstsein_dict(path=data_store):
    try:
        with open(path, "rb") as f:
            bewusstsein_dict = pickle.load(f)  # nosec
    except FileNotFoundError:
        bewusstsein_dict = {}
    return bewusstsein_dict


def load(name="Weltgeist", path=data_store):
    return _get_bewusstsein_dict(path=path).get(name)


def save(bewusstsein, path=data_store):
    if not isinstance(bewusstsein, LogischeForm):
        raise ValueError(
            f"pickled.save: trying to save {bewusstsein}, but it does not have the LogischeForm."
        )

    bewusstsein_dict = _get_bewusstsein_dict(path=path)
    bewusstsein_dict[bewusstsein.name] = bewusstsein
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} does not exist!")
    with open(path, "wb") as f:
        pickle.dump(bewusstsein_dict, f)
