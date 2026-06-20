from tarea04.config import RAW_DATA_DIR, ROOT_DIR


def test_root_exists():
    assert ROOT_DIR.exists()


def test_raw_data_dir_exists():
    assert RAW_DATA_DIR.exists()
