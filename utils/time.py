from datetime import timedelta


def parse_time(time_string: str):
    """
    Converts:
    10m -> 10 minutes
    2h -> 2 hours
    1d -> 1 day
    """

    unit = time_string[-1]
    amount = int(time_string[:-1])

    if unit == "s":
        return timedelta(seconds=amount)

    elif unit == "m":
        return timedelta(minutes=amount)

    elif unit == "h":
        return timedelta(hours=amount)

    elif unit == "d":
        return timedelta(days=amount)

    else:
        return None
