import pandas as pandas

series_ex = {"a":[1, 3, 5, 7,9], "b":[10, 11, 12, 13, 14], ,"c":[15, 16, 17, 18, 19]}

series_data = pd.DataFrame(series_ex)

print(series_data)
print("Xuat ra cot dau cua series)
print(series_data.iloc[:, 0])