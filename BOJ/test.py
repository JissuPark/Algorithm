# t = tuple([1, 'a', 'b', 'c', 'd', 'e'])
# print(f'1. 첫번째 튜플값 : {t[0]}, 마지막 튜플값 : {t[-1]}')
#
# l = ['Banana', 'Apple', 'Orange']
# l.remove("Apple")
# print(f'2. Apple 삭제 후 : {l}')
#
# tupledata = {'fun-coding1', 'fun-coding2', 'fun-coding3'}
# listdata = list(tupledata)
# print(f'3. 튜플 -> 리스트 : {listdata}')
# tldata = tuple(listdata)
# print(f'\t 리스트 -> 튜플 : {tldata}')
#
# d = {'성인': 100000, '청소년': 70000, '아동': 30000}
# d['소아'] = 0
#
# key = tuple(d.keys())
# print(f'6. 키 항목만 리스트로 저장 : {key}')
#
# set_list = list(set([5, 1, 2, 2, 3, 4, 5, 6, 7, 6, 7, 8, 9, 9, 10, 10]))
# print(f'7. 중복 숫자 제거 후 리스트 출력 : {set_list}')
#
# set1 = { '쥬만치', '정글북', '타이타닉', '월E', 'ET' }
# set2 = { '타이타닉', '아바타', '에일리언', '스타워즈', '쥬만치'}
# interlist = list(set1.intersection(set2))
# print(f'8. 중복 값으로 리스트 생성 : {interlist}')
#
# print(f'9. 리스트를 구분자를 이용해 출력 : {" / ".join(interlist)}')
#
# mySet = set()
# mySet.add(input('첫번째 아이템 값 = '))
# mySet.add(input('두번째 아이템 값 = '))
# mySet.add(input('세번째 아이템 값 = '))
# mySet.add(input('네번째 아이템 값 = '))
# mySet.add(input('다섯번째 아이템 값 = '))
# print(f'10. 값을 입력받아 집합에 삽입 : {mySet}')
#
# print(f'11. 집합을 딕셔너리 구조로 변환 : {dict(enumerate(mySet))}')


# 퀴즈 풀어보시고 15문제에서 7문제 이상 풀어보시면 됩니다.
# 다하신 분은 채팅창에 코드 날려주세요.


# ---------- for 반복문  ----------

# 1. 1~100 사이의 숫자 중 11의 배수이거나 7의 배수로 구성된 리스트를
# 리스트 내포 방식을 이용하여 출력하고 총 갯수도 함께 출력하세요.

#[7, 11, 14, 21, 22, 28, 33, 35, 42, 44, 49, 55, 56, 63, 66, 70, 77, 84, 88, 91, 98, 99]
# 22
print('='*30)
a=[i for i in range(1,101) if i%7==0 or i%11==0]
print(a)
print(len(a))





# 2. 이중 리스트 내포 방식을 이용하여 다음과 같은 리스트를 생성하고 출력하여 보세요
# ['1 - 1', '1 - 2', '1 - 3', '2 - 1', '2 - 2', '2 - 3',
#    '3 - 1', '3 - 2', '3 - 3', '4 - 1', '4 - 2', '4 - 3',
#    '5 - 1', '5 - 2', '5 - 3']
print('='*30)
ll = list()
for x in range(1,6):
    for y in range(1,4):
        #ll.append(str(x)+' - '+str(y))
        ll.append(f'{x} - {y}')
print(ll)



# 3. 다음 2차원 리스트를 생성하고 결과와 같이 for...in 문을 이용하여 출력하여 보세요
employees = [
                ['김수철', '서울', 25, '남', '총무부'],
                ['고길동', '부산', 33, '남', '회계부'],
                ['최미나', '대전', 22, '여', '기획부'],
                ['은지원', '서울', 44, '남', '영업부'],
                ['김영탁', '울산', 36, '남', '영업부'],
                ['마동탁', '대구', 50, '남', '기획부'],
                ['이은미', '창원', 42, '여', '총무부']
              ]
print('='*30)
for row in employees:
    for e in row:
        print(e, end='\t')
    print()
#
#    ----------------------------------------
#      사원명     출신지     나이     성별     부서
#    ----------------------------------------
#      김수철     서울     25     남     총무부
#      고길동     부산     33     남     회계부
#      최미나     대전     22     여     기획부
#      은지원     서울     44     남     영업부
#      김영탁     울산     36     남     영업부
#      마동탁     대구     50     남     기획부
#      이은미     창원     42     여     총무부




