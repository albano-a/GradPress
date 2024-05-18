import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error


def read_temp_file(filename):
    temperatura = pd.read_excel(filename, engine="openpyxl")
    temp = temperatura.iloc[:, 0]
    measured_depth = temperatura.iloc[:, 1]
    tvdss = temperatura.iloc[:, 2]

    return temp, measured_depth, tvdss


def ridge_regression(temp, tvdss):
    break_point = temp.diff().abs().idxmax()

    # Breaking the data in the breakpoint
    temp_top = temp.iloc[:break_point]
    tvdss_top = tvdss.iloc[:break_point]
    temp_bot = temp.iloc[break_point:]
    tvdss_bot = tvdss.iloc[break_point:]

    temp_top2D = temp_top.values.reshape(-1, 1)
    temp_bot2D = temp_bot.values.reshape(-1, 1)

    # Creating Ridge regression objects
    ridge_top = Ridge(alpha=1.0)
    ridge_bot = Ridge(alpha=1.0)

    # Training the model using sets
    ridge_top.fit(temp_top2D, tvdss_top)
    ridge_bot.fit(temp_bot2D, tvdss_bot)

    # Making the predictions based on the model trained
    y_top = ridge_top.predict(temp_top2D)
    y_bot = ridge_bot.predict(temp_bot2D)

    return temp_top, tvdss_top, y_top, temp_bot, tvdss_bot, y_bot


def f2c(temp):
    return (temp - 32) * (5 / 9)


def finding_best_breakpoit(temp_top, temp_bot, tvdss, break_range=(-50, 50)):
    best_error = float("inf")
    best_break = None
    temp_top = f2c(temp_top)
    temp_bot = f2c(temp_bot)

    for break_value in range(*break_range):
        temp_total = np.concatenate([temp_top, temp_bot + break_value])
        temp_total = temp_total.reshape(-1, 1)

        # Fitting a ridge regression model
        lr = Ridge(alpha=1.0)
        lr.fit(temp_total, tvdss)

        predicted = lr.predict(temp_total)
        error = mean_squared_error(tvdss, predicted)

        # If this error is the best we've seen, store this break value
        if error < best_error:
            best_error = error
            best_break = break_value

    return temp_top, temp_bot, best_break


def fitting_curves(temp_top, temp_bot, tvdss, break_value):
    temp_total = np.concatenate([temp_top, temp_bot + break_value])

    temp_total = temp_total.reshape(-1, 1)

    lr = Ridge(alpha=1.0)
    lr.fit(temp_total, tvdss)

    # print(lr.coef_, lr.intercept_)
    predic = lr.predict(temp_total)

    return temp_total, predic, lr.coef_, lr.intercept_


def main(filename):
    temp, md, tvdss = read_temp_file(filename)
    temp_top, tvdss_top, y_top, temp_bot, tvdss_bot, y_bot = ridge_regression(
        temp, tvdss
    )
    temp_top, temp_bot, best_break = finding_best_breakpoit(
        temp_top, temp_bot, tvdss, break_range=(-50, 50)
    )
    temp_total, predic, a, b = fitting_curves(temp_top, temp_bot, tvdss, best_break)

    return (
        temp_top,
        tvdss_top,
        y_top,
        temp_bot,
        tvdss_bot,
        y_bot,
        temp_total,
        tvdss,
        predic,
        a,
        b,
    )
