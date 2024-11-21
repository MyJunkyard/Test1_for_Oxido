import pytest
import codecs
from image_paste import get_input_text, write_output_html, fill_template


def test_if_get_input_text_loads_file():
    raw_text = get_input_text("test_files\content.txt")

    assert raw_text == "This file has content."


def test_if_get_imput_text_handles_empty_file():
    with pytest.raises(ValueError) as exception_info:
        get_input_text("test_files\empty.txt")
        assert True is False

    assert exception_info.value.args[0] == "File test_files\empty.txt has no content."


def test_if_write_output_html_correctly_calls_codecs(mocker):
    html = 'test'
    output_file_name = 'file.txt'
    encoding = 'UTF-16'

    class FileHandleMock:

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, exc_tb):
            return False

        def write(self, content: str):
            pass

    file_handle_mock = FileHandleMock()

    mocker.patch('codecs.open', return_value=file_handle_mock)
    open_spy = mocker.spy(codecs, 'open')
    write_spy = mocker.spy(file_handle_mock, 'write')

    write_output_html(html, output_file_name, encoding)

    open_spy.assert_called_once_with(output_file_name, "w", encoding)
    write_spy.assert_called_once_with(html)


def test_fill_template():
    template = 'before <body></body> after'
    content = 'middle'

    assert fill_template(template, content) == 'before <body>\nmiddle\n</body> after'
