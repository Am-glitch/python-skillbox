import os
from typing import Generator

def error_log_generator(file_path: str) -> Generator[str, None, None]:
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if 'ERROR' in line:
                yield line

def filter_errors(input_file: str, output_file: str) -> None:
    with open(output_file, 'w', encoding='utf-8') as output:
        for error_line in error_log_generator(input_file):
            output.write(error_line)

if __name__ == "__main__":
    input_file_name: str = "test.log"
    output_file_name: str = "errors.log"

    input_file_path: str = os.path.join("tests", input_file_name)
    output_file_path: str = os.path.join("tests", output_file_name)

    filter_errors(input_file_path, output_file_path)