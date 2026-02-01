import requests
from git_manager.list_repos_ops import list_repos
from config import auth_header

def test_list_repos_success(mocker):
    fake_response = (
        [
            {'name': 'aws-cloud-club1'},
            {'name': 'aws-cloud-club2'},
        ]
    )

    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = fake_response
    mock_response.raise_for_status.return_value = None

    mock_get = mocker.patch (
        'git_manager.list_repos_ops.requests.get',
        return_value = mock_response
    )

    repos = list_repos('gauciv')

    assert repos == fake_response
    mock_get.assert_called_once_with(
        'https://api.github.com/users/gauciv/repos',
        headers=auth_header,
        timeout=5
    )

def test_list_repos_failure(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 NOT FOUND")

    mock_get = mocker.patch (
        'git_manager.list_repos_ops.requests.get',
        return_value = mock_response
    )

    result = list_repos('nigga')
    assert result is None

    mock_get.assert_called_once_with(
        'https://api.github.com/users/nigga/repos',
        headers=auth_header,
        timeout=5
    )




