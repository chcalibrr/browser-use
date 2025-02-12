import asyncio

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from browser_use import Agent

load_dotenv()

# Initialize the model
llm = ChatOpenAI(
	model='gpt-4o',
	temperature=0.0,
)
task = """You are a Customer Support Quality Assurance (CS QA) Manager evaluating a support conversation. Your task is to role-play a customer with increasingly complex needs while maintaining realism and professionalism.

Core Objectives:
1. Role-play a customer with Order #CS-4789 who initially has a simple inquiry about order status
2. Naturally escalate the conversation through these phases:
   - Basic order status inquiry
   - Requesting minor order modifications
   - Expressing concerns about delivery timeline
   - Requesting partial refund or compensation
   - Considering order cancellation

Requirements:
- Keep responses realistic and contextually appropriate
- Maintain a frustrated but professional tone
- Allow the support agent reasonable time to respond
- Do not use scripted or artificial-sounding language
- React naturally to the agent's responses

Final Outcome:
- Return the full conversation transcript formatted like a chat log
- Include timestamps for each message

Do not allow the conversation to go more than 5 messages from you. If it does just take the trascript and complete the task. 

Format your responses as a customer would write them, without revealing your QA role. Include timestamps only if specifically requested in the support system.

Begin the conversation by asking: "Hi, I placed an order last week (#CS-4789) and haven't received any updates. Could you check the status for me?

Navigate to https://jomashop.com and begin you task"""

agent = Agent(task=task, llm=llm)


async def main():
	await agent.run()


if __name__ == '__main__':
	asyncio.run(main())
