## python file apiの例
# pathname = "test.txt"
# file = open(pathname)
# contents = print(file.read())
# file.close()

# file = open(pathname, "w")
# file.write(contents + "\nHello, World!")
# file.close()


# ファイル操作のためのライブラリ
import sys

# cli入力から第一引数、第二引数、第三引数、第四引数を変数に格納
arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]
arg4 = sys.argv[4] if len(sys.argv) > 4 else None

# print(arg1)

# reverse処理
# 実行例: python3 file_manipulator.py reverse test.txt test2.txt
if arg1 == "reverse":
    # arg2のパスにあるファイルを開いて、内容を受け取る
    fileData = open(arg2).read()

    # fileDataの文字列を逆順にして、arg3のパスにあるファイルに書き込む
    fileData = fileData[::-1]
    file = open(arg3, "w")
    file.write(fileData)
    file.close()


# copy処理
# 実行例: python3 file_manipulator.py copy test.txt test2.txt
if arg1 == "copy":
    # arg2のパスにあるファイルを開いて、内容を受け取る
    fileData = open(arg2).read()

    # arg3のパスにあるファイルに書き込む
    file = open(arg3, "w")
    file.write(fileData)
    file.close()

# duplicate処理
# 実行例: python3 file_manipulator.py duplicate test.txt 3
if arg1 == "duplicate":
    # arg2のパスにあるファイルを開いて、内容を受け取る
    fileData = open(arg2).read()

    # arg3で受け取った数値分の回数、fileDataの内容をarg2のパスにあるファイルに書き込む
    arg3 = int(arg3)
    writeContent = ""
    for i in range(arg3):
        writeContent += fileData

    file = open(arg2, "w")
    file.write(writeContent)
    file.close()

# replace-string処理
# 実行例: python3 file_manipulator.py replace-string test.txt "hello" "Goodbye"
if arg1 == "replace-string":
    # arg2のパスにあるファイルを開いて、内容を受け取る
    fileData = open(arg2).read()

    # arg3の文字列をarg4の文字列に置き換える
    fileData = fileData.replace(arg3, arg4)

    # arg2のパスにあるファイルに書き込む
    file = open(arg2, "w")
    file.write(fileData)
    file.close()