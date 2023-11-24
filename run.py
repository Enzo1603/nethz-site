from app import create_app


application = create_app()


if __name__ == "__main__":
    application.run(host=application.config.get("HOST", "127.0.0.1"))
