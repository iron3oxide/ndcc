from prompt_toolkit.validation import Validator


def _validate_collection_number(text: str) -> bool:
    return text.isdigit() and 1 < int(text) < 32


def _validate_picks(text: str) -> bool:
    for pick in text.split():
        if not pick.isdigit() or not 0 < int(pick) < 271:
            return False
    return True


def _validate_collection_name(text: str) -> bool:
    return bool(text)


collection_num_validator: Validator = Validator.from_callable(
    _validate_collection_number,
    "Number of collections must be between 2 and 32",
    move_cursor_to_end=True
)

pick_validator: Validator = Validator.from_callable(
    _validate_picks,
    "One or more picks is invalid. Picks must be ints between 1 and 270.",
    move_cursor_to_end=True
)

collection_name_validator: Validator = Validator.from_callable(
    _validate_collection_name,
    "Collection name/identifier cannot be empty",
    move_cursor_to_end=True
)
