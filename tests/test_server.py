import os
import tempfile
import shutil
import pytest
from datetime import datetime
from server import list_files, FileInfo

def create_test_files(test_dir):
    files = [
        ("file1.txt", 100),
        ("file2.log", 200),
    ]
    for fname, size in files:
        with open(os.path.join(test_dir, fname), "wb") as f:
            f.write(b"0" * size)
    os.mkdir(os.path.join(test_dir, "subdir"))
    return files

def test_list_files_returns_expected_files():
    test_dir = tempfile.mkdtemp()
    try:
        files = create_test_files(test_dir)
        result = list_files(test_dir)
        names = {f.name for f in result}
        for fname, _ in files:
            assert fname in names
        assert "subdir" in names
        for f in result:
            assert isinstance(f, FileInfo)
            assert f.name
            assert isinstance(f.size, int)
            assert isinstance(f.modified, datetime)
            assert f.type in ("file", "directory")
            assert isinstance(f.permissions, str)
    finally:
        shutil.rmtree(test_dir)

def test_list_files_invalid_dir_raises():
    with pytest.raises(Exception):
        list_files("/no/such/dir/exists")
