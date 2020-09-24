import sys
#input
T = int(sys.stdin.readline())
Students = sys.stdin.readlines()
#solution
def kukyoungsu(s):
    answer = []
    for student in s:
        entity = {}
        spl = student.split()
        entity['name'] = spl[0]
        entity['kor'] = int(spl[1])
        entity['eng'] = int(spl[2])
        entity['math'] = int(spl[3])
        answer.append(entity)
    return sorted(answer, key=lambda x:(-x['kor'], x['eng'], -x['math'], x['name']))
#output
for i in kukyoungsu(Students):
    print(i['name'], end='\n')