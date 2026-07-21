from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware

limiter = Limiter(key_func=get_remote_address)

def add_rate_limit_middleware(app):
    app.state.limiter = limiter
    app.add_middleware(SlowAPIMiddleware)