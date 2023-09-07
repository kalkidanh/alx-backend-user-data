#!/usr/bin/env python3
""" Base class template to implement authentication systems."""
from typing import List, TypeVar
from flask import request


class Auth():
    """ Define the authentication system."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Returns true if the path is not in the list. """
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
        """return the value of the header request Authorization"""
        if request:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None - request will be the Flask request object"""
        return None
