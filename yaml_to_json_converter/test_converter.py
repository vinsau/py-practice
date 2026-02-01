# In test_main.py
import pytest
from main import main
# --- Test 1: Test the 'main' function for YAML -> JSON ---

def test_main_yaml_to_json(mocker):
    # 1. ARRANGE
    
    # Create a fake 'args' object, just like argparse would have.
    fake_args = mocker.MagicMock()
    fake_args.input_file = "test.yaml"
    fake_args.output_file = "test.json"
    fake_args.reverse = False

    # Mock 'argparse.ArgumentParser' to return our fake args
    mocker.patch(
        'argparse.ArgumentParser.parse_args', 
        return_value=fake_args
    )

    # Mock the 'convert' function so we can see how it was called
    mock_convert = mocker.patch('main.convert', return_value={'status': 'success'})
    
    # Mock sys.exit so the test doesn't stop
    mock_exit = mocker.patch('sys.exit')

    # 2. ACT
    main() # Run the main function

    # 3. ASSERT
    # Check if 'convert' was called correctly
    mock_convert.assert_called_once_with(
        input_file="test.yaml",
        output_file="test.json",
        isReverse=False
    )
    
    # Check that sys.exit was NOT called
    mock_exit.assert_not_called()

# --- Test 2: Test 'main' for a failure ---

def test_main_failure(mocker):
    # 1. ARRANGE
    fake_args = mocker.MagicMock()
    fake_args.input_file = "bad.yaml"
    fake_args.output_file = "bad.json"
    fake_args.reverse = False

    mocker.patch(
        'argparse.ArgumentParser.parse_args', 
        return_value=fake_args
    )

    # This time, make the mock 'convert' return None
    mock_convert = mocker.patch('main.convert', return_value=None)
    mock_exit = mocker.patch('sys.exit')

    # 2. ACT
    main()

    # 3. ASSERT
    # Check that 'convert' was called
    mock_convert.assert_called_once_with(
        input_file="bad.yaml",
        output_file="bad.json",
        isReverse=False
    )
    
    # Check that sys.exit WAS called with the error code 1
    mock_exit.assert_called_once_with(1)