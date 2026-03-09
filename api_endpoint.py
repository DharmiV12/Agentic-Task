from langchain_core.prompts import PromptTemplate
from langchain.agents import create_agent
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(model="moonshotai/kimi-k2-instruct-0905")


def agent_creation(query, weather_tool, add_note, get_notes, add_task, get_tasks, update_task_status):

    try:

        prompt_template = """
        You are a helpful assistant.

        Based on the following query choose the tool from tool list:
        Query: {query}

        - Whenevr need to call the tool, that time only call the tool, otherwise not.
        - If there is multiple tasks and notes in query then one by one add into json.

        Response rules:
            - Give all tools respoonse in proper format and also print tool return statement with llm response
            - And in response, Don't mention "I" or any subject.

        For "update_task_status" tool follow the below conditions:

        Identify the id from the query

        - ID should be integer number like 3, 4, etc..
        - If ID is written in words like "Third", "One hundrade and one fifty" then identify that words from the query and covert that into numberuic digits.

        And passed that numeric digit as a query tool for status updation.

        """

        prompt = PromptTemplate(template=prompt_template, input_variables=["query"])

        formated_prompt = prompt.format(query=query)

        tools = [add_note, get_notes, weather_tool, add_task, get_tasks, update_task_status]

        print("Tools are listed\n")

        agent = create_agent(model=llm, tools=tools, system_prompt=formated_prompt)

        print("Tools and prompt passsed to the agent, And agent created...\n")

        response = agent.invoke({"messages": [{"role": "user", "content": query}]})

        print("Agent Invoked\n")

        print("Response: ", response, "\n")

        result = response["messages"][-1].content

        print("Response: ", result, "\n")

        return result
    
    except Exception as e:
        return f"Error: {str(e)}"