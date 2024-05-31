import lzma
import os
import json
import tarfile
import shutil

def decompress_file(input_file_path, output_directory, is_xz=True):
    """ 解压单个文件到输出目录 """
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)  # 创建输出目录如果它不存在

    output_file_path = os.path.join(output_directory, os.path.basename(input_file_path).split('.')[0])
    if is_xz:
        with lzma.open(input_file_path) as compressed_file, open(output_file_path, 'wb') as output_file:
            output_file.write(compressed_file.read())
    else:
        try:
            with tarfile.open(input_file_path) as tar:
                tar.extractall(path=output_directory)
        except tarfile.TarError:
            pass  # 忽略非 tar 文件

def process_directory(directory, output_file):
    """ 处理指定目录下的所有文件，并将结果写入输出文件。 """
    with open(output_file, 'w', encoding='utf-8') as out:
        for filename in os.listdir(directory):
            if filename.endswith('.txt'):  # 假设所有文本文件以 .txt 结尾
                file_path = os.path.join(directory, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    json_str = json.dumps({"text": file.read()})
                    out.write(json_str + '\n')

def main():
    input_directory = '/home/zhaowc/Datasets/openwebtext_small'  # 提供 openwebtext_small 的路径
    decompressed_directory = os.path.join(input_directory, 'decompressed')
    decompressed_tar_directory = os.path.join(decompressed_directory, 'tar') # 在 decompressed 目录内创建 decompressed_tar
    output_json_file = os.path.join(input_directory, 'raw_data.json') # 确保输出文件在 openwebtext_small 内

    # 解压 .xz 文件
    for filename in os.listdir(input_directory):
        if filename.endswith('.xz'):
            decompress_file(os.path.join(input_directory, filename), decompressed_directory, is_xz=True)

    # 解压 .tar 文件
    for filename in os.listdir(decompressed_directory):
        if not filename.endswith('.xz'):  # 跳过 .xz 文件
            decompress_file(os.path.join(decompressed_directory, filename), decompressed_tar_directory, is_xz=False)

    # 处理解压后的文件
    process_directory(decompressed_tar_directory, output_json_file)

    # 删除 decompressed 文件夹
    shutil.rmtree(decompressed_directory)

# 运行主函数
main()
