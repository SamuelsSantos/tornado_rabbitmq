from decouple import config

DEBUG = config('DEBUG', default=False, cast=bool)
RABBIT_HOST = config('RABBIT_HOST', default='localhost')
RABBIT_PORT = config('RABBIT_PORT', default=5672, cast=int)
RABBIT_USER = config('RABBIT_USER', default='guest')
RABBIT_PASS = config('RABBIT_PASS', default='guest')
