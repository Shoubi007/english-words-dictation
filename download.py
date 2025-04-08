# 安装 pydub 和 ffmpeg
# pip install pydub
# 下载并安装 ffmpeg: https://ffmpeg.org/download.html

import requests
import os
from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError

# from urllib.request import urlopen
# import requests
# import re
# from pydub import AudioSegment
# from pydub.exceptions import CouldntDecodeError
#
# def download(word):
#     if word == "":
#         return None
#     else:
#         url = "https://dictionary.cambridge.org/pronunciation/english/{}"+ word.replace(" ", "+")
#         try:
#             content = urlopen(url).read()
#             urls = set(re.findall('data-src-mp3="(.*?(uk|us)_pron.*?.mp3)', str(content)))
#             for u, s in urls:
#                 if s == 'us':
#                     file_path = "MP3_4/{}.mp3".format(word.replace(" ", "_"))
#                     f = requests.get(u)
#                     with open(file_path, "wb") as fp:
#                         fp.write(f.content)
#                     return file_path
#         except Exception as e:
#             print(f"Error downloading {word}: {e}")
#             return None
def download(word):
    directory = "MP3_5"

    if word == "":
        return None
    else:
        url = "http://dict.youdao.com/dictvoice?audio=" + word.replace(" ", "+")
        try:
            f = requests.get(url)
            if not os.path.exists(directory):
                os.makedirs(directory)
            file_path = os.path.join(directory, "{}.mp3".format(word.replace(" ", "_")))
            with open(file_path, "wb") as fp:
                fp.write(f.content)
            return file_path
        except Exception as e:
            print(f"Error downloading {word}: {e}")
            return None

# 从 processed_words.txt 文件中读取单词列表
words = []
with open("单词5_new.txt", "r", encoding="utf-8") as fp:
    for line in fp:
        words.extend(line.split(','))

# 下载所有单词的音频文件
audio_files = []
for word in words:
    file_path = download(word)
    if file_path:
        audio_files.append(file_path)

# 合并所有音频文件，并在每个单词之间添加3秒的间隔
combined = AudioSegment.empty() + AudioSegment.silent(duration=1000)
for file_path in audio_files:
    try:
        audio = AudioSegment.from_mp3(file_path)
        silence = AudioSegment.silent(duration=1000)
        combined += audio + silence + audio + AudioSegment.silent(duration=2000) # 添加3秒的间隔
    except CouldntDecodeError:
        print(f"Could not decode {file_path}")

# 导出合并后的音频文件
combined.export("combined_5_new.mp3", format="mp3")