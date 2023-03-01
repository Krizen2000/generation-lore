from src.genlore.app import app
import sys


if __name__ == "__main__":
    app_instance = app()
    sys.exit(app_instance.exec())