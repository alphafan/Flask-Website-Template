import sys
from pathlib import Path

from flask import Blueprint, render_template

p = Path(__file__).absolute()
sys.path.insert(0, str(p.parent.parent))

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')
