from docx import Document
import pandas
# import openpyxl

def read(all_word,part_word):
    doc = Document('high_school_eng_word.docx')
    for i in range(26):
        part_word.append([])
    first=False
    for paragraph in doc.paragraphs:
        if len(paragraph.text)>2 and first:
            word = paragraph.text.replace('*','')
            num=ord(word[0].lower())-ord('a')
            part = word.split(' ',1)
            if part[1]=="":
                print(part)
            all_word.append(part)
            part_word[num].append(part)
        first = True


def read_mistake(file,mistake_word):
    #file_path="mistake_word.xlsx"
    df=pandas.read_excel(file)
    for index, row in df.iterrows():
        word = row[0]  # 假设单词在第一列
        meaning = row[1]  # 假设意思在第二列
        temp=[]
        temp.append(word)
        temp.append(meaning)
        mistake_word.append(temp)
        # print(f"Word: {word}, Meaning: {meaning}")
    #print( mistake_word)