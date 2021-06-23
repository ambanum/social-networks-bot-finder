# social-networks-bot-finder

A simple classifier for twitter bot accounts based on Random Forest Algorithm

See our [Methodology](./explanation.md) for bot detection

# Install

Do `pip install -r requirements.txt` to install needed packages

# Usage

To get the bot score probability of a user account, simply launch

```
./bot-finder username

# which is equivalent to

python3 BotClassifier.py username
```

## Example

```
python3 BotClassifier.py ambnum
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

If for any reason, simply installing the required package is not enough to launch the command and you get errors, you can try and setup a virtual env

```
pip3 install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
pip install --upgrade pip
pip install Cython
pip install numpy --no-use-pep517
pip install pandas
pip install tweepy
pip install joblib
pip install shap
```

then try again
