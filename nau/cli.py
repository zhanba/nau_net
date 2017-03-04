#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
import click
from .network import login as nau_login
from .network import logout as nau_logout
from .network import test_network, network_use_condition
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
        click.echo("----------------NO USER!-------------")
    else:
        click.echo("---------------Current User is %s---------" % username)
    if test_network():
        click.echo("Current login to the network.")
        network_use_condition()
    else:
        click.echo("Current offline.")


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
