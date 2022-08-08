import requests
import json
import os
import pandas as pd
import geocoder
from IPython.core.display import clear_output
from sklearn.base import BaseEstimator, TransformerMixin


class AddressConverter(BaseEstimator, TransformerMixin):
    def __init__(self, neighborhood):
        self.neighborhood = neighborhood

    def fit(self, x):
        return self

    def transform(self, x, y=None):
        neighborhood = self.neighborhood
        x["fullNeighborhood"] = x[neighborhood]
        x["fullNeighborhood"].replace("Blmngtn", "Bloomington Heights", inplace=True)
        x["fullNeighborhood"].replace("Blueste", "Bluestem", inplace=True)
        x["fullNeighborhood"].replace("BrDale", "Briardale", inplace=True)
        x["fullNeighborhood"].replace("BrkSide", "Brookside", inplace=True)
        x["fullNeighborhood"].replace("ClearCr", "Clear Creek", inplace=True)
        x["fullNeighborhood"].replace("CollgCr", "College Creek", inplace=True)
        x["fullNeighborhood"].replace("Crawfor", "Crawford", inplace=True)
        x["fullNeighborhood"].replace("Edwards", "Edwards", inplace=True)
        x["fullNeighborhood"].replace("Gilbert", "Gilbert", inplace=True)
        # x["fullNeighborhood"].replace("IDOTRR", "Iowa DOT and Rail Road", inplace=True)
        # geocoder couldn't handel this address and this address modified to below
        x["fullNeighborhood"].replace("IDOTRR", "Iowa DOT", inplace=True)
        x["fullNeighborhood"].replace("MeadowV", "Meadow Village", inplace=True)
        x["fullNeighborhood"].replace("Mitchel", "Mitchell", inplace=True)
        x["fullNeighborhood"].replace("Names", "North Ames", inplace=True)
        x["fullNeighborhood"].replace("NoRidge", "Northridge", inplace=True)
        x["fullNeighborhood"].replace("NPkVill", "Northpark Villa", inplace=True)
        x["fullNeighborhood"].replace("NridgHt", "Northridge Heights", inplace=True)
        x["fullNeighborhood"].replace("NWAmes", "Northwest Ames", inplace=True)
        x["fullNeighborhood"].replace("OldTown", "Old Town", inplace=True)
        # x["fullNeighborhood"].replace("SWISU", "South & West of Iowa State University", inplace=True)
        # geocoder couldn't handel this address and this address modified to below
        x["fullNeighborhood"].replace("SWISU", "Iowa State University", inplace=True)
        x["fullNeighborhood"].replace("Sawyer", "Sawyer", inplace=True)
        x["fullNeighborhood"].replace("SawyerW", "Sawyer West", inplace=True)
        x["fullNeighborhood"].replace("Somerst", "Somerset", inplace=True)
        x["fullNeighborhood"].replace("StoneBr", "Stone Brook", inplace=True)
        x["fullNeighborhood"].replace("Timber", "Timberland", inplace=True)
        x["fullNeighborhood"].replace("Veenker", "Veenker", inplace=True)
        x['lat'] = pd.Series(x["fullNeighborhood"])
        x['long'] = pd.Series(x["fullNeighborhood"])
        # fak = "forward?access_key=a86d264896b9d26e816f31538a0c68a8&query="
        # endpoint = "http://api.positionstack.com/v1/"
        i = 1
        for fullNeighborhood in x["fullNeighborhood"].unique():
            try:
                print("requesting lat and long for ", fullNeighborhood, i, "/", len(x["fullNeighborhood"].unique()))
                # response = requests.get(os.path.join(endpoint, fak, fullNeighborhood))
                g = geocoder.osm(fullNeighborhood)
                x['lat'].replace(fullNeighborhood, g.json['lat'], inplace=True)
                x['long'].replace(fullNeighborhood, g.json['lng'], inplace=True)
                i += 1
                clear_output(wait=False)
                os.system('cls')
            except Exception as e:
                i += 1
                print(e)
                continue
            # x["lat"].replace(fullNeighborhood, json.loads(response.content)['data'][0]['latitude'], inplace=True)
            # x["long"].replace(fullNeighborhood, json.loads(response.content)['data'][0]['longitude'], inplace=True)
        x = x.drop(columns=["fullNeighborhood"])
        return x

