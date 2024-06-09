import pytest
import production_ready

@pytest.fixture
def app():
    # app = create_app()
    return production_ready.app
