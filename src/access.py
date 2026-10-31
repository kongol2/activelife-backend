def validate_access(membership):
    if not membership["is_active"]:
        return False

    if membership["has_debt"]:
        return False

    return True
