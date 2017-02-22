#!/usr/bin/python
# -*- coding: utf-8 -*-

import click
from nau.network import login as nau_login
from nau.network import logout as nau_logout

@click.group()
def cli():
    """ NAU school network CLI. """
    pass

@click.command()
def login():
    nau_login()

@click.command()
def logout():
    nau_logout()

cli.add_command(login)
cli.add_command(logout)
