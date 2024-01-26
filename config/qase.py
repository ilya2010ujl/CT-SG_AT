import os


class Qase:
    TOKEN = 'e2ebd282d170a00199b6d3e819bf6319d9d8f67bb20eecc9b6b2d5eb0a59d0b2'
    IS_DOC_UPDATE_NEEDED = 'False'
    # TOKEN = os.getenv('QASE_TOKEN') if os.getenv('QASE_TOKEN') is not None else False
    # IS_DOC_UPDATE_NEEDED = True if os.getenv('QASE_DOC') == 'True' else False

    API_DOMAIN = 'https://api.qase.io'
    FRONTEND_DOMAIN = 'https://app.qase.io'
    API_VERSION = 'v1'
    PROJECT = 'GS'