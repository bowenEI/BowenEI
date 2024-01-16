import re
import sys


def cover_math(text):
    # pattern = r"(?<=\{\{< math >\}\}\n)(\$\$\n[\s\S]+?\n\$\$\n)(?=\{\{< /math >\}\})"
    pattern = r"(?<!\{\{< math >\}\}\n)(?<!\$\$\n)(\$\$[\s\S]+?\$\$)(?!\n\$\$\n)(?!\{\{< /math >\}\})"
    # 将 text 中所有的 LaTeX 公式用 {{< math >}} 和 {{< /math >}} 包裹起来
    text = re.sub(pattern, r"{{< math >}}\n\1\n{{< /math >}}", text)
    return text


if __name__ == "__main__":
    file_list = sys.argv[1:]
    for file in file_list:
        with open(file, "r", encoding="utf-8") as f:
            text = f.read()
        text = cover_math(text)
        with open(file, "w", encoding="utf-8") as f:
            f.write(text)
