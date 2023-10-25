import pandas as pd
from pmdarima.arima import auto_arima
import numpy as np


# Read the data
data1 = pd.read_excel('2023test1/B1/Q3时间序列城市对.xlsx', sheet_name=None)

# 创建ExcelWriter对象，用于写入多个sheet
with pd.ExcelWriter('2023test1/B1/Q3时间序列城市对.xlsx') as writer:
    # For each sheet, perform the operations
    for sheet_name, sheet_data in data1.items():
        

        # Extract the 'Date Y/M/D' and 'Express delivery quantity (PCS)' columns
        data = sheet_data[['Date Y/M/D', 'Express delivery quantity (PCS)']]
        data.columns = ['Date', 'Quantity']  # Rename the columns for convenience

        # Fit ARIMA model
        model_autoARIMA = auto_arima(data['Quantity'], start_p=0, start_q=0,
                                 test='adf', max_p=5, max_q=5,
                                 m=1, d=None, seasonal=False,
                                 start_P=0, D=0, trace=True,
                                 error_action='ignore',
                                 suppress_warnings=True,
                                 stepwise=True)

        # 预测未来2个时间点的数据
        prediction = model_autoARIMA.predict(n_periods=2)
        # 根据预测值之和与0.5的关系调整预测值
        prediction = np.where(sum(prediction) > 0.5, 1, 0)

        # 将预测值添加到数据的末尾
        last_date = data['Date'].iloc[-1]
        new_dates = pd.date_range(start=last_date, periods=3)[1:]  # 生成新的日期
        new_data = pd.DataFrame({'Date Y/M/D': new_dates, 'Express delivery quantity (PCS)': prediction})
        new_sheet_data = pd.concat([sheet_data, new_data])

        # 将新的sheet数据写回Excel文件
        new_sheet_data.to_excel(writer, sheet_name=sheet_name, index=False)

        


