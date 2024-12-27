import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_excel('D:\\OneDrive\\Desktop\\豆瓣电影top250数据.xlsx', sheet_name='豆瓣电影top250数据')

# 数据预处理
# 将评价人数转换为数值类型
df['评价人数'] = df['评价人数'].str.replace('人评价', '').astype(int)

# 绘制条形图：电影评分分布
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号
plt.figure(figsize=(12, 6))  # 创建一个大小为12x6的图形窗口
plt.bar(df['标题'][:10], df['评分'][:10], color='skyblue')  # 这里只展示前10部电影以避免图表过于拥挤，使用skyblue颜色填充条形
plt.xlabel('电影标题')  # 设置x轴标签为电影标题
plt.ylabel('评分')  # 设置y轴标签为评分
plt.title('电影评分分布（条形图）')  # 设置图形标题为电影评分分布（条形图）
plt.xticks(rotation=45, ha='right')  # 旋转x轴标签以避免重叠
plt.tight_layout()
# 保存图像
plt.savefig('电影评分分布_条形图.png')

# 绘制折线图：电影评价人数随序号的变化趋势
plt.figure(figsize=(12, 6))
plt.plot(df['序号'], df['评价人数'], marker='o', linestyle='-', color='olive')
plt.xlabel('序号')
plt.ylabel('评价人数')
plt.title('电影评价人数随序号的变化趋势（折线图）')
plt.grid(True)
plt.savefig('电影评价人数随序号的变化趋势_折线图.png')

# 绘制散点图：电影评分和评价人数之间的关系
plt.figure(figsize=(12, 6))
plt.scatter(df['评分'], df['评价人数'], color='coral', alpha=0.6)
plt.xlabel('评分')
plt.ylabel('评价人数')
plt.title('电影评分和评价人数之间的关系（散点图）')
plt.grid(True)
plt.savefig('电影评分和评价人数之间的关系_散点图.png')

# 绘制饼图：电影评分分布
plt.figure(figsize=(8, 8))
plt.pie(df['评分'].value_counts(), labels=df['评分'].value_counts().index, autopct='%1.1f%%', startangle=140)
plt.title('电影评分分布（饼图）')
plt.axis('equal')  # 确保饼图是圆形的
plt.savefig('电影评分分布_饼图.png')