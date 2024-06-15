import os

# 设置目标目录
directory = '.'

# 获取目录中所有文件
for filename in os.listdir(directory):
    # 如果文件以.txt结尾
    if filename.endswith('.md'):
        # 构建新的文件名
        new_filename = filename.replace('.zh', '')
        # 重命名文件
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
