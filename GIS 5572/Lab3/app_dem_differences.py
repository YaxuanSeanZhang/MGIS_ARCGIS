import psycopg2
from flask import Flask, jsonify
from psycopg2 import sql
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

@app.route('/dem_difference', methods=['GET'])
def get_difference():
    conn = psycopg2.connect(host='35.193.80.209',
                            database='Lab3',
                            user='postgres',
                            password='zyx11457')

    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(sql.SQL("SELECT error, ST_AsGeoJSON(geom)::json AS geometry FROM dem_BayesianKriging_difference"))
    result = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
