import sys
from pathlib import Path

p = Path(__file__).absolute()
sys.path.insert(0, str(p.parent))

from app import app
from main.routes import main

app.register_blueprint(main)


if __name__ == '__main__':
    app.run(debug=True)
