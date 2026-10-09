from src.app import generate_app

if __name__ == "__main__":
    app = generate_app()
    app.run(debug=True)