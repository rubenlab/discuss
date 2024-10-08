import re

def remove_old_numbering(title):
    """
    移除标题中已有的编号，保持标题的文本部分。
    """
    # 正则表达式匹配类似 '1.1.1 ' 这样的编号
    return re.sub(r'^\d+(\.\d+)*\s+', '', title)

def add_numbering_to_markdown(file_path, output_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    numbering = [0] * 6  # 用于存储每个级别的编号，假设最多6个级别的标题
    output_lines = []

    for line in lines:
        header_match = re.match(r'^(#+)\s*(.*)', line)
        if header_match:
            header_level = len(header_match.group(1))  # 标题级别，基于 # 的数量
            header_text = header_match.group(2).strip()  # 标题文本

            # 移除旧的编号
            clean_header_text = remove_old_numbering(header_text)

            # 更新编号
            numbering[header_level - 1] += 1
            for i in range(header_level, len(numbering)):
                numbering[i] = 0

            # 生成新的编号
            section_number = '.'.join(str(num) for num in numbering[:header_level] if num > 0)
            new_header = f"{header_match.group(1)} {section_number} {clean_header_text}"
            output_lines.append(new_header + '\n')
        else:
            output_lines.append(line)

    # 输出到新文件
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(output_lines)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python markdown_numbering.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]  # 从命令行获取输入的 Markdown 文件路径
    output_file = sys.argv[2]  # 从命令行获取输出的 Markdown 文件路径

    add_numbering_to_markdown(input_file, output_file)