import matplotlib.pyplot as plt
import numpy as np

# 数据
# NCCL setup times in seconds (First set)
nccl_times = [0.5424, 1.6356, 1.7185, 2.0278]

# Parallel times in seconds (Second set)
parallel_times = [0.0191, 0.0462, 0.0713, 0.0999]

# 配置（设备数量）
configs = ['1 machine 2 GPUs', '2 machines 4 GPUs', '3 machines 6 GPUs', '4 machines 8 GPUs']

# 创建图形，大小为 10x6
plt.figure(figsize=(10, 6))

# 绘制NCCL时间
plt.plot(configs, nccl_times, marker='o', color='tab:red', label='NCCL Setup Time (s)', linestyle='-', linewidth=2)

# 绘制并行时间
plt.plot(configs, parallel_times, marker='s', color='tab:blue', label='Parallel Time (s)', linestyle='--', linewidth=2)

# 设置X轴标签
plt.xlabel('Hardware Configuration')

# 设置Y轴标签
plt.ylabel('Time (seconds)')

# 设置标题
plt.title('NCCL Setup Time vs Parallel Time')

# 显示网格
plt.grid(True)

# 设置X轴标签的角度，使其更易读
plt.xticks(rotation=45)

# 添加图例
plt.legend()

# 自动调整布局，使图形更紧凑
plt.tight_layout()

# 保存为图片
plt.savefig("nccl_parallel_time_comparison.png")

# 显示图形
plt.show()
