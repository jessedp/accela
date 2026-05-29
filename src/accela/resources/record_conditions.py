from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from .base import BaseResource, ListResponse, ResourceModel


@dataclass
class RecordCondition(ResourceModel):
    """Represents a condition associated with an Accela record."""

    id: int
    raw_json: Dict[str, Any] = field(default_factory=dict)

    action_by_department: Optional[Dict[str, Any]] = None
    action_by_user: Optional[Dict[str, Any]] = None
    active_status: Optional[Dict[str, Any]] = None
    additional_information: Optional[str] = None
    additional_information_plain_text: Optional[str] = None
    applied_date: Optional[datetime] = None
    applied_by_department: Optional[Dict[str, Any]] = None
    applied_by_user: Optional[Dict[str, Any]] = None
    disp_additional_information_plain_text: Optional[str] = None
    display_notice_in_agency: Optional[bool] = None
    display_notice_in_citizens: Optional[bool] = None
    display_notice_in_citizens_fee: Optional[bool] = None
    display_order: Optional[int] = None
    effective_date: Optional[datetime] = None
    expiration_date: Optional[datetime] = None
    group: Optional[Dict[str, Any]] = None
    inheritable: Optional[Dict[str, Any]] = None
    is_include_name_in_notice: Optional[bool] = None
    is_include_short_comments_in_notice: Optional[bool] = None
    long_comments: Optional[str] = None
    name: Optional[str] = None
    severity: Optional[str] = None
    short_comments: Optional[str] = None
    status: Optional[Dict[str, Any]] = None
    type: Optional[Dict[str, Any]] = None

    FIELD_MAPPING = {
        "actionbyDepartment": "action_by_department",
        "actionbyUser": "action_by_user",
        "activeStatus": "active_status",
        "additionalInformation": "additional_information",
        "additionalInformationPlainText": "additional_information_plain_text",
        "appliedDate": "applied_date",
        "appliedbyDepartment": "applied_by_department",
        "appliedbyUser": "applied_by_user",
        "dispAdditionalInformationPlainText": "disp_additional_information_plain_text",
        "displayNoticeInAgency": "display_notice_in_agency",
        "displayNoticeInCitizens": "display_notice_in_citizens",
        "displayNoticeInCitizensFee": "display_notice_in_citizens_fee",
        "displayOrder": "display_order",
        "effectiveDate": "effective_date",
        "expirationDate": "expiration_date",
        "group": "group",
        "id": "id",
        "inheritable": "inheritable",
        "isIncludeNameInNotice": "is_include_name_in_notice",
        "isIncludeShortCommentsInNotice": "is_include_short_comments_in_notice",
        "longComments": "long_comments",
        "name": "name",
        "severity": "severity",
        "shortComments": "short_comments",
        "status": "status",
        "type": "type",
    }

    DICT_FIELDS = [
        "actionbyDepartment",
        "actionbyUser",
        "activeStatus",
        "appliedbyDepartment",
        "appliedbyUser",
        "group",
        "inheritable",
        "status",
        "type",
    ]

    DATETIME_FIELDS = [
        "appliedDate",
        "effectiveDate",
        "expirationDate",
    ]


class RecordConditions(BaseResource):
    """Resource for interacting with Accela record conditions."""

    def list(
        self,
        record_id: str,
        fields: Optional[List[str]] = None,
        limit: int = 100,
        offset: int = 0,
    ) -> ListResponse[RecordCondition]:
        """
        List all conditions associated with a record with pagination support.

        Args:
            record_id: The ID of the record to get conditions for.
            fields: List of fields to include in the response.
            limit: Number of conditions per page, default 100.
            offset: Starting offset for pagination, default 0.

        Returns:
            ListResponse object with pagination support.
        """
        url = f"{self.client.BASE_URL}/records/{record_id}/conditions"
        params: Dict[str, Union[int, str]] = {"limit": limit, "offset": offset}

        if fields is not None and len(fields) > 0:
            params["fields"] = ",".join(fields)

        return self._list_resource(url, RecordCondition, params)
