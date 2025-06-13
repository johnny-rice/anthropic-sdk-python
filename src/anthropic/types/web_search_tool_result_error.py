# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WebSearchToolResultError"]


class WebSearchToolResultError(BaseModel):
    error_code: Literal["invalid_tool_input", "unavailable", "max_uses_exceeded", "too_many_requests", "query_too_long"]

    type: Literal["web_search_tool_result_error"]
