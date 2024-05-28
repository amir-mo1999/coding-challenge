"""In this file the routes of our backend server are defined."""

from fastapi import APIRouter, HTTPException
from .models import TextInput, ErrorList
from .LLM_connections import co
import json
from json.decoder import JSONDecodeError

# define the API router
router = APIRouter()


# Define a little test route
@router.get("/")
async def home():
    return "Backend is running"


@router.post(
    "/correct-text",
    response_model=ErrorList,
    responses={
        404: {
            "description": "Text could not be processed by LLM.",
            "content": {
                "application/json": {
                    "example": {"detail": "Text not processable by LLM"}
                }
            },
        },
    },
)
async def correct_text(input_text: TextInput):
    """Screen a text for errors and provide errors, correction and error types in a list of triplets."""

    # # process input text using model
    # model_output = co.generate(
    #     prompt="""
    #             I want you to provide a list of errors found in a text, their correction and their type of error as a list of JSON compatible triplets. Do not provide the corrected sentence at the end of your response and do not add unnecessary text. Just the list of errors should be given.
    #             Example:
    #             I want to has a god day.
    #             Output:
    #             [["has", "have", "Subject-Verb Agreement"], ["god", "good", "Misspelling"]]

    #             Proceed for the following text: """
    #     + input_text.text
    # )
    try:
        json_output = json.loads("gewgew[]")
    except JSONDecodeError:
        raise HTTPException(status_code=404, detail="Text not processable by LLM")

    return ErrorList(json_output)
