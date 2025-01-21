from pydantic import BaseModel


class DocumentFormData(BaseModel):
    title: str
    content: str
