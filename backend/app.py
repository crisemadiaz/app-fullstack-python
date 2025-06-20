from flask import Flask, render_template
from backend.routes import init_routes

app = Flask(__name__, template_folder="../frontend/templates")
init_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
