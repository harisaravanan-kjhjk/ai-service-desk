from database.level_repository import (
    get_level as repo_get_level,
    get_specializtion as repo_get_specialization,
    insert_level as repo_insert_level,
    assigned_devs as repo_assigned_devs,
    get_dev_by_level as repo_get_dev_by_level,
    debug_levels as repo_debug_levels
)


def get_level(dev_id):
    return repo_get_level(dev_id)


def get_specializtion(dev_id):
    return repo_get_specialization(dev_id)


def insert_level(dev_id, level, specialization):
    return repo_insert_level(
        dev_id,
        level,
        specialization
    )


def assigned_devs():
    return repo_assigned_devs()


def get_dev_by_level(level):
    return repo_get_dev_by_level(level)


def debug_levels():
    return repo_debug_levels()