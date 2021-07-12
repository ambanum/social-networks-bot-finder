<img src="https://disinfo.quaidorsay.fr/assets/img/logo.png" width="140">

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
botfinder --username ambnum
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

## Using Docker

### "regular" image

```sh
# build and run image yourself
docker build --tag botfinder:latest -f Dockerfile .
docker run -it -d --rm botfinder

# or pull from Dockerhub
#TODO

# execute your command in the container
docker exec -it botfinder botfinder --username ambnum
```

### ARM/M1 image (using conda)

Note that you need to activate the conda env everytime you want to use `docker exec` which slows things down... See [this article](https://pythonspeed.com/articles/activate-conda-dockerfile) for a description of the issue.

```sh
# build and run image yourself
docker build  --tag botfinder:latest -f Dockerfile.conda .
docker run -it -d --name botfinder --rm botfinder:latest

# execute your command in the container
docker exec -it botfinder conda init bash && conda activate botfinder && botfinder --username ambnum
```

# Deployment

This package is deployed on pypi as a package named `social-networks-bot-finder`. So that it can be installed using pip
We are using `twine` for this

```
pip install twine
npm install -g semver # for consistent package number generation
pip install gitchangelog # to generate changelog automatically based on git commits
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

## ERROR: Could not detect requirement name...

```
ERROR: Could not detect requirement name for 'git+https://github.com/JustAnotherArchivist/snscrape.git', please specify one with #egg=your_package_name
```

In requirements.txt file, you have to add `#egg=your_package_name` to github repository url.
In this case, replace `git+https://github.com/JustAnotherArchivist/snscrape.git`by `git+https://github.com/JustAnotherArchivist/snscrape.git#egg=snscrape`

## Install on M1/ARM processors

As of today, the easiest way to install the package and its dependencies on a M1/ARM chip is via [`conda`](https://conda.io/)

#### Install `conda`

We recommend [downloading and installing](https://docs.conda.io/en/latest/miniconda.html#installing) the python 3.9 version of conda. The `miniconda` distribution is enough for our purpose.

#### Navigate to root of repository and pull the latest changes

#### Create a new conda environment

`conda env create --name botfinder python=3.9 -f environment.yml`

and activate it :

`conda activate botfinder`

#### Install botfinder

`python -m pip install -e .`

#### Check that it worked

```sh
botfinder --help
```

## Command line is too slow

In order to profile the execution of the command line, you can use a profiler named `tuna`

```
pip install tuna

time python -X importtime botfinder-dev.py --rawjson '{"_id":"60d352cf13b64d38e9a184dd","id":"1106210510058463233","platformId":"twitter","created":"2019-03-14T15:08:32.000Z","createdAt":"2021-06-23T15:27:11.019Z","description":"Social Enterprise Digital Marketing Agency - Empowering our staff with knowledge & skills to provide the best quality marketing services  WEB | PPC | SEO & more","displayname":"Ground Up Digital","favouritesCount":500,"followersCount":583,"friendsCount":592,"linkUrl":"https://groundup.digital/","listedCount":4,"location":"Leeds","mediaCount":164,"profileImageUrl":"https://pbs.twimg.com/profile_images/1106606764584288256/vQ6Fs2y__normal.png","statusesCount":541,"updatedAt":"2021-06-23T15:27:11.019Z","username":"GroundUpDigital","verified":false}' 2> import.log

tuna import.log
```
