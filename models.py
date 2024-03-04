from pydantic import BaseModel, Field


class Task(BaseModel):
    id: int
    title: str = Field(max_length=32)
    description: str = Field(max_length=1024)
    done: bool = Field(default=False)


class TaskIn(BaseModel):
    title: str = Field(max_length=32)
    description: str = Field(max_length=1024)
    done: bool = Field(default=False)
