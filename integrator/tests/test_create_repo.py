import requests
from git_manager.create_repo_ops import create_repo
from config import auth_header

fake_response = {
        'name': 'test-repo',
        'html_url': 'somerandomwebsite.com'
}



def test_create_repo_success(mocker):
    mock_response = mocker.Mock()

    mock_response.status_code = 201
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = fake_response

    mock_post = mocker.patch(
        'git_manager.create_repo_ops.requests.post',
        return_value = mock_response
    )

    result = create_repo('test-repo')
    payload = {
        "name": 'test-repo',
        "description": "A new repo created by my Python script",
        "private": True
    }
    assert result == fake_response

    mock_post.assert_called_once_with(
        'https://api.github.com/user/repos',
        json=payload,
        headers=auth_header
    )

def test_create_repo_failure(mocker):
    mock_response = mocker.Mock()

    mock_response.status_code = 422
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
        "The server understood your request (the JSON was valid), but the data inside it failed validation."
    )
    
    mock_post = mocker.patch(
        'git_manager.create_repo_ops.requests.post',
        return_value = mock_response
    )

    result = create_repo('nigga')
    expected_payload = {
        "name": 'nigga',
        "description": "A new repo created by my Python script",
        "private": True
    }
    assert result is None

    mock_post.assert_called_once_with(
        'https://api.github.com/user/repos',
        json=expected_payload,
        headers=auth_header
    )




