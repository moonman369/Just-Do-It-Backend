from django.utils.crypto import get_random_string

def uuid():
    return get_random_string(30)

def uuid_task():
    return get_random_string(50)