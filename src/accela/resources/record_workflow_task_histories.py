from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from .base import BaseResource, ListResponse, ResourceModel


@dataclass
class RecordWorkflowTaskHistory(ResourceModel):
    """Represents a workflow task history item associated with an Accela record."""

    id: str
    raw_json: Dict[str, Any] = field(default_factory=dict)

    action: Optional[str] = None
    actionby_department: Optional[Dict[str, Any]] = None
    actionby_user: Optional[Dict[str, Any]] = None
    approval: Optional[str] = None
    assign_email_display: Optional[str] = None
    assigned_date: Optional[datetime] = None
    assigned_to_department: Optional[Dict[str, Any]] = None
    assigned_user: Optional[Dict[str, Any]] = None
    billable: Optional[bool] = None
    comment: Optional[str] = None
    comment_display: Optional[str] = None
    comment_public_visible: Optional[List[str]] = None
    current_task_id: Optional[str] = None
    days_due: Optional[int] = None
    description: Optional[str] = None
    disposition_note: Optional[str] = None
    due_date: Optional[datetime] = None
    end_time: Optional[datetime] = None
    estimated_due_date: Optional[datetime] = None
    estimated_hours: Optional[float] = None
    hours_spent: Optional[float] = None
    in_possession_time: Optional[float] = None
    is_active: Optional[bool] = None
    is_completed: Optional[bool] = None
    last_modified_date: Optional[datetime] = None
    last_modified_date_string: Optional[str] = None
    next_task_id: Optional[str] = None
    over_time: Optional[str] = None
    process_code: Optional[str] = None
    record_id: Optional[Dict[str, Any]] = None
    service_provider_code: Optional[str] = None
    start_time: Optional[datetime] = None
    status: Optional[Dict[str, Any]] = None
    status_date: Optional[datetime] = None
    track_start_date: Optional[datetime] = None

    FIELD_MAPPING = {
        "action": "action",
        "actionbyDepartment": "actionby_department",
        "actionbyUser": "actionby_user",
        "approval": "approval",
        "assignEmailDisplay": "assign_email_display",
        "assignedDate": "assigned_date",
        "assignedToDepartment": "assigned_to_department",
        "assignedUser": "assigned_user",
        "billable": "billable",
        "comment": "comment",
        "commentDisplay": "comment_display",
        "commentPublicVisible": "comment_public_visible",
        "currentTaskId": "current_task_id",
        "daysDue": "days_due",
        "description": "description",
        "dispositionNote": "disposition_note",
        "dueDate": "due_date",
        "endTime": "end_time",
        "estimatedDueDate": "estimated_due_date",
        "estimatedHours": "estimated_hours",
        "hoursSpent": "hours_spent",
        "id": "id",
        "inPossessionTime": "in_possession_time",
        "isActive": "is_active",
        "isCompleted": "is_completed",
        "lastModifiedDate": "last_modified_date",
        "lastModifiedDateString": "last_modified_date_string",
        "nextTaskId": "next_task_id",
        "overTime": "over_time",
        "processCode": "process_code",
        "recordId": "record_id",
        "serviceProviderCode": "service_provider_code",
        "startTime": "start_time",
        "status": "status",
        "statusDate": "status_date",
        "trackStartDate": "track_start_date",
    }

    DICT_FIELDS = [
        "actionbyDepartment",
        "actionbyUser",
        "assignedToDepartment",
        "assignedUser",
        "recordId",
        "status",
    ]

    DATETIME_FIELDS = [
        "assignedDate",
        "dueDate",
        "endTime",
        "estimatedDueDate",
        "lastModifiedDate",
        "startTime",
        "statusDate",
        "trackStartDate",
    ]

    BOOL_FIELDS = [
        "billable",
        "isActive",
        "isCompleted",
    ]


class RecordWorkflowTaskHistories(BaseResource):
    """Resource for interacting with Accela record workflow task histories."""

    def list(
        self,
        record_id: str,
        fields: Optional[List[str]] = None,
        limit: int = 100,
        offset: int = 0,
    ) -> ListResponse[RecordWorkflowTaskHistory]:
        """
        List all workflow task histories associated with a record with pagination support.

        Args:
            record_id: The ID of the record to get workflow task histories for.
            fields: List of fields to include in the response.
            limit: Number of histories per page, default 100.
            offset: Starting offset for pagination, default 0.

        Returns:
            ListResponse object with pagination support.
        """
        url = f"{self.client.BASE_URL}/records/{record_id}/workflowTasks/histories"
        params: Dict[str, Union[int, str]] = {"limit": limit, "offset": offset}

        if fields is not None and len(fields) > 0:
            params["fields"] = ",".join(fields)

        return self._list_resource(url, RecordWorkflowTaskHistory, params)
