import sys
from pathlib import Path

from flask import Flask

p = Path(__file__).absolute()
sys.path.insert(0, str(p.parent))

from config import Config

# Import app config
app = Flask(__name__)
app.config.from_object(Config)
