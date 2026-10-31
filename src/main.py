from access import validate_access


def main():
    membership = {
        "client_id": 101,
        "is_active": True,
        "has_debt": False
    }

    result = validate_access(membership)

    print(f"Access granted: {result}")


if __name__ == "__main__":
    main()
