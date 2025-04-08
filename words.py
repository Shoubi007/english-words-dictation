import re
def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            words = line.split()
            if words:  # Check if the list is not empty
                valid_words = []
                for word in words:
                    if all(substring not in word for substring in ['pron.', 'prep', 'v.', 'vt.', 'vi.', 'n.', 'adj.', 'adv.'])and not re.search(r'[\u4e00-\u9fff]', word):
                            valid_words.append(word)
                    else:
                        break  # Stop processing further words
                phrase = ' '.join(valid_words)  # Join valid words
                outfile.write(phrase + ',')  # Write to the output file

# 使用示例
input_file = '单词5.txt'
output_file = '单词5_new.txt'

process_file(input_file, output_file)