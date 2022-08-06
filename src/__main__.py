from src.preprocess.TransformerPipeLine import TransformerPipeLine
import pandas as pd


def main():
    data = pd.read_csv("C:/Users\h.karimi\Documents\pprojects\housing_hw\data\external/train.csv")
    transform_pipe_line = TransformerPipeLine()
    x_train, x_test, y_train, y_test = transform_pipe_line.fit_transform(data)
    x_train.to_csv(
        r"C:\Users\h.karimi\Documents\pprojects\housing_hw\data\interim\preprocessed_data_x_train.csv",
        index=False, header=True)
    y_train.to_csv(
        r"C:\Users\h.karimi\Documents\pprojects\housing_hw\data\interim\preprocessed_data_y_train.csv",
        index=False, header=True)
    x_test.to_csv(
        r"C:\Users\h.karimi\Documents\pprojects\housing_hw\data\interim\preprocessed_data_x_test.csv",
        index=False, header=True)
    y_test.to_csv(
        r"C:\Users\h.karimi\Documents\pprojects\housing_hw\data\interim\preprocessed_data_y_test.csv",
        index=False, header=True)


if __name__ == "__main__":
    main()
