activate_this = "/home/ebfrigon/code/venv/bin/activate.fish"
exec(activate_this, dict(__file__=activate_this))
import sys
sys.path.insert(0, "/home/ebfrigon/code/")
from index import app as application
