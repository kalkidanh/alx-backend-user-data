#!/usr/bin/env python3
""" Session class that inherits from Auth."""
from models.user import User
from uuid import uuid4
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ A session authentication class inherited from Auth."""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ A function that creates a Session ID for a user_id."""
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ A method that returns a user ID based on the session ID."""
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)
