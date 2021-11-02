"""
Program: page_126_casestydy_01.py
Author: Nguyen Tan Viet
Date: 28/09/2021
     Lời yêu cầu
     Viết chương trình tính Chỉ số Flesch và cấp lớp cho văn bản được lưu trữ trong
     tệp văn bản.
     Phân tích
     Đầu vào của chương trình này là tên của một tệp văn bản. Kết quả đầu ra là số lượng
     các câu, từ và âm tiết trong tệp, cũng như Chỉ mục và Lớp Flesch của tệp
     Mức độ tương đương.
     Trong quá trình phân tích, chúng tôi tham khảo ý kiến ​​của các chuyên gia trong lĩnh vực vấn đề để
     tìm hiểu bất kỳ thông tin nào có thể liên quan đến việc giải quyết vấn đề. Đối với vấn đề của chúng tôi, thông tin này
     bao gồm các định nghĩa của câu, từ và âm tiết. Đối với mục đích của chương trình này, các thuật ngữ này
     được định nghĩa trong Bảng 4-7 Word Any sequence of non-whitespace characters.
     Sentence Any sequence of words ending in a period, question mark, exclamation point,
                              colon, or semicolon.
     Syllable Any word of three characters or less; or any vowel (a, e, i, o, u) or pair of
     consecutive vowels, except for a final -es, -ed, or -e that is not -le

"""
"""
Program: textanalysis.py
Author: Ken
Computes and displays the Flesch Index and the Grade 
Level Equivalent for the readability of a text file.
"""
# Lấy đầu vào

fileName = input("Enter the file name: ")
inputFile = open(fileName, 'r')
text = inputFile.read()

# Đếm số câu

sentences = text.count('.') + text.count('?') + \
 text.count(':') + text.count(';') + \
 text.count('!')

# Đếm các từ

words = len(text.split())

# Đếm âm tiết

syllables = 0
vowels = "aeiouAEIOU"
for word in text.split():
    for vowel in vowels:
        syllables += word.count(vowel)
    for ending in ['es', 'ed', 'e']:
        if word.endswith(ending):
           syllables -= 1
    if word.endswith('le'):
         syllables += 1

# Tính chỉ số da thịt và cấp lớp

index = 206.835 - 1.015 * (words / sentences) - \
        84.6 * (syllables / words)
level = round(0.39 * (words / sentences) + 11.8 * \
              (syllables / words) - 15.59)

# Đưa ra kết quả

print("The Flesch Index is", index)
print("The Grade Level Equivalent is", level)
print(sentences, "sentences")
print(words, "words")
print(syllables, "syllables")
.