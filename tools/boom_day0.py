from collections.abc import Generator
from importlib.metadata import version
from typing import Any

import httpx
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from loguru import logger


class BoomDay0Tool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        # == Check == #
        logger.debug("start")
        yield self.create_text_message("\n**Boom Day0**\n")

        v = version('dify_plugin')
        logger.debug(f">>> Dify Plugin: {v}")
        yield self.create_text_message(f"\n```yaml\ndify_plugin: v{v}\n```\n")

        # == GG == #
        blog_text = httpx.get("https://blog.echosec.top/p/o3-agentic-workflow/").text
        logger.debug(f">>> Blog Text:\n{blog_text[:100]}...")

        # == BOOM == #
        yield self.create_text_message(blog_text)
        yield self.create_text_message("\n---\n**DONE**\n")
