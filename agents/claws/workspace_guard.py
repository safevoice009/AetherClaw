import os

WORKSPACE_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

MAX_FILE_SIZE = 200_000  # 200 KB safety limit


def ensure_workspace_path(path):

    abs_path = os.path.abspath(path)

    if not abs_path.startswith(WORKSPACE_ROOT):
        raise PermissionError("Access outside AI_WORKSPACE is not allowed")

    return abs_path


def check_file_size(code):

    size = len(code.encode("utf-8"))

    if size > MAX_FILE_SIZE:
        raise ValueError(
            f"Generated code too large ({size} bytes). Limit: {MAX_FILE_SIZE}"
        )