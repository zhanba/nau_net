#!/usr/bin/python
# -*- coding: utf-8 -*-

import click
from nau.network import login as nau_login
from nau.network import logout as nau_logout
from .config import Config


@click.group()
def cli():
    """ NAU school network CLI.
        add user
        remove user
        login status
        login to current user
        logout
    """
    pass

@click.command()
def login():
    nau_login()

@click.command()
def logout():
    nau_logout()

@click.command()
def status():
    pass

@click.command()
@click.option('--name', prompt=True)
@click.option('--password', prompt=True)
def add(name, password):
    Config.add_user(name, password)
    click.echo('Hello %s!' % name)

@click.command()
def remove():
    Config.remove_user()

cli.add_command(login)
cli.add_command(logout)
cli.add_command(status)
cli.add_command(add)
cli.add_command(remove)
