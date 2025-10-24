from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
import asyncio
from autogen_ext.models.ollama import OllamaChatCompletionClient
from autogen_core.tools import FunctionTool
from autogen_agentchat.messages import TextMessage

model_client = OllamaChatCompletionClient(
    model="llama3.2",
)

user_agent = UserProxyAgent(
    name="User_Agent",
    input_func=input
)

primary_agent = AssistantAgent(
    name="Coder_agent",
    model_client=model_client,
    system_message="You are a helpful AI assistant that keeps answers concise."
)

critic_agent=AssistantAgent(
    name="Critic",
    model_client=model_client,
    system_message="Look over the result, and check for any errors."
)

summary_agent=AssistantAgent(
    name="Summarizer",
    model_client=model_client,
    system_message="Summarize the information from the entire conversation. Keep answers concise."
)

text_termination = TextMentionTermination("APPROVE")
team = RoundRobinGroupChat([primary_agent,critic_agent,user_agent], termination_condition=text_termination)

async def main():
    await Console(team.run_stream(task="Spell 'REGGIN' backwards."))


asyncio.run(main())
