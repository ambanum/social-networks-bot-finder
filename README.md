# social-networks-bot-finder

A simple classifier for twitter bot accounts based on Random Forest Algorithm

# install

Do `pip install -r requirements.txt` to install needed packages

# Usage

To get the bot score probability of a user account, simply launch

```
python3 BotClassifier.py username
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
