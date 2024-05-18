# We will use this file to apply more settings that are docker specific
# to the docker container. Such as the midlware settings for example .

if IN_DOCKER:  # type: ignore # noqa: F821
    # print("Running in Docker mode ....")
    assert MIDDLEWARE[:1] == [  # type: ignore # noqa: F821
        'django.middleware.security.SecurityMiddleware',
    ]
