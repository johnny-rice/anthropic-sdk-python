# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from .beta_web_search_tool_result_block_content import BetaWebSearchToolResultBlockContent

__all__ = ["BetaWebSearchToolResultBlock"]


class BetaWebSearchToolResultBlock(BaseModel):
    content: BetaWebSearchToolResultBlockContent

    tool_use_id: str

    type: Literal["web_search_tool_result"]
