def 퀵정렬(입력리스트):
    입력리스트의길이 = len(입력리스트)
    if 입력리스트의길이 <= 1:
        return 입력리스트
    기준값 = 입력리스트.pop(입력리스트의길이//2)
    그룹_하나 = []
    그룹_둘 = []
    
    for i in range(입력리스트의길이-1):
        if #내용을 채워주세요:
            그룹_하나.append(입력리스트[i])
        else:
            그룹_둘.append(입력리스트[i])
    return #내용을 채워주세요

주어진리스트 = input().split(' ')
#내용을 채워주세요.

print(퀵정렬(주어진리스트))