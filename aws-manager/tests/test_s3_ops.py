from aws_manager import s3_ops
from pathlib import Path
import os

def test_upload_to_s3(mocker):
    mock_s3 = mocker.MagicMock()

    mocker.patch('boto3.client', return_value=mock_s3)

    s3_ops.upload_to_s3(file_path='test_file.txt', bucket_name='test-bucket')

    mock_s3.upload_file.assert_called_once_with(
        Path('test_file.txt'),
        'test-bucket',
        'test_file.txt'
    )