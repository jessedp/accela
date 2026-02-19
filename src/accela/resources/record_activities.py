from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

from .base import BaseResource, ListResponse, ResourceModel


@dataclass
class RecordActivity(ResourceModel):
    """Represents an activity associated with an Accela record."""

    id: int
    raw_json: Dict[str, Any] = field(default_factory=dict)

    activity_status: Optional[Dict[str, Any]] = None
    assigned_department: Optional[Dict[str, Any]] = None
    assigned_user: Optional[Dict[str, Any]] = None
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    name: Optional[str] = None
    priority: Optional[Dict[str, Any]] = None
    start_date: Optional[datetime] = None
    type: Optional[Dict[str, Any]] = None
    record_id: Optional[str] = None


    FIELD_MAPPING = {
        "activityStatus": "activity_status",
        "assignedDepartment": "assigned_department",
        "assignedUser": "assigned_user",
        "description": "description",
        "dueDate": "due_date",
        "id": "id",
        "name": "name",
        "priority": "priority",
        "startDate": "start_date",
        "type": "type",
        "recordId": "record_id",
    }

    DICT_FIELDS = [
        "activityStatus",
        "assignedDepartment",
        "assignedUser",
        "priority",
        "type",
    ]

    DATETIME_FIELDS = [
        "dueDate",
        "startDate",
    ]


class RecordActivities(BaseResource):
    """Resource for interacting with Accela record activities."""

    def list(
        self,
        record_id: str,
        fields: Optional[List[str]] = None,
        limit: int = 100,
        offset: int = 0,
    ) -> ListResponse[RecordActivity]:
        """
        List all activities associated with a record with pagination support.

        Args:
            record_id: The ID of the record to get activities for.
            fields: List of fields to include in the response.
            limit: Number of activities per page, default 100.
            offset: Starting offset for pagination, default 0.

        Returns:
            ListResponse object with pagination support.
        """
        url = f"{self.client.BASE_URL}/records/{record_id}/activities"
        params: Dict[str, Union[int, str]] = {"limit": limit, "offset": offset}

        if fields is not None and len(fields) > 0:
            params["fields"] = ",".join(fields)

        return self._list_resource(url, RecordActivity, params)