# 4. 3번의 리스트에서 남자 사원 목록만 출력하여 보세요.
print('='*30)
for (name, loc, age, sex, dep) in employees:
    if sex == '남':
        print(name, loc, age, sex, dep)



# 5. 3번의 리스트에서 성이 '김'인 사원 목록만 출력하여 보세요.
print('='*30)
for (name, loc, age, sex, dep) in employees:
    if name[0] == '김':
        print(name, loc, age, sex, dep)





# ------------------- 함수 퀴즈

# 퀴즈1 : 별찍기
# 숫자만큼 다음과 같은 형태로 출력하는
# 함수를 정의한 후 호출하여라.
def starPrint(num):
    for i in range(1,num+1):
        print('*'*i)
starPrint(5)
starPrint(3)
'''
starPrint(5)

결과 :
*
**
***
****
*****

starPrint(3)

결과 :
*
**
***
'''



# 퀴즈 2
# 인자값을 받아서 출력하는 구구단 함수를 정의한 후
# 호출하여 출력하여라
def gugu(n):
    for i in range(1,10):
        print(f'{n} x {i} = {n*i}')
gugu(9)
'''
def gugu(n):
    ?

gugu(9)

출력 >>
9 X 1 = 9
9 X 2 = 18
9 X 3 = 27
9 X 4 = 36
9 X 5 = 45
9 X 6 = 54
9 X 7 = 63
9 X 8 = 72
9 X 9 = 81

'''


# 퀴즈 3:
# 리스트를 호출하면 각각의
# 아이템이 다음과 같이 출력되도록 함수를 정의하여라
def printList(args):
    print('\t', '오늘의 메뉴')
    for i, a in enumerate(args):
        print(f'{i+1} : {a}')
printList(['ramen', 'binsu'])
printList(['모밀', '탕수육', '육계장'])
'''
# printList(['라면', '빙수'])

   오늘의 메뉴   
1  :  라면
2  :  빙수

printList(['모밀', '탕수육', '육계장'])
   오늘의 메뉴   
1  :  모밀
2  :  탕수육
3  :  육계장
'''


# 퀴즈 4
# 키와 몸무게를 인자로 입력하여
# 메세지가 출력되도록 함수를 정의하고
# bmi 값에 따라 출력한다.
#
# k = 키(입력값) 단위 cm
# w = 체중(입력값)
#
# bmi = (체중(kg)/키(m)의제곱)*1000
#
# bmi 값에 따라 다음과 출력한다.
#
# 고도 비만 : 35 보다 클 경우
# 중등도 비만  : 30 - 35 미만
# 경도 비만 : 25 - 30 미만
# 과체중 : 23 - 25 미만
# 정상 : 18.5 - 23 미만
# 저체중 : 18.5 미만
def BMI(k, w):
    print(f'키 : {k}')
    print(f'몸무게 : {w}')
    bmi = round((w/(k*0.01)**2),2)
    if bmi > 35: print('고도 비만')
    elif bmi > 30: print('중등도 비만')
    elif 25> bmi > 23: print('과체중')
    elif 23>bmi > 18.5 : print('정상')
    elif bmi < 18.5 : print('저체중')
    print(f'BMI : {bmi}')
BMI(170,68)
'''
# 함수 호출 
Bmi(170, 68)


키 :  170
몸무게 :  68
중등도 비만
BMI : 23.53

'''


# 퀴즈 5
# 아래와 함수를 호출하여 메세지가 출력되도록
# 함수를 정의하여라
# 이때 함수 인자는 3개로 구성하며 마지막 man 만 True 형태로
# 초기값을 지정한다.
def say_myself(name, old, man=True):
    print(f'나의 이름은 {name} 입니다.')
    print(f'나이는 {old}살입니다.')
    if man : print(f'남자입니다.')
    else : print(f'여자입니다.')
say_myself('김철수', 20)
say_myself('백설공주', 15, False)
'''
# 함수 정의 
def say_myself(name, old, man=True):
    ?

# 함수 호출 
say_myself('김철수', 20)
say_myself('백설공주', 15, False)

# 결과값 1
나의 이름은 김철수 입니다.
나이는 20살입니다.
남자입니다.
--------------------------------------------------
# 결과값 2
나의 이름은 백설공주 입니다.
나이는 15살입니다.
여자입니다.

'''



