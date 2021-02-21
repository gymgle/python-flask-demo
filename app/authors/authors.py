from flask import request, jsonify, make_response
from flask_restful import Resource

from app import db
from app.authors.models import Authors
from app.authors.schema import AuthorsSchema


class AuthorsAPI(Resource):
    # list authors
    def get(self):
        get_authors = Authors.query.all()
        author_schema = AuthorsSchema(many=True)
        authors = author_schema.dump(get_authors)
        return make_response(jsonify({"authors": authors}))

    # create author
    def post(self):
        data = request.get_json()
        author_schema = AuthorsSchema()
        author = author_schema.load(data)
        result = author_schema.dump(author.create())
        return make_response(jsonify({"author": result}), 200)


class AuthorDetailAPI(Resource):
    # get author by id
    def get(self, id):
        get_author = Authors.query.get(id)
        author_schema = AuthorsSchema()
        author = author_schema.dump(get_author)
        return make_response(jsonify({"author": author}))

    # update author by id
    def put(self, id):
        data = request.get_json()
        get_author = Authors.query.get(id)
        if data.get('specialisation'):
            get_author.specialisation = data['specialisation']
        if data.get('name'):
            get_author.name = data['name']

        db.session.add(get_author)
        db.session.commit()
        author_schema = AuthorsSchema(only=['id', 'name', 'specialisation'])
        author = author_schema.dump(get_author)
        return make_response(jsonify({"author": author}))

    # delete author by id
    def delete(self, id):
        get_author = Authors.query.get(id)
        db.session.delete(get_author)
        db.session.commit()
        return make_response("", 204)
