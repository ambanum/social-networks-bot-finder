# social-networks-bot-finder

A simple classifier for twitter bot accounts based on Random Forest Algorithm

See our [Methodology](./explanation.md) for bot detection

# Install

Do `pip install -r requirements.txt` to install needed packages

# Usage

To get the bot score probability of a user account, you can do so

```
# by username: this will use snscrape to get the data
./bot-finder.py --name username

# by user data you just got from snscrape
SNSCRAPE_USER=$(snscrape --with-entity --max-results 0 --jsonl twitter-user username)
echo "./bot-finder.py --rawjson '$SNSCRAPE_USER'"
# -> and launch the result of this command

# by user data you just got from snscrape and stored into a file
./bot-finder.py --jsonfile ./filepath.json

```

## Example

```
./bot-finder.py --name ambnum
```

will return

```json
{
  "botScore": 0.14,
  "details": {
    "statuses_count": -0.08,
    "followers_count": -0.195,
    "favourites_count": 0.009,
    "friends_count": -0.036,
    "listed_count": -0.153,
    "default_profile": -0.041,
    "profile_use_background_image": 0,
    "verified": 0.013,
    "age": -0.003,
    "tweet_frequence": -0.013,
    "followers_growth_rate": -0.019,
    "friends_growth_rate": 0,
    "listed_growth_rate": -0.068,
    "friends_followers_ratio": -0.009,
    "followers_friend_ratio": -0.004,
    "name_length": -0.001,
    "screenname_length": 0,
    "name_digits": -0,
    "screen_name_digits": -0.002,
    "description_length": -0.009
  }
}
```

# Troubleshooting

## Illegal instruction: 4

If your installation fail you may try to launch a virtual environment :

```
pip3 install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
pip install --upgrade pip
pip install Cython
pip install numpy --no-use-pep517
pip install pandas
pip install joblib
pip install shap
```

And try to install again.
