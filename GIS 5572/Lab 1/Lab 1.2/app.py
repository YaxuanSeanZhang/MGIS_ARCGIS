import psycopg2
from flask import Flask, jsonify
from psycopg2 import sql
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

@app.route('/get_polygon', methods=['GET'])
def get_polygon():
    conn= psycopg2.connect(host = '35.193.80.209',
                             database = 'lab0',
                             user = 'postgres',
                             password = 'zyx11457')

    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(sql.SQL("SELECT myPolygon, ST_AsGeoJSON(geom)::json AS geometry FROM myPolygon"), (1,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify(result)
