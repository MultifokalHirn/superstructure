import dill as pickle  # nosec

data_store = "pickled_data"


def get_bewusstsein_dict():
    try:
        with open(data_store, "rb") as f:
            bewusstsein_dict = pickle.load(f)  # nosec
    except FileNotFoundError:
        bewusstsein_dict = {}
    except BaseException as e:
        print(e)
        bewusstsein_dict = {}
    return bewusstsein_dict


def load(name="weltgeist"):
    return get_bewusstsein_dict().get(name.lower())


def save(bewusstsein):
    bewusstsein_dict = get_bewusstsein_dict()
    bewusstsein_dict[bewusstsein.name.lower()] = bewusstsein
    with open(data_store, "wb") as f:
        pickle.dump(bewusstsein_dict, f)
