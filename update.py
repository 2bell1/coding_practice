import os
from urllib import parse
from datetime import datetime

HEADER = """#
# 백준, 프로그래머스 문제 풀이 목록
"""

def main():
    content = ""
    content += HEADER

    directories = []
    solveds = []

    for root, dirs, files in os.walk("."):
        dirs.sort()
        if root == '.':
            for dir in ('.git', '.github'):
                try:
                    dirs.remove(dir)
                except ValueError:
                    pass
            continue

        category = os.path.basename(root)

        if category == 'images':
            continue

        directory = os.path.basename(os.path.dirname(root))

        if directory == '.':
            continue

        if directory not in directories:
            if directory in ["백준", "프로그래머스"]:
                content += "## 📚 {}\n".format(directory)
            else:
                content += "### 🚀 {}\n".format(directory)
                content += "| 문제 | 링크 | 날짜 |\n"
                content += "| ----- | ----- | ----- |\n"
            directories.append(directory)

        for file in files:
            if category not in solveds:
                file_path = os.path.join(root, file)
                commit_date = get_commit_date(file_path)  # 각 파일의 커밋 날짜 가져오기
                content += "|{}|[링크]({})|{}|\n".format(category, parse.quote(file_path), commit_date)
                solveds.append(category)

    with open("README.md", "w") as fd:
        fd.write(content)

def get_commit_date(file_path):
    try:
        result = os.popen('git log -1 --format=%cd -- ' + file_path).read()
        commit_date = datetime.strptime(result.strip(), "%a %b %d %H:%M:%S %Y %z")
        return commit_date.strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        return ""

if __name__ == "__main__":
    main()
