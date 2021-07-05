from pathlib import Path
import tempfile

TMP_DIR = Path(tempfile.gettempdir())

PACKAGE_INSTALL_DIR = Path(__file__).parent

SNSCRAPE_TO_API = {
    "username": "name",
    "displayname": "screen_name",
    "created": "created_at",
    "followersCount": "followers_count",
    "friendsCount": "friends_count",
    "statusesCount": "statuses_count",
    "favouritesCount": "favourites_count",
    "listedCount": "listed_count",
}

FEATURES = [
    "statuses_count",
    "followers_count",
    "favourites_count",
    "friends_count",
    "listed_count",
    "default_profile",
    "profile_use_background_image",
    "verified",
    "age",
    "name",
    "screen_name",
    "description",
]