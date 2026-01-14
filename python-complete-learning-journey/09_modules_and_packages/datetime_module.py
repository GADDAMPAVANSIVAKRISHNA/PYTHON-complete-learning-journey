"""Datetime module examples and practice."""

from datetime import datetime, timedelta


def now_iso():
    return datetime.utcnow().isoformat()


# Practice (5):
# 1) Parse different date formats.
# 2) Calculate difference between two datetimes.
# 3) Convert between timezones (using pytz or zoneinfo).
# 4) Add business days to a date (skip weekends).
# 5) Format dates in different human-readable forms.

if __name__ == "__main__":
    print(now_iso())
    print('add 5 days', (datetime.utcnow() + timedelta(days=5)).isoformat())
