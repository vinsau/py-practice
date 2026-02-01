# test_api_client.py
import requests
from api_client import get_user_name

# 'mocker' is provided by the pytest-mock plugin
def test_get_user_name_success(mocker):
    """
    Tests the "happy path" when the API call is successful (HTTP 200).
    """
    # 1. ARRANGE
    # This is the fake data we want requests.get() to return
    fake_json = {"id": 1, "name": "Leanne Graham", "username": "Bret"}
    
    # This is the "stunt double" for the response object
    mock_response = mocker.MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = fake_json
    
    # This is the key: "Patch" the 'requests.get' function.
    # When it's called, make it return our 'mock_response' instead.
    mock_get = mocker.patch('requests.get', return_value=mock_response)
    
    # 2. ACT
    # Call the function we are testing
    name = get_user_name(1)
    
    # 3. ASSERT
    # Check that the function returned what we expected
    assert name == "Leanne Graham"
    
    # (Bonus) Check that our mock was called correctly
    mock_get.assert_called_once_with("https://jsonplaceholder.typicode.com/users/1")

# --- YOUR TASK ---
# Write a second test for the "failure" case.

def test_get_user_name_failure_404(mocker):
    """
    Tests the "sad path" when the API returns a 404 Not Found.
    """
    # 1. ARRANGE
    # Hint: You need a mock_response, but this time it shouldn't be happy.
    # Tell the mock to raise an error when .raise_for_status() is called.
    # Like this:
    mock_response = mocker.MagicMock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")

    # Hint: You still need to patch 'requests.get' to return this mock_response 
    mock_get = mocker.patch('requests.get', return_value=mock_response)
    
    # 2. ACT
    # Call the function
    name = get_user_name(999) # 999 is a user that doesn't exist
    
    # 3. ASSERT
    # Hint: What does your function return on an HTTPError?
    assert "API Error" in name
    
    # (Bonus) Assert that requests.get was called with the right user_id
    mock_get.assert_called_once_with("https://api.example.com/users/999")