from database.user_repository import (
    store_user as repo_store_user,
    get_user as repo_get_user,
    get_developer as repo_get_developer,
    get_occupied_developers as repo_get_occupied_developers,
    get_by_id as repo_get_by_id,
    get_by_name as repo_get_by_name
)


def store_user(name, password, role):
    return repo_store_user(
        name,
        password,
        role
    )


def get_user(name):
    return repo_get_user(name)


def get_developer():
    return repo_get_developer()


def get_occupied_developers(level):
    return repo_get_occupied_developers(level)


def get_by_id(user_id):
    return repo_get_by_id(user_id)


def get_by_name(name):
    return repo_get_by_name(name)