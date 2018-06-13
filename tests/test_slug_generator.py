from shortify.slug_generator import random_slug_generator


def test_should_generate_random_slugs():
    slugs = [random_slug_generator() for _ in range(5)]

    assert len(slugs) == len(set(slugs))
