import autogen

config_list=(
    {
        "model": "open_ai",
        "base_url": "http://localhost:1234/v1",
        "api_key": "NULL"
    }
)

llm_config={
    'config_list': config_list,
}

assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config
)

user_proxy = autogen.UserProxyAgent(
    name="UserProxy",
    code_execution_config={"use_docker": False},
    max_consecutive_auto_reply=10,
    llm_config=llm_config
)

user_proxy.initiate_chat(
    assistant, 
    message="summarize this article:"
)