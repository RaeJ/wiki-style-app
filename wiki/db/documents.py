from sqlalchemy.orm import Session

from components.form_data import DocumentFormData
from db.models import Document


def get_document_by_id(db: Session, id: int) -> Document:
    return db.query(Document).get(id)


def get_documents_by_title(db: Session, title: str) -> list[Document]:
    return db.query(Document).filter(Document.title.ilike(f"%{title}%")).all()


def get_documents(db: Session) -> list[Document]:
    return db.query(Document).all()


def delete_document(db: Session, id: int):
    db.query(Document).filter(Document.id == id).delete()
    db.commit()


def create_document(db: Session, form: DocumentFormData) -> Document:
    document = Document(title=form.title, content=form.content)
    db.add(document)
    db.commit()
    db.refresh(document)
    return document


def update_document(db: Session, id: int, form: DocumentFormData) -> Document:
    existing_document = db.query(Document).get(id)
    existing_document.title = form.title
    existing_document.content = form.content
    db.commit()
    return existing_document
