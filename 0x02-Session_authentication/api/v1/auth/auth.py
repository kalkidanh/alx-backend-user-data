#!/usr/bin/env python3
""" Base class template to implement authentication systems."""
from os import getenv
from typing import List, TypeVar
from flask import request


class Auth():
    """ Define the authentication system."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Return true if the path is not in the list. """
        if not excluded_paths or not len(excluded_paths) or not path:
            return True
        for element in excluded_paths:
            if "*" in element:
                if path.startswith(element.replace("*", "")):
                    return False
        if path in excluded_paths or f'{path}/' in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Return the value of the header request authorization."""
        if request:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Return None - request will be the Flask request object."""
        return None

    def session_cookie(self, request=None):
        """ Return the cookie value from a request."""
        if request is None:
            return None
        session_name = getenv('SESSION_NAME')
        return request.cookies.get(session_name)
