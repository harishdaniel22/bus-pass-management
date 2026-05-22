import os

class Config:
    # ── Database ──────────────────────────────────────────────
    MYSQL_HOST     = os.environ.get('MYSQL_HOST', 'localhost')
    MYSQL_PORT     = int(os.environ.get('MYSQL_PORT', 3306))
    MYSQL_USER     = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '')   # ← set your password
    MYSQL_DB       = os.environ.get('MYSQL_DB', 'bus_mgmt')
    MYSQL_CURSORCLASS = 'DictCursor'

    # ── JWT ───────────────────────────────────────────────────
    JWT_SECRET_KEY            = os.environ.get('JWT_SECRET_KEY', 'bus-mgmt-super-secret-2025')
    JWT_ACCESS_TOKEN_EXPIRES  = 3600        # 1 hour
    JWT_REFRESH_TOKEN_EXPIRES = 86400 * 7   # 7 days

    # ── App ───────────────────────────────────────────────────
    DEBUG = os.environ.get('DEBUG', 'True') == 'True'
    PORT  = int(os.environ.get('PORT', 5000))
