"""
Created on Tue Jun 15 15:02:23 2021

@author: barre
"""

import datetime
import json
import os

import joblib
import pandas as pd
from shap import TreeExplainer

from botfinder import config


ramdom_forest_file = config.PACKAGE_INSTALL_DIR / "random_forest.joblib"

model = joblib.load(ramdom_forest_file)
explainer = TreeExplainer(model)


def age(date):
    u = pd.Timestamp(date, tz=None)
    u = u.tz_convert(None)
    return (pd.Timestamp.today() - u).days + 1


def nbdigits(string):
    return sum(c.isdigit() for c in string)


def augmentdf(df):
    output = pd.DataFrame.copy(df)
    output["tweet_frequence"] = df["statuses_count"] / df["age"]
    output["followers_growth_rate"] = df["followers_count"] / df["age"]
    output["friends_growth_rate"] = df["friends_count"] / df["age"]
    output["favourites_growth_rate"] = df["favourites_count"] / df["age"]
    output["listed_growth_rate"] = df["listed_count"] / df["age"]
    output["friends_followers_ratio"] = df["friends_count"] / (
        df["followers_count"] + 1
    )
    output["followers_friend_ratio"] = df["followers_count"] / (df["friends_count"] + 1)
    output["name_length"] = df["name"].apply(len)
    output["screenname_length"] = df["screen_name"].apply(len)
    output["name_digits"] = df["name"].apply(nbdigits)
    output["screen_name_digits"] = df["screen_name"].apply(nbdigits)
    output["description_length"] = df["description"].apply(len)
    return output


def is_bot(df):
    df.rename(columns=config.SNSCRAPE_TO_API, inplace=True)
    df["profile_use_background_image"] = True
    df["default_profile"] = False
    df["age"] = df["created_at"].apply(age)
    features = df[config.FEATURES]
    features = augmentdf(features)
    features = features.drop(columns=["description", "name", "screen_name"])
    shap_values = explainer.shap_values(features)
    rounded = [round(i, 3) for i in shap_values[1][0]]
    dic = dict(zip(features.columns, rounded))
    dic["base_value"] = explainer.expected_value[1]

    botScore = round(model.predict_proba(features)[0][1], 3)
    return json.dumps({"botScore": botScore, "details": dic})


def findbot(name):
    """Also works with the id"""

    tmp_file = config.TMP_DIR / "user.json"
    os.system(
        f"snscrape --with-entity --max-results 0 --jsonl twitter-user {name} > {tmp_file}"
    )
    df = pd.read_json(tmp_file, lines=True)
    os.remove(tmp_file)
    t0 = datetime.datetime.now()
    return is_bot(df), datetime.datetime.now() - t0


def findbot_filename(filename):
    df = pd.read_json(f"{filename}.json", lines=True)
    return is_bot(df)


def findbot_rawjson(rawjson):
    js = json.loads(rawjson)
    df = pd.DataFrame.from_dict(js, orient="index").T
    return is_bot(df)
