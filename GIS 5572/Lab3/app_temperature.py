import psycopg2
from flask import Flask, jsonify
from psycopg2 import sql
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

@app.route('/temperature', methods=['GET'])
def get_points():
    conn = psycopg2.connect(host='35.193.80.209',
                            database='Lab3',
                            user='postgres',
                            password='zyx11457')

    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(sql.SQL("SELECT grid_code, ST_AsGeoJSON(geom)::json AS geometry FROM temperature_BayesianKriging"))
    result = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
