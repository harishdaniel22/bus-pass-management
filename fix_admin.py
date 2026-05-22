import bcrypt
from flask import Flask
from flask_mysqldb import MySQL
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
mysql = MySQL(app)

with app.app_context():
    cur = mysql.connection.cursor()
    # Generate a valid hash
    pw_hash = bcrypt.hashpw(b'Admin@123', bcrypt.gensalt()).decode()
    # Update the admin user
    cur.execute("UPDATE users SET password_hash=%s WHERE email='admin@busmanagement.com'", (pw_hash,))
    mysql.connection.commit()
    cur.close()
    print("Admin password fixed successfully!")
