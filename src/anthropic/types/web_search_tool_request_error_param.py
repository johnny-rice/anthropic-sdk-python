# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["WebSearchToolRequestErrorParam"]


class WebSearchToolRequestErrorParam(TypedDict, total=False):
    error_code: Required[
        Literal["invalid_tool_input", "unavailable", "max_uses_exceeded", "too_many_requests", "query_too_long"]
    ]

    type: Required[Literal["web_search_tool_result_error"]]
