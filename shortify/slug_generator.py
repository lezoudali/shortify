import random

CHARS = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"
         "abcdefghijklmnopqrstuvwxyz"
         "0123456789")


def random_slug_generator(length=7):
    return ''.join([random.choice(CHARS) for _ in range(length)])
