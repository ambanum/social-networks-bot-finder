#!/usr/bin/env python


import click
from botfinder.bot_classifier import findbot, findbot_rawjson, findbot_filename


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
def main(rawjson, username, jsonfile):
    """Command line utility to estimate the probability of a twitter user to be a bot"""
    if rawjson:
        print(findbot_rawjson(rawjson))
    elif username:
        print(findbot(username))
    elif jsonfile:
        print(findbot_filename(jsonfile))
    else:
        ctx = click.get_current_context()
        click.echo(ctx.get_help())
        ctx.exit()


if __name__ == "__main__":
    main()
