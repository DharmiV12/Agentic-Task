from fastapi import FastAPI, HTTPException
from langchain_core.tools import tool
import uvicorn
from utils import *
from api_endpoint import agent_creation

app = FastAPI()


@tool
def add_task(query:str):
    """
    When "Add task" in query use this tool to add the task in json file.
    """

    try:
        print("Add Task tool is callled...\n")

        result = task_add(query)

        print(f"Add task tool's result: {result}")

        return result

    except Exception as e:
        return f"Facing error in add task, Error: {str(e)}"


@tool
def get_tasks(query: str):
    """List all the task with id, name and status in proper format."""

    try:

        print("Get tasks tool called...")

        data = task_get(query)

        print(f"Get tasks tool's result: {data}\n")

        return data

    except Exception as e:
       return f"Facing error to get task list, Error: {str(e)}"
    

@tool
def update_task_status(query: str):
    """
    Update the status of task from "Pending" to "Completed".

    Also return that task details like below:
    {id, task name, task status}
    """

    try:

        print("Update task tool is called...\n")

        data = task_status_updation(query)    

        return data

    except Exception as e:
        return f"Facing error in updation of task, Error: {str(e)}"


@tool
def add_note(query: str):
    """
    When "Add note" is in query use this tool to add the note in json file.
    """

    try:

        print("Add Note tool called...\n")

        result = note_add(query)

        print(f"Add note tool result: {result}")

        return result

    except Exception as e:
        return f"Facing error in add note, Error: {str(e)}"
    

@tool
def get_notes(query: str):
    """List all the notes with id and name in proper format."""

    try:

        print("Get notes tool called...")

        data = note_get(query)

        print(f"Get notes tool's result: {data}\n")

        return data

    except Exception as e:
        return f"Facing error to get list of notes, Error: {str(e)}"
    
@tool
def weather_tool(city_name:str):
    """To get weather of location."""
    
    try:
        print("Weather tool is called...")

        data = weather_get(city_name)

        print(f"Weather data get successfully\n")

        return data
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Response error: {e}")


@app.post("/llm_response/")
def llm_response(query: str):

    try:

        if not query:
            print(f"Enter a question")
            raise ValueError("Query is not founded")
        
        print(f"Query is given, Query: {query}")

        response = agent_creation(query, weather_tool, add_note, get_notes, add_task, get_tasks, update_task_status)

        print("Agent gave response successfully")

        result = {"Response":response}

        return result

    except Exception as e:
        return f"Facing error in agent creation or tool calling, Error: {str(e)}"


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8004, reload=True)