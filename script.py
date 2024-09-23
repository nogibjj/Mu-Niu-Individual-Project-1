import matplotlib.pyplot as plt
from lib import read_data
import math


def calc_mean(path, colname):
    df = read_data(path)
    if colname not in df.columns:
        return "Column Does Not Exist"
    elif df[colname].dtype == object:
        return "Mean not available for string"
    else:
        return sum(df[colname]) / len(df[colname])


def calc_median(path, colname):
    df = read_data(path)
    if colname not in df.columns:
        return "Column Does Not Exist"
    elif df[colname].dtype == object:
        return "Median not available for string"
    else:
        sorted_data = sorted(df[colname])
        n = len(sorted_data)
        if n % 2 == 1:
            median_val = sorted_data[n // 2]
        else:
            median_val = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        return median_val


def calc_sd(path, colname):
    df = read_data(path)
    if colname not in df.columns:
        return "Column Does Not Exist"
    elif df[colname].dtype == object:
        return "Standard Deviation not available for string"
    else:
        variance = sum((x - calc_mean(path, colname)) ** 2 for x in df[colname]) / (
            len(df[colname]) - 1
        )
        std = math.sqrt(variance)
        return std


def draw(path, colname):
    df = read_data(path)
    if colname not in df.columns:
        return "Column Does Not Exist"
    elif df[colname].dtype == object:
        return "Plot not available for string"
    else:
        plt.hist(df[colname], bins=5)
        plt.xlabel(f"{colname}")
        plt.ylabel("Frequency")
        plt.title(f"{colname} Distribution")
        plt.show()
