# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .beta_cache_control_ephemeral_param import BetaCacheControlEphemeralParam
from .beta_web_search_tool_result_block_param_content_param import BetaWebSearchToolResultBlockParamContentParam

__all__ = ["BetaWebSearchToolResultBlockParam"]


class BetaWebSearchToolResultBlockParam(TypedDict, total=False):
    content: Required[BetaWebSearchToolResultBlockParamContentParam]

    tool_use_id: Required[str]

    type: Required[Literal["web_search_tool_result"]]

    cache_control: Optional[BetaCacheControlEphemeralParam]
    """Create a cache control breakpoint at this content block."""
