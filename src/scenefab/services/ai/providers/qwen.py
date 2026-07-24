#!/usr/bin/env python3

"""通义千问 Qwen 提供商。"""

<<<<<<< HEAD
=======
import json
import logging
import time

import httpx

from ..base_llm_provider import LLMRequest, LLMResponse, ProviderError
>>>>>>> ee9c209ea90d432a86973b7316565e83ab68e46f
from ..model_catalog import DEFAULT_MODELS, provider_models
from .openai_compat import OpenAICompatProvider


class QwenProvider(OpenAICompatProvider):
    """通义千问提供商（OpenAI 兼容 API）。"""

    PROVIDER_NAME = "qwen"
    DEFAULT_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
    MODELS = provider_models("qwen")
    DEFAULT_MODEL = DEFAULT_MODELS["qwen"]
<<<<<<< HEAD
=======

    async def generate(self, request: LLMRequest) -> LLMResponse:
        """生成文本（带重试和延迟统计）"""
        model = self._get_model_name(request.model)
        messages = self._build_messages(request)
        body = self._build_request_body(request, model, messages)

        start_time = time.monotonic()

        async def _call():
            return await self._call_api(
                "POST", f"{self.base_url}/chat/completions", json=body
            )

        try:
            data = await self._retry_handler.execute(_call)
            latency_ms = (time.monotonic() - start_time) * 1000
            return self._parse_response(data, model, latency_ms)
        except httpx.HTTPError as e:
            # 网络/HTTP 错误 (连接超时/DNS失败/SSL错误/非 2xx 状态), 显式收口
            raise ProviderError(f"生成失败 (网络错误): {e}") from e
        except (json.JSONDecodeError, KeyError, IndexError, ValueError) as e:
            # 响应解析错误 (上游返回非预期格式), 显式收口
            raise ProviderError(f"生成失败 (响应解析): {e}") from e
>>>>>>> ee9c209ea90d432a86973b7316565e83ab68e46f
