from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Any, Dict, List, Optional, Union

from .base import BaseResource, ListResponse
from .records import Record

class MyRecords(BaseResource):
    """Resource for interacting with the current user's records."""

    def list(
        self,
        limit: int = 100,
        offset: int = 0,
        type: Optional[str] = None,  # noqa
        opened_date_from: Optional[Union[date, datetime]] = None,
        opened_date_to: Optional[Union[date, datetime]] = None,
        custom_id: Optional[str] = None,
        module: Optional[str] = None,
        status: Optional[str] = None,
        assigned_date_from: Optional[Union[date, datetime]] = None,
        assigned_date_to: Optional[Union[date, datetime]] = None,
        completed_date_from: Optional[Union[date, datetime]] = None,
        completed_date_to: Optional[Union[date, datetime]] = None,
        status_date_from: Optional[Union[date, datetime]] = None,
        status_date_to: Optional[Union[date, datetime]] = None,
        update_date_from: Optional[Union[date, datetime]] = None,
        update_date_to: Optional[Union[date, datetime]] = None,
        completed_by_department: Optional[str] = None,
        completed_by_user: Optional[str] = None,
        closed_date_from: Optional[Union[date, datetime]] = None,
        closed_date_to: Optional[Union[date, datetime]] = None,
        closed_by_department: Optional[str] = None,
        closed_by_user: Optional[str] = None,
        record_class: Optional[str] = None,
        types: Optional[str] = None,
        modules: Optional[str] = None,
        status_types: Optional[str] = None,
        expand: Optional[List[str]] = None,
        expand_custom_forms: Optional[str] = None,
        fields: Optional[List[str]] = None,
    ) -> ListResponse[Record]:
        """
        List the current user's records with pagination and filtering.
        """
        url = f"{self.client.BASE_URL}/records/mine"
        params: Dict[str, Any] = {"limit": limit, "offset": offset}

        def format_date_param(date_param):
            if date_param is None:
                return None
            if isinstance(date_param, date) and not isinstance(date_param, datetime):
                date_param = datetime.combine(date_param, datetime.min.time())
            if isinstance(date_param, datetime) and date_param.tzinfo is None and self.client.timezone:
                date_param = date_param.replace(tzinfo=self.client.timezone)
            return date_param.isoformat()

        filter_params = {
            "type": type,
            "openedDateFrom": format_date_param(opened_date_from),
            "openedDateTo": format_date_param(opened_date_to),
            "customId": custom_id,
            "module": module,
            "status": status,
            "assignedDateFrom": format_date_param(assigned_date_from),
            "assignedDateTo": format_date_param(assigned_date_to),
            "completedDateFrom": format_date_param(completed_date_from),
            "completedDateTo": format_date_param(completed_date_to),
            "statusDateFrom": format_date_param(status_date_from),
            "statusDateTo": format_date_param(status_date_to),
            "updateDateFrom": format_date_param(update_date_from),
            "updateDateTo": format_date_param(update_date_to),
            "completedByDepartment": completed_by_department,
            "completedByUser": completed_by_user,
            "closedDateFrom": format_date_param(closed_date_from),
            "closedDateTo": format_date_param(closed_date_to),
            "closedByDepartment": closed_by_department,
            "closedByUser": closed_by_user,
            "recordClass": record_class,
            "types": types,
            "modules": modules,
            "statusTypes": status_types,
        }

        for key, value in filter_params.items():
            if value is not None:
                params[key] = value

        if expand:
            params["expand"] = ",".join(expand)
        if expand_custom_forms:
            params["expandCustomForms"] = expand_custom_forms
        if fields:
            params["fields"] = ",".join(fields)

        return self._list_resource(url, Record, params)
