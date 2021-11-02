"""
Author: NGUYEN TAN VIET
Date: 09/10/2021
Program: projects_01_page_165.py
Problem:
 Sửa đổi chương trình tạo câu của Nghiên cứu điển hình 5.3 để chương trình này nhập từ vựng của mình từ một bộ văn bản
 khi khởi động. Tên tệp là nouns.txt, verbs.txt, article.txt và prepositions.txt. (Gợi ý: Xác định
 một chức năng mới duy nhất, get AdWords. Hàm này sẽ yêu cầu một tên tệp làm đối số. Hàm nên
 mở tệp đầu vào có tên này, xác định danh sách tạm thời, đọc các từ từ tệp và thêm chúng vào
 danh sách. Sau đó, hàm sẽ chuyển đổi danh sách thành một tuple và trả về tuple này. Gọi hàm bằng
 một tên tệp thực tế để khởi tạo từng biến trong số bốn biến cho từ vựng.)

Solution:
        Hiển thị kết quả
        Nhập số câu: 4
        VÁY NÓI KÍNH VỚI CẬU BÉ
        KÍNH LỜI NÓI CHUYỆN VỚI CẬU BÉ
        KÍNH NÓI CÔ GÁI VỚI CẬU ẤY
        VÁY NÓI CẬU BÉ TRONG KÍNH

"""
import random

def getWords(fileName):
    inputFile = open(fileName, 'r')
    words = []
    for line in inputFile:
        words.extend(line.split())
    return tuple(words)

articles = getWords("../TextFolder/articles.txt")

nouns = getWords("../TextFolder/nouns.txt")

verbs = getWords("../TextFolder/verbs.txt")

preposition = getWords("../TextFolder/preposition.txt")

def sentence():
    """Tạo và trả về một câu."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Tạo và trả về một cụm danh từ."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Tạo và trả về một cụm động từ."""
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
    return random.choice(preposition) + " " + nounPhrase()

def main():
    number = int(input("Nhập số câu: "))
    for count in range(number):
        print(sentence())
main()

