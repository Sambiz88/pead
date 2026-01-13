from datetime import datetime
import zoneinfo


def is_call_in_am(date_str: str) -> bool:
    dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    return dt.hour < 12

