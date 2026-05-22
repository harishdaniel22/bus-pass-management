from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_mysqldb import MySQL
from datetime import timedelta

from config import Config
from routes.auth  import auth_bp,  init_auth
from routes.buses import buses_bp, init_buses
from routes.passes import passes_bp, init_passes
from routes.punch import punch_bp,  init_punch
from routes.admin import admin_bp,  init_admin

app = Flask(__name__)
app.config.from_object(Config)

# JWT timedelta fix
app.config['JWT_ACCESS_TOKEN_EXPIRES']  = timedelta(seconds=Config.JWT_ACCESS_TOKEN_EXPIRES)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(seconds=Config.JWT_REFRESH_TOKEN_EXPIRES)

# Extensions
CORS(app, resources={r"/api/*": {"origins": "*"}},
     supports_credentials=True)
jwt  = JWTManager(app)
mysql = MySQL(app)

# Inject mysql into route modules
init_auth(mysql)
init_buses(mysql)
init_passes(mysql)
init_punch(mysql)
init_admin(mysql)

# Register blueprints
app.register_blueprint(auth_bp,   url_prefix='/api/auth')
app.register_blueprint(buses_bp,  url_prefix='/api/buses')
app.register_blueprint(passes_bp, url_prefix='/api/passes')
app.register_blueprint(punch_bp,  url_prefix='/api/punch')
app.register_blueprint(admin_bp,  url_prefix='/api/admin')


@app.route('/api/health')
def health():
    return {'status': 'ok', 'service': 'Bus Punching Management API'}, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=Config.PORT, debug=Config.DEBUG)
