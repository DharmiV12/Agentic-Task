from fastapi import FastAPI, HTTPException
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_core.prompts import PromptTemplate
from langchain.agents import create_agent
import os
import json
import uvicorn
from utils import *
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

notes_file_path = "D:/DHARMI/Final Test/notes.json"
task_fle_path = "D:/DHARMI/Final Test/task.json"

API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")


@tool
def add_task(query:str):
    """When task in query use this tool to add the task in json file
    """

    try:
        print("Add Task tool is callled...\n")

        print(f"Query is: {query}")

        result = task_add(query)

        return "Tasks added successfully"

    except Exception as e:
        return f"Facing error in add task, Error: {str(e)}"


@tool
def get_tasks(query: str):
    """To get list of all tasks"""

    try:

        print("Get tasks tool called...")

        print(f"Query is: ", query)

        data = task_get(query)

        return data

    except Exception as e:
       return f"Facing error to get task list, Error: {str(e)}"
    

def get_id(query: str):

    try:
        with open(task_fle_path, 'r') as f:
            data = json.load(f)

        prompt_template = """
        You are a id identifier of task.

        Identify the id from below query:
        Query: {query}

        - ID should be numeric number like 3, 4, etc..

        Return id in below format:
        ID: id-no

        - ID is numeric number like 3, 4, etc..

        In response only return Id from query.

        """

        prompt = PromptTemplate(template=prompt_template, input_variables=["query", "data"])

        formated_prompt = prompt.format(query=query)

        response = llm.invoke(formated_prompt)

        print(f"Response is; {response["messages"][-1].content}")

        return response
    
    except Exception as e:
        return f"Facing error in add task, Error: {str(e)}"


@tool
def update_task_status(query: str):
    """Update the status of provided task"""

    try:

        print("Update task tool is called...\n")

        with open(task_fle_path, 'r') as f:
            data = json.load(f)

        id = get_id(query)

        return id

    except Exception as e:
        return f"Facing error in updation of task, Error: {str(e)}"


@tool
def add_note(query: str):
    """When notes are in query use this tool to add the noted in json file.
    Notes example is: "Meeting at 5 PM"
    """

    try:

        print("Save Note tool called...\n")

        result = note_add(query)

        print(f"Result: {result}")

        return "Notes added successfully"

    except Exception as e:
        return f"Facing error in add note, Error: {str(e)}"
    

@tool
def get_notes(query: str):
    """To get list of all notes"""

    try:

        print("Get notes tool called...")

        data = note_get(query)

        return data

    except Exception as e:
        return f"Facing error to get list of notes, Error: {str(e)}"
    
@tool
def weather_tool(city_name:str):
    """To get weather of location"""
    
    try:
        print("Weather tool is called...")

        data = weather_get(city_name)

        return data
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Response error: {e}")


@app.post("/llm_response/")
def llm_response(query: str):

    try:

        if not query:
            print(f"Enter a question")
            raise ValueError("Query is not founded")
        
        print("Query is given")
        
        prompt_template = """
        You are a tool identifier.

        Based on the following query choose one tool from tool list:
        Query: {query}

        Decide the tool based on their work, that is define below:

        1) add_note: 
            Called when: User told notes like an example "Meeting at 5 PM" or "Add note : Reminder this" 
        
        2) get_notes:
            Called when: User told show the list of notes 

        3) weather_tool:
            Called when: User ask whether for specific city

        4) add_task:
            Called when: User told task to add like an example "Buy Groceries"

        5) get_tasks:
            Called when: User told show the list of tasks

        In get_notes and get_tasks need response in proper "json" format.

        In agent, response give proper answer to the user and also print tool return message.

        """

        prompt = PromptTemplate(template=prompt_template, input_variables=["query"])

        formated_prompt = prompt.format(query=query)

        tools = [add_note, get_notes, weather_tool, add_task, get_tasks]

        print("Tools are listed")

        agent = create_agent(model=llm, tools=tools, system_prompt=formated_prompt)

        print("Tools and prompt passsed to the agent, And agent created...")

        response = agent.invoke({"messages": [{"role": "user", "content": query}]})

        print("Agent Invoked")

        print("Response: ", response)

        print("Response: ", response["messages"][-1].content)

        return response["messages"][-1].content

    except Exception as e:
        return f"Facing error in agent creation or tool calling, Error: {str(e)}"


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8002, reload=True)