# 퀴즈 6
# 여러가지 값이 리스트에 저장될 수 있게
# 인자가 가변인 함수를 정의하고 호출하여라
def addList(*args):
    print(f'총 갯수 : {len(args)}')
    print(f'데이타형 : {type(args)}')
    for i, a in enumerate(args):
        print(f'{i}번째 => {a}')

# 함수 호출 
addList(1,2,3,4)
addList('가','나','다','라','마')
'''
결과1 >>>
총 갯수 : 3
데이타형 : <class 'list'>
0 번째 => 1
1 번째 => 2
2 번째 => 3

결과2 >>>
총 갯수 : 5
데이타형 : <class 'list'>
0 번째 => 가
1 번째 => 나
2 번째 => 다
3 번째 => 라
4 번째 => 마


'''


# 퀴즈 7
# 첫번째 인자의 값이 'min'이면 다음 인자의 숫자 중
# 최대값을 출력하고
# 첫번째 인자의 값이 'max'이면 다음 인자의 숫자중
# 최소값을 출력하여라
# 이 때 전달하는 숫자의 갯수는 가변으로 한다.
def min_max_number(info, *args):
    if info == 'min':
        print(f'최소값은? {min(args)}')
    elif info == 'max':
        print(f'최대값은? {max(args)}')
    else:
        print('error')

min_max_number('min', 100, 20, 40)
min_max_number('min', 100, 20, 40, 500, 1)
min_max_number('max', 100, 20, 40)
min_max_number('max', 100, 20, 40, 500, 1)
'''
# 결과 
최소값은?  20
최소값은?  1
최대값은?  100
최대값은?  500

'''



# 퀴즈 8
# **kwargs 인자 가변 함수를 이용하여
# 함수 호출시 결과값이 다음과 같이 딕셔너리 형태로
# 출력되도록 하여라
def dictDefine(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f'{key} : {value}')
dictDefine(a='apple', b='banana', n='nano')
dictDefine(b='banana', n='nano', s='soup', d='dress', q='quit')


'''
# 함수 호출 
dictDefine(a='apple', b='banana', n='nano')
dictDefine(b='banana', n='nano', s='soup', d='dress', q='quit')

결과1 >>>

{'a': 'apple', 'b': 'banana', 'n': 'nano'}
a : apple
b : banana
n : nano

결과2 >>>
{'b': 'banana', 'n': 'nano', 's': 'soup', 'd': 'dress', 'q': 'quit'}
b : banana
n : nano
s : soup
d : dress
q : quit

'''



# 퀴즈 9
# 첫글자를 제외한 나머지 글자를 '*'로 표시하는
# 람다함수를 정의하여라. 입력되는 문자열은 3글자로 한다.
f1 = lambda name : print(name[0]+'*'*(len(name)-1))
f1('홍길동')
f1('김이박가')
'''
# 함수 호출 
# f1('홍길동')
# f1('김철수')

결과: >>
홍**
김**
'''

# 퀴즈 10
# 국어,영어,수학 3과목의 합과 평균을 구하는
# 람다 함수를 정의하여라
f2 = lambda x,y,z: print(f'국어:{x}, 영어:{y}, 수학:{z}, 총점:{x+y+z}, 평균:{(x+y+z)/3}')
f2(100,80,90)
'''
# 람다 호출 
# f2(100,80,90)

결과 >>
국어:100, 영어:80, 수학:90 , 총점:270, 평균90.00

'''
# 퀴즈1 : if문과 datetime 모듈 이용
# 현재 시간을 아래와 같이 오전과 오후로 분리해서 출력한다.
# 현재 시간은 오후 5시 ? 분입니다.
import datetime
now = datetime.datetime.now()
if now.hour < 12:
    print(f'현재 시간은 오전 {now.hour}시 {now.minute} 분입니다.')
else:
    print(f'현재 시간은 오후 {now.hour-12}시 {now.minute} 분입니다.')

# 퀴즈2 : if문과 datetime 모듈 이용
# 달을 추출 now.month
# 달에 따라 봄, 여름, 가을 ,겨울 메세지 출력
# 12, 1,2 : 겨울
# 3~5 : 봄
# 6~8 : 여름
# 9~11 : 가을
# 출력은 아래와 같이.
# 12월은 겨울입니다.

# 퀴즈 : 문자열에서 숫자와 숫자가아닌문자의 갯수를 출력하여라
testWord = 'Python1234Java4774'
numcnt, apbcnt = 0, 0
for i in testWord:
    if i.isdigit(): numcnt += 1
    else: apbcnt += 1

