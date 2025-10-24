model_client=OpenAIChatCompletionClient(
    model="gpt-oss",
    base_url="http://localhost:11434/v1",
    api_key="nicolovescock",
    model_info={
        "json_output": True,
        "function_calling": True,
        "vision": False,
        "family": "unknown",
        "structured_output": True,
    },
   
)