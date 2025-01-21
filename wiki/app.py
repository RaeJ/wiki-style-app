from flask import Flask, redirect, render_template, request, url_for

from components.form_data import DocumentFormData
from db.documents import (
    create_document,
    delete_document,
    get_document_by_id,
    get_documents,
    get_documents_by_title,
    update_document,
)
from db.engine import db_session
from settings import settings

app = Flask(__name__)
app.config["SECRET_KEY"] = settings.secret_key.get_secret_value()


@app.route("/edit", methods=["GET"])
def view_edit_page():
    with db_session() as db:
        id = request.args.get("id")
        if id and (document := get_document_by_id(db, id)):
            return render_template("editor.html", page=document)

    return render_template("editor.html")


@app.route("/edit", methods=["POST"])
def submit_edit_page():
    form = DocumentFormData(title=request.form.get("title"), content=request.form.get("content"))
    with db_session() as db:
        id = request.args.get("id")
        if not id or not get_document_by_id(db, id):
            create_document(db, form)
        else:
            update_document(db, id, form)

        return redirect(url_for("list_docs"))

    return render_template("editor.html")


@app.route("/view/<id>", methods=["GET"])
def view_page(id: int):
    with db_session() as db:
        if document := get_document_by_id(db, id):
            return render_template("view.html", page=document)

    return redirect(url_for("list_docs"))


@app.route("/delete/<id>", methods=["GET"])
def delete(id: int):
    with db_session() as db:
        delete_document(db, id)

    return redirect(url_for("list_docs"))


@app.route("/", methods=["GET"])
def list_docs():
    documents = []
    with db_session() as db:
        documents = get_documents(db)

    return render_template("listing.html", pages=documents)


@app.route("/", methods=["POST"])
def search():
    documents = []
    search_text = request.form.get("search-input")
    with db_session() as db:
        if not search_text:
            documents = get_documents(db)
        else:
            documents = get_documents_by_title(db, search_text)

    return render_template("listing.html", pages=documents)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
