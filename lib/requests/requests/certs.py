#!/usr/bin/env python

"""
THIS SOURCE FILE HAS BEEN ADAPTED FROM THE ORIGINAL SOURCE FILE, UTILIZING
RELATIVE IMPORTS

requests.certs
~~~~~~~~~~~~~~

This module returns the preferred default CA certificate bundle. There is
only one — the one from the certifi package.

If you are packaging Requests, e.g., for a Linux distribution or a managed
environment, you can change the definition of where() to return a separately
packaged CA bundle.
"""
from ...certifi.certifi import where

if __name__ == "__main__":
    print(where())
