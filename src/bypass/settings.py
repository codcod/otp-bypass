import os
import pathlib

BASE_DIR = pathlib.Path(__file__).parent.parent.parent
# PACKAGE_NAME = 'valet'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '{levelname} {name} {message}',
            'style': '{',
        },
        'verbose': {
            'format': '{asctime} - {name}:{module} - {levelname} - {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {'class': 'logging.StreamHandler', 'formatter': 'simple'},
        'file': {
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'server.log',
            'formatter': 'verbose',
            'level': 'DEBUG',
            'mode': 'w',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': os.getenv('APP_LOG_LEVEL', 'DEBUG'),
    },
    'loggers': {
        'asyncio': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'aiosqlite': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'gunicorn.glogging': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'aiohttp': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
