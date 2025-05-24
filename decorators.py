from functools import wraps
from flask import g, url_for
from werkzeug.utils import redirect


def loginrequired(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if g.user:
            return func(*args, **kwargs)
        else:
            return redirect(url_for("auth.login"))
    return inner




