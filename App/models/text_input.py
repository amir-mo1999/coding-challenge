from pydantic import BaseModel, StringConstraints, Field
from typing import Annotated


class TextInput(BaseModel):
    """This list represents a textual input."""

    text: Annotated[
        str,
        StringConstraints(min_length=2, max_length=1000),
        Field(
            example="I want to has a god day today. Yesterday i feel not so great.",
            description="The text to be processed for errors. Min length of 2 characters and a maximum length of 1000 characters.",
        ),
    ]
