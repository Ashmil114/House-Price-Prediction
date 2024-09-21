import pickle
import json
import numpy as np

with open("./model/home_price_model.pickle", "rb") as f:
    model = pickle.load(f)

with open("./dataset/columns.json", "r") as f:
    data_columns = json.load(f)["data_columns"]


def predict_price(location, sqft, bath, bhk):
    try:
        loc_index = data_columns.index(location.lower())
    except Exception as e:
        loc_index = -1
        return False
    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(model.predict([x])[0], 2)


# print(fun("1st Block Jayanagar", 2000, 1, 3))
