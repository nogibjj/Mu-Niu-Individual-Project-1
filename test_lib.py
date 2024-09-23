from lib import read_data


def test_read_data():
    file = "student_performance.csv"
    df = read_data(file)
    assert df is not None


if __name__ == "__main__":
    test_read_data()
