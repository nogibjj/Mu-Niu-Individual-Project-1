from lib import read_data
from script import calc_mean, calc_median, calc_sd, draw


def test_df_exists():
    file = "student_performance.csv"
    df = read_data(file)
    assert df is not None


def test_calc_mean():
    file = "student_performance.csv"
    dataframe = read_data(file)
    for colname in dataframe.select_dtypes(include=["number"]).columns:
        assert calc_mean(file, colname) == dataframe[colname].mean()
    for colname in dataframe.select_dtypes(include=["object"]).columns:
        assert calc_mean(file, colname) == "Mean not available for string"


def test_calc_median():
    file = "student_performance.csv"
    dataframe = read_data(file)
    for colname in dataframe.select_dtypes(include=["number"]).columns:
        assert calc_median(file, colname) == dataframe[colname].median()
    for colname in dataframe.select_dtypes(include=["object"]).columns:
        assert calc_median(file, colname) == "Median not available for string"


def test_calc_sd():
    file = "student_performance.csv"
    dataframe = read_data(file)
    for colname in dataframe.select_dtypes(include=["number"]).columns:
        assert calc_sd(file, colname) == dataframe[colname].std()
    for colname in dataframe.select_dtypes(include=["object"]).columns:
        assert calc_sd(file, colname) == "Standard Deviation not available for string"


def test_draw():
    file = "student_performance.csv"
    dataframe = read_data(file)
    for colname in dataframe.select_dtypes(include=["object"]).columns:
        assert draw(file, colname) == "Plot not available for string"


if __name__ == "__main__":
    test_calc_mean()
    test_calc_median()
    test_calc_sd()
    test_df_exists()
    test_draw()
