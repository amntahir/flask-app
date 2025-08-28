from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.get("/")
    def home():
        return {"status": "ok", "message": "Hello CI!"}, 200

    @app.get("/about")
    def about():
        return render_template("about.html")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
