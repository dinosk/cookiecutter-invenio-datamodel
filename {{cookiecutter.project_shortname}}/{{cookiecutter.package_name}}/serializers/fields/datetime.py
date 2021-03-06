"""Date string field."""

from __future__ import absolute_import, print_function

import arrow
from arrow.parser import ParserError
from marshmallow import fields, missing


class DateString(fields.Date):
    """ISO8601-formatted date string."""

    def _serialize(self, value, attr, obj):
        """Serialize an ISO8601-formatted date."""
        try:
            return super(DateString, self)._serialize(
                arrow.get(value).date(), attr, obj)
        except ParserError:
            return missing

    def _deserialize(self, value, attr, data):
        """Deserialize an ISO8601-formatted date."""
        return super(DateString, self)._deserialize(value, attr,
                                                    data).isoformat()
