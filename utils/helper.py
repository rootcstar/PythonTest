import uuid
def generate_uuid():
    return str(uuid.uuid4())


def check_none_or_empty_string(value, field_name):
    if value is None or (isinstance(value, str) and value.strip() == ""):
        return False
    return True