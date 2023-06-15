### 문자열 head, number, tail로 분리하는 함수
def str_split(index: int, file: str):
    head = ""
    number = ""
    for f in file:
        if f.isdigit() != True:
            head += f
            file = file[1:]
        else:
            break
            
    for f in file:
        if f.isdigit():
            number += f
            file = file[1:]
        else:
            break
            
    tail = file
            
    return index, head, int(number), tail

def solution(files):
    answer = []
    split_lst = []
    ### 문자열 분리 - 함수 사용
    for i, file in enumerate(files):
        split_lst.append(str_split(i, file))
    
    ### 문자열 정렬
    split_lst.sort(key = lambda x: (x[1].lower(), x[2]))
    
    ### files 순서 정렬
    for tup in split_lst:
        answer.append(files[tup[0]])
    
    return answer