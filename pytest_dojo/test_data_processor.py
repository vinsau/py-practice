import pytest
from data_processor import get_user_by_id, get_admin_emails

@pytest.fixture
def setup_data():
    return [
    {
        'user': 'Wow',
        'id': 11,
        'email': 'john@gmail.com',
        'role': 'admin'
    },
    {
        'user': 'LOL',
        'id': 13,
        'email': 'john3232@gmail.com',
        'role': 'member'
    }
]

def test_get_user_by_id(setup_data):
    assert get_user_by_id(setup_data, 13) == True

def test_get_admin_emails(setup_data):
    assert get_admin_emails(setup_data) == ['john@gmail.com']
