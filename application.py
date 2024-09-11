from flask import Flask, request, jsonify, render_template
import psycopg2
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(
    dbname="asteroidwatch",
    user="postgres",
    password="anika1234",
    host="localhost",
    port="5432"
)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

"""@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({'success': False, 'message': 'Request must be JSON'}), 400
    
    data = request.get_json()
    email = data['email']
    password = data['password']
    
    session_local = SessionLocal()
    user = session_local.query(User).filter_by(email=email).first()
    
    if user and check_password_hash(user.password_hash, password):
        session['user_id'] = user.id
        session_local.close()
        return jsonify({'success': True, 'message': 'Logged in successfully!'})
    else:
        session_local.close()
        return jsonify({'success': False, 'message': 'Invalid email or password'}), 401"""

@app.route('/search',methods=['GET'])
def search_page():
    return render_template('search.html')

@app.route('/search',methods=['POST'])
def search_asteroids():
    data = request.json
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    diameter_min = data.get('diameter_min')
    diameter_max = data.get('diameter_max')
    hazardous = data.get('hazardous')

    query = """
    SELECT 
        name,
        relative_velocity_kph AS velocity,
        diameter_km AS diameter,
        absolute_magnitude_h AS absolute_magnitude
    FROM 
        near_earth_objects AS neo
    JOIN 
        close_approach_data AS cad ON neo.id = cad.neo_id
    WHERE 
        cad.close_approach_date BETWEEN %s AND %s
    """

    params = [start_date, end_date]

    if diameter_min:
        query += " AND neo.diameter_km >= %s"
        params.append(diameter_min)
    
    if diameter_max:
        query += " AND neo.diameter_km <= %s"
        params.append(diameter_max)
    
    if hazardous:
        query += " AND neo.is_potentially_hazardous = TRUE"

    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute(query, params)
    results = cursor.fetchall()
    cursor.close()

    return jsonify({'results': results})


if __name__ == '__main__':
    app.run(debug=True)
