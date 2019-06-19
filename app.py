from coord.model import Coord, coords_schema, coord_schema
from extensions import app
from extensions import session
from bottle import request, response
from bottle import post, get, delete
import json
import bottle
import sys


@get('/coords')
def get_all_coord():
    response.headers['Content-Type'] = 'application/json'
    coords = session.query(Coord).all()
    js = coords_schema.dump(coords).data
    print(type(js))
    print(js)
    return json.dumps(js)


@get('/coord/<coord_id>')
def get_one_coord(coord_id):
    coord = session.query(Coord).filter_by(id=coord_id).first()
    if not coord:
        return json.dumps({'message': 'No coord found!'}, 404)

    response.headers['Content-Type'] = 'application/json'
    print(coord_schema.dump(coord).data)
    return coord_schema.dump(coord).data


@post('/coord')
def create_coord():
    data = request.json

    coord = Coord(id=data['id'], x=data['x'], y=data['y'])
    session.add(coord)
    session.commit()

    response.headers['Content-Type'] = 'application/json'
    print(coord_schema.dump(coord).data)
    return coord_schema.dump(coord).data


@delete('/coord/<coord_id>')
def delete_coord(coord_id):
    response.headers['Content-Type'] = 'application/json'

    coord = session.query(Coord).filter_by(coord_id=coord_id).first()

    if not coord:
        return json.dumps({'message': 'No coord found!'})

    session.delete(coord)
    session.commit()

    return json.dumps({'message': 'The coord has been deleted!'})


def main():
    c = Coord(id="test", x=0, y=0)
    print("c: " + str(coord_schema.dump(c).data))
    session.add(c)
    session.commit()
    coords = session.query(Coord).all()
    print("all: " + str(coords_schema.dump(coords).data))
    if len(sys.argv) > 1 and sys.argv[1] == "exit":
        return
    bottle.run(server='gunicorn', host='127.0.0.1', port=5000)


if __name__ == '__main__':
    main()
