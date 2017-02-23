#!/usr/bin/python
# -*- coding: utf-8 -*-

import click
from .network import login as nau_login
from .network import logout as nau_logout
from .config import get_config_status, add_user, remove_user

@click.group()
def cli():
    """ NAU school network CLI."""
    pass

@click.command()
def login():
    """login to network"""
    nau_login()

@click.command()
def logout():
    """logout network"""
    nau_logout()

@click.command()
def status():
    """show current user and network status"""
    username = get_config_status()
    if username is None:
        print("----------------NO USER!-------------")
    else:
        print("---------------Current User is %s---------" % username)

@click.command()
@click.option('--username', prompt=True)
@click.option('--password', prompt=True)
def add(username, password):
    """
    add user for the network
    --username
    --password
    """
    add_user(username, password)
    click.echo('Add user %s successful!' % username)

@click.command()
def remove():
    """remove current account(include username and password)"""
    remove_user()
    click.echo("Done!")

cli.add_command(login)
cli.add_command(logout)
cli.add_command(status)
cli.add_command(add)
cli.add_command(remove)
