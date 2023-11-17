import matplotlib.pyplot as plt  
import matplotlib.dates as mdates  
import datetime
# 创建一个数据列表，包含年份  
years = [2000, 2003, 2005, 2008, 2011, 2014, 2017]  
months = [1, 1, 1, 4, 8, 12, 12]  # 可以指定具体的月份，这里假设都是年初  
  
# 将年份和月份转换为日期格式  
years = mdates.date2num(years)  # 年份转换为matplotlib能识别的日期格式  
months = mdates.date2num(months)  # 月份转换为matplotlib能识别的日期格式  
  
# 创建时间序列对象  
dates = mdates.drange(mdates.date2num(years[0]), mdates.date2num(years[-1]), mdates.date2num(days=1))  
  
# 绘制时间轴  
fig, ax = plt.subplots()  
ax.xaxis_date()  # 设置x轴为日期格式  
ax.plot(dates, [0] * len(dates), linestyle='--', color='gray')  # 绘制时间轴线  
ax.plot(years, months, marker='o', markersize=8, linestyle='-', color='blue')  # 在时间轴上标记点  
ax.set_yticklabels([])  # 隐藏y轴标签，因为我们只关心x轴标签  
plt.title("Time Axis with Years Labels")  # 设置标题  
plt.xlabel("Year")  # 设置x轴标签  
plt.show()  # 显示图像