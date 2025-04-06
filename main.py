# from langchain_openai import AzureChatOpenAI
from browser_use import Agent, Browser, BrowserConfig, Controller
from pydantic import SecretStr
from pydantic import BaseModel
from typing import List
import os
import asyncio
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model="gpt-4o"
)

browser = Browser(
    config=BrowserConfig(
        chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', 
    )
)

initial_actions = [
    {'open_tab': {'url': 'https://in.linkedin.com/'}},
    {'open_tab': {'url': "https://www.linkedin.com/jobs/search/?currentJobId=4186269047&distance=25&f_AL=true&geoId=102713980&keywords=generative%20AI&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"}}
]


# Create agent with the model
async def main():
    agent = Agent(
        task="""
             You are a browser agent. Your task is to log in to LinkedIn and and apply for easy apply jobs with respective to generative AI with 4 years of experience.
             Follow these steps:
                1. Apply for easy apply jobs with respective to generative AI with 4 years of experience.
            """,
        llm=llm,
        initial_actions=initial_actions,
        # sensitive_data=sensitive_data,
        save_conversation_path = "logs/conversation",
        browser=browser,
    )
    result = await agent.run()
    print(result)
    print("FINAL RESULT",result.is_done())

asyncio.run(main())

