from pydantic import BaseModel, Field
from annotated_types import Len
from typing import List, Annotated


class ErrorList(BaseModel):
    """This class represents a list of errors. Each error is represented as a triplet of the original error,
    its correction, and its error-type."""

    # List with exactly three string fields
    error_list: List[Annotated[list[str], Len(min_length=3, max_length=3)]] = Field(
        ...,
        example=[
            ["has", "have", "Subject-Verb Agreement"],
            ["god", "good", "Misspelling"],
        ],
        description="List of error corrections with the original text, corrected text, and a error-type.",
    )
