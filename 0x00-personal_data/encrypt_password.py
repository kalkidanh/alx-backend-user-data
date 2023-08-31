#!/usr/bin/env python3
""" Function that accepts a string argument name password and
returns a hashed password, which is a byte string."""


import bcrypt


def hash_password(password: str) -> bytes:
    """ Return a hashed password."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Return true if password is valid and false otherwise."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
