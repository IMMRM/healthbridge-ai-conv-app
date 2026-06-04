from decimal import Decimal
from datetime import date, datetime


def serialize_model(instance, fields):

    if not instance:
        return None

    serialized_data = {}

    for field in fields:

        value = getattr(instance, field, None)

        # Handle dates
        if isinstance(value, (date, datetime)):

            serialized_data[field] = (
                value.isoformat()
            )

        # Handle Decimal
        elif isinstance(value, Decimal):

            serialized_data[field] = float(value)

        else:

            serialized_data[field] = value

    return serialized_data