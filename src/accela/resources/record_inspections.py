from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from .base import BaseResource, ListResponse, ResourceModel


@dataclass
class RecordInspection(ResourceModel):
    """Represents an inspection associated with an Accela record."""

    id: str
    raw_json: Dict[str, Any] = field(default_factory=dict)

    carryover_flag: Optional[str] = None
    category: Optional[str] = None
    comment_display: Optional[str] = None
    comment_public_visible: Optional[List[str]] = None
    completed_ampm: Optional[str] = None
    completed_date: Optional[str] = None
    completed_time: Optional[str] = None
    inspector_full_name: Optional[str] = None
    inspector_id: Optional[str] = None
    is_auto_assign: Optional[str] = None
    major_violation: Optional[int] = None
    priority: Optional[float] = None
    public_visible: Optional[str] = None
    record_id: Optional[Dict[str, Any]] = None
    request_ampm: Optional[str] = None
    request_date: Optional[str] = None
    request_time: Optional[str] = None
    requestor_first_name: Optional[str] = None
    requestor_last_name: Optional[str] = None
    required_inspection: Optional[str] = None
    result_type: Optional[str] = None
    schedule_date: Optional[str] = None
    service_provider_code: Optional[str] = None
    status: Optional[Dict[str, Any]] = None
    submit_ampm: Optional[str] = None
    submit_date: Optional[str] = None
    submit_time: Optional[str] = None
    total_score: Optional[int] = None
    type: Optional[Dict[str, Any]] = None
    units: Optional[float] = None

    FIELD_MAPPING = {
        "carryoverFlag": "carryover_flag",
        "category": "category",
        "commentDisplay": "comment_display",
        "commentPublicVisible": "comment_public_visible",
        "completedAMPM": "completed_ampm",
        "completedDate": "completed_date",
        "completedTime": "completed_time",
        "id": "id",
        "inspectorFullName": "inspector_full_name",
        "inspectorId": "inspector_id",
        "isAutoAssign": "is_auto_assign",
        "majorViolation": "major_violation",
        "priority": "priority",
        "publicVisible": "public_visible",
        "recordId": "record_id",
        "requestAMPM": "request_ampm",
        "requestDate": "request_date",
        "requestTime": "request_time",
        "requestorFirstName": "requestor_first_name",
        "requestorLastName": "requestor_last_name",
        "requiredInspection": "required_inspection",
        "resultType": "result_type",
        "scheduleDate": "schedule_date",
        "serviceProviderCode": "service_provider_code",
        "status": "status",
        "submitAMPM": "submit_ampm",
        "submitDate": "submit_date",
        "submitTime": "submit_time",
        "totalScore": "total_score",
        "type": "type",
        "units": "units",
    }

    DICT_FIELDS = [
        "recordId",
        "status",
        "type",
    ]


class RecordInspections(BaseResource):
    """Resource for interacting with Accela record inspections."""

    def list(
        self,
        record_id: str,
        fields: Optional[List[str]] = None,
        limit: int = 100,
        offset: int = 0,
    ) -> ListResponse[RecordInspection]:
        """
        List all inspections associated with a record with pagination support.

        Args:
            record_id: The ID of the record to get inspections for.
            fields: List of fields to include in the response.
            limit: Number of inspections per page, default 100.
            offset: Starting offset for pagination, default 0.

        Returns:
            ListResponse object with pagination support.
        """
        url = f"{self.client.BASE_URL}/records/{record_id}/inspections"
        params: Dict[str, Union[int, str]] = {"limit": limit, "offset": offset}

        if fields is not None and len(fields) > 0:
            params["fields"] = ",".join(fields)

        return self._list_resource(url, RecordInspection, params)
