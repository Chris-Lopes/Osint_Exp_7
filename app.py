from flask import Flask, jsonify, send_from_directory
import sqlite3
import os

app = Flask(__name__)

# Database path
DB_PATH = os.path.join(os.path.dirname(__file__), 'data', 'osint.db')

def get_db_connection():
    """Create a database connection."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Return rows as dictionaries
    return conn

@app.route('/')
def index():
    """Serve the main dashboard page."""
    return send_from_directory('pages', 'index.html')

@app.route('/api/data')
def get_data():
    """API endpoint to fetch all OSINT data."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Fetch all records from osint_data table
        cursor.execute('SELECT * FROM osint_data ORDER BY timestamp DESC')
        rows = cursor.fetchall()
        
        # Convert rows to list of dictionaries
        data = []
        for row in rows:
            data.append({
                'platform': row['platform'],
                'user': row['user'],
                'text': row['text'],
                'timestamp': row['timestamp'],
                'url': row['url']
            })
        
        conn.close()
        return jsonify(data)
    
    except Exception as e:
        print(f"Error fetching data: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/stats')
def get_stats():
    """API endpoint to get statistics."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Total records
        cursor.execute('SELECT COUNT(*) as total FROM osint_data')
        total = cursor.fetchone()['total']
        
        # Records per platform
        cursor.execute('SELECT platform, COUNT(*) as count FROM osint_data GROUP BY platform')
        platform_stats = {row['platform']: row['count'] for row in cursor.fetchall()}
        
        conn.close()
        
        return jsonify({
            'total': total,
            'platforms': platform_stats
        })
    
    except Exception as e:
        print(f"Error fetching stats: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Check if database exists
    if not os.path.exists(DB_PATH):
        print(f"Warning: Database not found at {DB_PATH}")
        print("Please run main.py first to collect data.")
    
    print("🚀 Starting OSINT Dashboard Server...")
    print("📊 Dashboard available at: http://localhost:5000")
    print("🔌 API endpoint at: http://localhost:5000/api/data")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
