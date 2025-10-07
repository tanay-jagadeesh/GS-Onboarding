from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from backend.api.models.request_model import CommandRequest
from backend.api.models.response_model import CommandListResponse, CommandSingleResponse
from backend.data.data_models import Command
from backend.data.engine import get_db
from datetime import datetime

# Prefix: "/commands"
command_router = APIRouter(tags=["Commands"])


@command_router.get("/", response_model=CommandListResponse)
def get_commands(db: Session = Depends(get_db)):
    """
    Gets all the items

    :return: Returns a list of commands
    """
    query = select(Command)
    items = db.exec(query).all()
    return {"data": items}


@command_router.post("/", response_model=CommandSingleResponse)
def create_command(payload: CommandRequest):
    """
    Creates an item with the given payload in the database and returns this payload after pulling it from the database 

    :param payload: The data used to create an item
    :return: returns a json object with field of "data" under which there is the payload now pulled from the database 
    """
    # TODO:(Member) Implement this endpoint
    
    # New command instance from req payload
    new_command = Command(
        command_type = payload.command_type,
        status = "PENDING",
        created_on = datetime.now(),
        updated_on = datetime.now()
    )

    #Save to database
    db.add(new_command)
    db.commit()
    db.refresh(new_command)

    return {"data": new_command}


@command_router.delete("/{id}", response_model=CommandListResponse)
def delete_command(id: int):
    """
    Deletes the item with the given id if it exists. Otherwise raises a 404 error.

    :param id: The id of the item to delete
    :return: returns the list of commands after deleting the item
    """
    # TODO:(Member) Implement this endpoint

    #Find the command through the "ID" 
    if not command:
        raise HTTPException(status_code = 404, detail = f"Command {id} not found")
    
    #Delete the items with the given id if it exists
    db.delete(command)
    db.commit()
    # Return appropriate values
    return get_db_commands()
    