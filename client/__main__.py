#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging
import click
import requests
from tenacity import(
    retry,
    stop_after_attempt,
    stop_after_delay
)


@click.group("client")
@click.option("--endpoint", "-e", default="http://localhost:8080/", help="The target endpoint")
@click.pass_context
def cli(ctx, endpoint: str) -> None:
    """The base command"""
    ctx.ensure_object(dict)
    ctx.obj["endpoint"] = endpoint


@cli.command("attempts")
@click.pass_context
@retry(stop_after_attempt(10))
def attempts(ctx) -> int:
    """This command will retry forever"""
    endpoint: str = ctx.obj["endpoint"]
    response = requests.get(endpoint)
    if response.status_code == 200:
        return 0
    return 1

@cli.command("forever")
@click.pass_context
@retry
def forever(ctx) -> int:
    """This command will retry forever"""
    endpoint: str = ctx.obj["endpoint"]
    response = requests.get(endpoint)
    if response.status_code == 200:
        return 0
    return 1


def main() -> int:
    """The main script entrypoint"""
    return cli(prog_name="client")


if __name__ == '__main__':
    main()
