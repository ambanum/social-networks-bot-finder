#!/usr/bin/env python


import click
import os
from bot_classifier import findbot, findbot_rawjson, findbot_filename


@click.command()
@click.option("--username", required=False, help="a twitter username")
@click.option(
    "--rawjson",
    required=False,
    help="a JSON string gotten from snscrape with `snscrape --with-entity --max-results 0 --jsonl twitter-user username`",
)
@click.option(
    "--jsonfile", required=False, help="a json file path containing a snscrape user "
)
def cli(rawjson, username, jsonfile):
    """Command line utility to estimate the probability of a twitter user to be a bot"""
    if rawjson:
        print(findbot_rawjson(rawjson))
    elif username:
        print(findbot(username))
    elif jsonfile:
        print(findbot_filename(jsonfile))
    else:
        os.system("./bot-finder.py --help")


if __name__ == "__main__":
    cli()