print(f'결과\n숫자 갯수 : {numcnt}\n문자 갯수 : {apbcnt}')
'''
결과 >>
숫자 갯수 : ? 
문자 갯수 : ?
'''
# 퀴즈 1
# 입력받은 수식에 관련된 결과계산값을 출력한다.
# eval() 이용
'''
result = input('계산식을 입력하세요?.... ')

3+4*20-100

결과 >>
3+4*20-100 = ?

'''

# 퀴즈 2
# 7개의 입력받은 숫자 값을 리스트로 저장한 후
# 최대값과 최소값을 출력한다.
'''
숫자 1? .... 56
숫자 2? .... 34
숫자 3? .... 100
숫자 4? .... 23
숫자 5? .... 78
숫자 6? .... 90
숫자 7? .... 3
입력 리스트 :  ['56', '34', '100', '23', '78', '90', '3']
최소값 :  100
최대값 :  90
'''

# # 퀴즈3
# aList = [78,90,80,50]
# bList = [8,100,34,60]
# 두개의 리스트 요소중에서 최대값과 최소값을 출력하여라

aList = [78,90,80,50]
bList = [8,100,34,60]
print(f'최소값 : {min(aList+bList)}')
print(f'최대값 : {max(aList+bList)}')
'''
최소값 : 8
최대값 : 100
'''

# 퀴즈 4
# enumerate() 함수를 이용하여 아래 리스트를
# 시작 인덱스가 1이 되게 자료 구조를 생성하고
# 아래 형태로 출력한다.

foodList = ['감자탕', '떡국', '모밀냉면', '연어덮밥', '케이준 샐러드']
for i, a in enumerate(foodList):
    print(f'{i+1}번째 메뉴: {a}' )
'''
1 번째 메뉴: 감자탕
2 번째 메뉴: 떡국
3 번째 메뉴: 모밀냉면
4 번째 메뉴: 연어덮밥
5 번째 메뉴: 케이준 샐러드

'''

# 퀴즈 5
# 아래는 리스트를 딕셔너리 리스트(리스트안의 딕셔너리 구조)로 변경하는 프로그래밍이다.
# 이때 딕셔너리 키는 'user숫자' 형태이다.
# map 함수를 이용한 구조로 변경하여라

# 리스트 => 딕셔너리 리스트로 변경 코드
def quiz5(x,y):
    return {'user'+str(y): x}
valueList = ['양준일', '노사연', '구창모', '조용원', '김정화']
print(list(map(quiz5, valueList, [i for i in range(1,6)])))
'''
def makeDict(valueList):
    result = []
    for i in range(0, len(valueList)):
        temp = {}
        temp['user'+str(i+1)] = valueList[i]
        result.append(temp)
    return result

print(f'\n 결과 >> \n valueList = {valueList}')
print((f' \n 딕셔너리 리스트 구조로 변경 => \n {makeDict(valueList)}'))
'''
'''
 결과 >>
 valueList = ['양준일', '노사연', '구창모', '조용원', '김정화']

 딕셔너리 리스트 구조로 변경 => 
 [{'user1': '양준일'}, {'user2': '노사연'}, {'user3': '구창모'}, {'user4': '조용원'}, {'user5': '김정화'}]
'''

'''
 map함수 이용 결과 >> 
 valuelist = ['양준일', '노사연', '구창모', '조용원', '김정화']
 [{'user1': '양준일'}, {'user2': '노사연'}, {'user3': '구창모'}, {'user4': '조용원'}, {'user5': '김정화'}]
'''

# 퀴즈 6
# 퀴즈5의 딕셔너리 리스트(리스트안의 딕셔너리 구조)로 변경하는 프로그래밍을
# map 함수안에 lambda 함수를 이용한 구조로 변경하여라
print(list(map(lambda x,y: {'user'+str(y): x}, valueList, [i for i in range(1,6)])))
'''
 map함수와 lambda 이용 결과 >> 
 valuelist = ['양준일', '노사연', '구창모', '조용원', '김정화']
 [{'user1': '양준일'}, {'user2': '노사연'}, {'user3': '구창모'}, {'user4': '조용원'}, {'user5': '김정화'}]
'''

