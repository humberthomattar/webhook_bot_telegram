import pytest
import os
import sys

top_dir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(top_dir)

@pytest.fixture ()
def create_app():
    from webapp import app
    app.config.testing = True
    app.test_client()
    return app