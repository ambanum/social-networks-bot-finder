# social-networks-bot-finder

A simple classifier for twitter bot accounts based on Random Forest Algorithm

See our [Methodology](./explanation.md) for bot detection

## Install for common usage with pip

Create a virtual env if needed

```
pip3 install virtualenv
virtualenv -p python3 social-networks-bot-finder
source social-networks-bot-finder/bin/activate
```

Install

```
pip3 install social-networks-bot-finder
```

Then you can launch `botfinder`

## Install for development

```
git clone https://github.com/ambanum/social-networks-bot-finder
cd social-networks-bot-finder
```

### Virtual env

We strongly recommend that you use a virtual env for any development in python

For this

```
pip3 install virtualenv
virtualenv -p python3 social-networks-bot-finder
source social-networks-bot-finder/bin/activate
```

### build on local

If you do not want to develop but just use the software, do

```
./build.sh
```

Then you can use `botfinder` as an executable command

### use for development with no build

```
pip3 install -r requirements.txt
```

Then you can use `./botfinder-dev.py` as an executable command

# Usage

To get the bot score probability of a user account, you can do so

```
# by username: this will use snscrape to get the data
botfinder --name username

# by user data you just got from snscrape
SNSCRAPE_USER=$(snscrape --with-entity --max-results 0 --jsonl twitter-user username)
echo "botfinder --rawjson '$SNSCRAPE_USER'"
# -> and launch the result of this command

# by user data you just got from snscrape and stored into a file
botfinder --jsonfile ./filepath.json

```

## Example

```
botfinder --name ambnum
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

# Deployment

This package is deployed on pypi as a package named `social-networks-bot-finder`. So that it can be installed using pip
We are using `twine` for this

```
pip install twine
npm install -g semver # for consistent package number generation
```

## Authentication on pyPi

In order to not set your username and password again and again, you can set them using thos

```
keyring set https://upload.pypi.org/legacy/ username
```

## Deploy a new release

A new release should come with a new version
We are using semver to generate consistent package number

```
./release.sh
# org
./release.sh patch # for small fixes
./release.sh minor # for minor features
./release.sh major # for breaking changes
```

This will bum the version in `botfinder/version.py` and create a git tag

# Troubleshooting

## Illegal instruction: 4

If your installation fail, it might be because you're not using a virtual environment :

```
pip3 install virtualenv
virtualenv -p python3 social-networks-bot-finder
source social-networks-bot-finder/bin/activate
./build.sh
```
