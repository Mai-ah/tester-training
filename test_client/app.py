#!/usr/bin/env python3
import datetime
import logging

import connexion
from connexion import NoContent

from flask_sqlalchemy import SQLAlchemy


logging.basicConfig(level=logging.INFO)

connexion_app = connexion.App(__name__)

app = connexion_app.app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Pet(db.Model):

    id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(100))
    animal_type = db.Column(db.String(20))
    created = db.Column(db.DateTime())
    updated = db.Column(db.DateTime())

    def update(self, name=None, animal_type=None, tags=None, updated=None):
        if name is not None:
            self.name = name
        if animal_type is not None:
            self.animal_type = animal_type
        if updated is not None:
            self.updated = updated

    def dump(self):
        return dict([(k, v) for k, v in vars(self).items() if not k.startswith('_')])


def get_pets(limit, animal_type=None):
    q = db.session.query(Pet)
    if animal_type:
        q = q.filter(Pet.animal_type == animal_type)
    return [p.dump() for p in q][:limit]


def get_pet(pet_id):
    pet = db.session.query(Pet).filter(Pet.id == pet_id).one_or_none()
    return pet.dump() if pet is not None else ('Not found', 404)


def put_pet(pet_id, pet):
    p = db.session.query(Pet).filter(Pet.id == pet_id).one_or_none()
    pet['id'] = pet_id
    timestamp = datetime.datetime.now()
    if p is not None:
        logging.info('Updating pet %s..', pet_id)
        p.update(pet["name"], pet["animal_type"], updated=timestamp)
    else:
        logging.info('Creating pet %s..', pet_id)
        pet['created'] = timestamp
        pet['updated'] = timestamp
        db.session.add(Pet(**pet))
    db.session.commit()
    return NoContent, (200 if p is not None else 201)


def delete_pet(pet_id):
    pet = db.session.query(Pet).filter(Pet.id == pet_id).one_or_none()
    if pet is not None:
        logging.info('Deleting pet %s..', pet_id)
        db.session.query(Pet).filter(Pet.id == pet_id).delete()
        db.session.commit()
        return NoContent, 204
    else:
        return NoContent, 404


@app.cli.command()
def create_db():
    db.create_all()


@app.cli.command()
def drop_db():
    db.drop_all()


connexion_app.add_api('swagger.yaml')


if __name__ == '__main__':
    db.create_all()
    app.run()
