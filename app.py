from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.get("/")
    def home():
        return {"status": "ok", "message": "Hello CI!"}, 200

    return app

# For local run: python app.py
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
