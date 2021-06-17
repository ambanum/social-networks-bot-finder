# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 15:02:23 2021

@author: barre
"""
import json 
import tweepy
import pandas as pd
import joblib
import shap

model=joblib.load('./random_forest.joblib')
explainer=shap.TreeExplainer(model)


def Age(date):
    u=pd.Timestamp(date, tz=None)
    u=u.tz_convert(None)
    return (pd.Timestamp.today()-u).days+1

def length(string) :
    try :
        return(len(string))
    except TypeError :
        return 0

def nbdigits(string):
    try :
        return sum(c.isdigit() for c in string)
    except :
        print(string)
        

def augmentdf(df):
    output=pd.DataFrame.copy(df)
    output['tweet_frequence']=df['statuses_count']/df['age']
    output['followers_growth_rate']=df['followers_count']/df['age']
    output['friends_growth_rate']=df['friends_count']/df['age']
    output['friends_growth_rate']=df['favourites_count']/df['age']
    output['listed_growth_rate']=df['listed_count']/df['age']
    output['friends_followers_ratio']=df['friends_count']/(df['followers_count']+1)
    output['followers_friend_ratio']=df['followers_count']/(df['friends_count']+1)
    output['name_length']=df['name'].apply(length)
    output['screenname_length']=df['screen_name'].apply(length)
    output['name_digits']=df['name'].apply(nbdigits)
    output['screen_name_digits']=df['screen_name'].apply(nbdigits)
    output['description_length']=df['description'].apply(length)
    return(output)

ConsideredFeatures=['statuses_count','followers_count','favourites_count', 'friends_count', 'listed_count',
                   'default_profile', 'profile_use_background_image', 'verified', 'age', 'name', 'screen_name',
                   'description']

def findbot(name) :
    '''Also works with the id'''
    data=api.get_user(name)._json
    df=pd.DataFrame.from_dict(data, orient='index').T
    df['age']=df['created_at'].apply(Age)
    df=df[ConsideredFeatures]
    df=augmentdf(df)
    df=df.drop(columns=['description', 'name', 'screen_name'])
    shap_values=explainer.shap_values(df)
    rounded=[round(i,3) for i in shap_values[1][0]]
    dic=dict(zip(df.columns, rounded))
    return(round(model.predict_proba(df)[0][1],3), json.dumps(dic))
    #print(df)
