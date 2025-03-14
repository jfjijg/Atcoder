import subprocess

# テストケースのファイル名
test_files = ["TestDoc/input1.txt", "TestDoc/input2.txt", "TestDoc/input3.txt"]

# 各テストケースに対してプログラムを実行
for file in test_files:
    print(f"Testing with {file}")
    subprocess.run(["python3", "a.py"], stdin=open(file, "r"))
    print("---")