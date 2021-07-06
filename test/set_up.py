import pytest
from pathlib import Path
import os


@pytest.fixture(scope='function')
def test_db():
    Path('testDb.db').touch()
    yield 'testDb.db'
    os.remove('testDb.db')