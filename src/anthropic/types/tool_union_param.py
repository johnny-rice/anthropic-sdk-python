# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .tool_param import ToolParam
from .tool_bash_20250124_param import ToolBash20250124Param
from .cache_control_ephemeral_param import CacheControlEphemeralParam
from .web_search_tool_20250305_param import WebSearchTool20250305Param
from .tool_text_editor_20250124_param import ToolTextEditor20250124Param

__all__ = ["ToolUnionParam", "TextEditor20250429"]


class TextEditor20250429(TypedDict, total=False):
    name: Required[Literal["str_replace_based_edit_tool"]]
    """Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.
    """

    type: Required[Literal["text_editor_20250429"]]

    cache_control: Optional[CacheControlEphemeralParam]
    """Create a cache control breakpoint at this content block."""


ToolUnionParam: TypeAlias = Union[
    ToolParam, ToolBash20250124Param, ToolTextEditor20250124Param, TextEditor20250429, WebSearchTool20250305Param
]
