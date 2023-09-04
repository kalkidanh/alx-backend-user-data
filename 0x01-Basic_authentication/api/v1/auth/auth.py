#!usr/bin/env python3
""" Base class template to implement authentication systems."""
from typing import List, TypeVar
from flask import request


class Auth():
    """ Define the authentication system."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Returns False """
        return False

    def authorization_header(self, request=None) -> str:
        """return the value of the header request Authorization"""
        if request:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None - request will be the Flask request object"""
        return None
