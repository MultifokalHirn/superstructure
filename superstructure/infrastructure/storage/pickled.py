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


def load(name="Weltgeist"):
    return get_bewusstsein_dict().get(name)


def save(bewusstsein):
    bewusstsein_dict = get_bewusstsein_dict()
    bewusstsein_dict[bewusstsein.name] = bewusstsein
    with open(data_store, "wb") as f:
        pickle.dump(bewusstsein_dict, f)