#  퀴즈7
# 아래의 2개의 리스트를 튜플 리스트(리스트안에 튜플 구조)로 zip() 함수를 이용하여 변경하여라
mKind = ['발라드', '댄스', '클래식', 'OST']
mTitle = ['거리에서', 'DNA', '소녀의 기도', '썸머']
print(list(zip(mKind,mTitle)))
'''
첫번째 리스트 = ['발라드', '댄스', '클래식', 'OST']
두번째 리스트 = ['거리에서', 'DNA', '소녀의 기도', '썸머']
튜플 리스트로 변경 
 [('발라드', '거리에서'), ('댄스', 'DNA'), ('클래식', '소녀의 기도'), ('OST', '썸머')]
 <class 'list'>

('발라드', '거리에서') <class 'tuple'>
('댄스', 'DNA') <class 'tuple'>
('클래식', '소녀의 기도') <class 'tuple'>
('OST', '썸머') <class 'tuple'>
'''

# 퀴즈 8
# 아래는 퀴즈 7의 결과 튜플 리스트이다. 딕셔너리 구조로 변경하고 출력하여라
d = dict()
for x,y in list(zip(mKind,mTitle)):
    d[x]=y
print(d)
'''
튜플리스트 [('발라드', '거리에서'), ('댄스', 'DNA'), ('클래식', '소녀의 기도'), ('OST', '썸머')]
딕셔너리로 변경 
 {'발라드': '거리에서', '댄스': 'DNA', '클래식': '소녀의 기도', 'OST': '썸머'}

발라드  :  거리에서 <class 'str'>
댄스  :  DNA <class 'str'>
클래식  :  소녀의 기도 <class 'str'>
OST  :  썸머 <class 'str'>
'''

# 퀴즈 9
# 아래는 5~10까지의 곱을 구하는 프로그래밍이다.
# lambda 함수, reduce()를 이용한 구조로 변경하여라
# reduce() 함수 임포트 명령어는?
import functools as f


print('-'*20)
numList = list(range(5,11))
print(f'\n\nnumList = {numList}')
'''
def fact_f1(numList):
    result=1
    txtList = []
    for i in numList:
        result *= i
        txtList.append(str(i))
    return txtList, result

print(f'\n \n numList = {numList}')
print(f' 5~10까지의 곱 >> \n {" * ".join(fact_f1(numList)[0])} = {fact_f1(numList)[1]}\n\n')
'''

'''
 numList = [5, 6, 7, 8, 9, 10]
 5~10까지의 곱 >> 
 5 * 6 * 7 * 8 * 9 * 10 = 151200
'''
print(f.reduce(lambda x,y:x*y,numList))
'''
lambda 함수, reduce() 이용 >> 5~10까지의 곱 >> 
 numList = [5, 6, 7, 8, 9, 10]
5 X 6 X 7 X 8 X 9 X 10  =  151200
'''

# 퀴즈 10
# 아래는 문자열 변수를 정의하고 숫자와 글자를 제외한 나머지 글자를 리스트로 변경하는 프로그래밍이다.
# filter() 함수를 이용한 구조로 변경하여라

# 숫자와 글자를 제외한 나머지 글자의 리스트화 
myString = 'a4+5b6&word*bn%~564^3'
def filterList(txt):
    result = []
    for i in range(0,len(txt)):
       if not (txt[i].isdigit() or txt[i].isalpha()) :
           result.append(txt[i])
    return result



print('-'*20)
print(f'\n\n myString = {myString}')
print(f' 숫자와 글자 제외 결과 리스트 = {filterList(myString)}')
print(f' 총 갯수 = {len(filterList(myString))}')

'''
myString = a4+5b6&word*bn%~564^3
 숫자와 글자 제외 결과 리스트 = ['+', '&', '*', '%', '~', '^']
 총 갯수 = 6
'''

'''
 filter() 함수 활용 >> 
 myString = a4+5b6&word*bn%~564^3
 숫자와 글자 제외 결과 리스트 =  ['+', '&', '*', '%', '~', '^']
 총 갯수 = 6
'''
print('-'*20)
print(f'filter()와 lambda 함수 활용 >> ')
print(f' 숫자와 글자 제외 결과 리스트 = {filterList(myString)}')
print(f' 총 갯수 = {len(filterList(myString))}')
print(list(filter(lambda x: not x.isdigit() and not x.isalpha(), myString)))
'''
 filter()와 lambda 함수 활용 >> 
 myString = a4+5b6&word*bn%~564^3
 숫자와 글자 제외 결과 리스트 =  ['+', '&', '*', '%', '~', '^']
 총 갯수 = 6
'''
