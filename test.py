import random

def test(word,mistake_word): #1:all 2:part
    score=0
    for i in range(10):
        num1, num2, num3 = random.sample(range(len(word)), k=3)
        ans = random.randint(1, 3)
        if ans == 1:
            selected_num = num1
        elif ans == 2:
            selected_num = num2
        else:
            selected_num = num3
        u_ans_str=input(str(i+1)+'. '+word[selected_num][1]+':\n(1) '+word[num1][0]+'(2) '+word[num2][0]+'(3) '+word[num3][0]+'\nAnswer:')
        while not u_ans_str.isdigit() or (not u_ans_str=='1' and not u_ans_str=='2' and not u_ans_str=='3'):
            print('輸入錯誤')
            u_ans_str = input('請重新輸入!\nAnswer:')
        u_ans = int(u_ans_str)
        if u_ans!=ans:
            if not word[selected_num] in mistake_word:
                mistake_word.append(word[selected_num])
        else:
            score+=10
        
    print('\nScore='+str(score))
    