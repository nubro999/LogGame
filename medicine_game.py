# 알약의 체력 초기화

# 치질약 알약 항문까지 가아함
# 방어력이 있어야함
# 엔딩 1 : 체력 다떨어져서 죽음
# 엔딩 2 : 방어력이 떨어져서 의미없음
# 엔딩 3 : 체력 방어력이 있어서 살아남음
# 히든엔딩 4 : 코에서 뇌로 넘어가서 정신병 자살

'''
시작

-> 체력 떨어지는 시나리오 - 침샘에서 랜덤으로 침이 와서 체력이 깎임

-> 코/인두 선택 - 코일 경우 사망/ 인두일 경우 다음 단계

-> 방어력 떨어지는 시나리오 - 식도/기도 선택 -> 기도 선택 시 방어력 떨어짐 / 체력도 떨어지고 방어력도 떨어짐

-> 위장 펩신 - 랜덤 문제 3번 기회를 줘서 높/낮 방어력 떨어짐

-> 

'''

'''
변수 medi / health/ defen
'''
#----------------------------------------------------------------------------------------------------------
#import
from time import sleep

import random
#-----------------------------------------------------------------------------------------------------------
#자주쓰는 기능함수
def next():
    ans = input("다음(enter)")
    if ans != None: return True

#-----------------------------------------------------------------------------------------------------------
#엔딩 함수
def end1(): #엔딩 1
    print("체력이 다떨어졌습니다! 알약은 항문까지 가지 못하였습니다...")
    ans = input("ㄹ?:(ㄹ입력)")
    if ans == "ㄹ": start()
    else: quit()


def end2(): #엔딩 2
    print("클리어! 알약은 항문까지 무사히 도착했지만..\n방어력이 다떨어져 약은 효과를 잃었습니다...")
    ans = input("ㄹ?:(ㄹ입력)")
    if ans == "ㄹ": start()
    quit()


def end3(): #엔딩 3
    print("클리어! 무사히 항문까지 도착한 치질약쿤, 오혁은 치질에서 해방되었습니다")
    ans = input("ㄹ?:(ㄹ입력)")
    if ans == "ㄹ": start()
    quit()

def end4(): #히든 엔딩
    print("!!뇌에 알약성분이 침투!!")
    sleep(1)
    print("오혁은 그만 정신병에 걸리고 말았습니다")
    sleep(1)
    print("고통에 못이겨 죽음을 선택하는 오혁.")
    ans = input("ㄹ?:(ㄹ입력)")
    if ans == "ㄹ": start()
    quit()
#-----------------------------------------------------------------------------------------------------------
#전역 변수
trying = 0
health = 100
defence = 100
#-----------------------------------------------------------------------------------------------------------
#시작 함수
def start():
    trying = 0
    global health 
    global defence
    health = 100
    defence = 100
    while trying < 4 :
        ans = "시작"
        question = "오혁의 알약 스토리를 시작합니다."

        print(question)
        user_ans = input("'시작'을 입력해주세요.")

        if user_ans == ans :
            adventure_start()
            break
        
        else :
            print("올바르지 않은 입력입니다.")
            trying = trying+1

        if trying == 3 :
            print("스토리를 들을 준비가 되었을 때 처음부터 다시 실행해주세요!")
            import sys
            sys.exit()


def adventure_start():
    print("당신은 이제 몸속을 여행하는 알약입니다.")
    if start == True:
        print ("으아아아 입에 들어간다아아아아")
    if next(): print("당신은 입에 도착했습니다")
    mouth()



#-----------------------------------------------------------------------------------------------------------
#장기들 함수
def mouth():
    global health
    global defence
    saliva = random.randint(10, 80)
    saliva2 = random.randint(10, 50)
    health = health - saliva
    defence -= defence - saliva2
    print(f"입 안에서 {saliva}만큼의 침이 분비되어, 알약의 체력,방어력이 감소했습니다. \n체력: {health}\n방어력{defence}")
        
    if(health < 0): end1()

    if next(): 
        print("다음 단계로 넘어갑니다")
        choice()
    

def choice():
    global health
    global defence
    ans = input("두가지 선택지가 있습니다 1. 코 2. 인두 어디로 넘어가시겠습니까?(입력): ")
    if ans == '코':
        nose() #함수 구현
        
    elif ans == "인두":
        neck() #함수 구현
    else : 
        print("잘못된 입력입니다. '코'나 '인두'를 입력해주세요") 
        choice()
        return



def nose():
    global health
    global defence

    print("당신은 코로 넘어왔습니다")
    damage = random.randint(20, 50)
    if next(): print(f'콧털로 인해 방어력이{damage}감소하고 콧물로 인해 체력이{damage}감소\n')
    defence = defence - damage
    health = health - damage
    print(f"현재체력: {health}\n현재방어력: {defence}")
    if next():
    
        if(health < 0): 
            end1() 

    print("다시 입으로 넘어갑니다")
    #히든
    if next():
        num = random.randint(1,10)
        if num <= 2 : 
            print("!!오혁의 기침!!")
            if next():print("알약은 뇌로 넘어갑니다")
            end4()
        else: mouth()

        return
        
    


def neck():
    global health
    global defence
    print("당신은 인두로 넘어왔습니다.")
    sleep(1)
    print("넘어가는 중")
    sleep(1)
    print("...")
    sleep(1)

    while(True):
        ans = input("식도와 기도를 만났습니다! 어디로 가시겠습니까?:")
        if ans == "식도": 
            print("식도로 넘어갑니다\n")
            sleep(1)
            print(f"식도에서 방어력 20 감소")
            defence = defence - 20
            if(health < 0): end1()
            break
        
        elif ans == "기도":
            print("기도로 넘어갑니다\n")
            print("기도에서 기침해서 코로 들어갑니다.")
            nose()
            break

        else : 
            print("잘못된 입력입니다. 다시 입력해주세요")
    stomach()

def stomach():
    global health
    global defence

    print("당신은 위에 도착했습니다 (enter)")
    if next(): print("펩신을 만난 당신, 펩신은 당신에게 문제를 냅니다. (enter)")
    print("펩신: 방가 방가 나는 펩신이라고 한다.\n 나는 몇가지의 성분을 녹일 수 있을까? 힌트는 1과 20사이에 있다.")
    coans = 10
    
    def quest():
        global health
        global defence
        trying = 0
        while(trying <= 3):
            ans = (input("답은?:"))
            ansint = int(ans)
            if(ansint):
                if ansint < coans :
                    print("낮다 다시!\n") 
                    defence = defence - 4
                    health = health - 2
                    if(health < 0): end1()

                    print("방어력 -4, 체력 -2\n")
                    print(f"현재체력: {health}\n현재방어력: {defence}")
                    trying += 1
                    

                elif ansint > coans : 
                    print("높다 다시!\n")
                    defence = defence - 4
                    health = health - 2
                    if(health < 0): end1()

                    print("방어력 -4, 체력 -2\n")
                    print(f"현재체력: {health}\n현재방어력: {defence}")
                    trying += 1

                else:
                    print("정답이다")
                    break

            else:
                print("숫자만 입력해라")
                quest()
    quest()


    
    print("답을 잘 맞췄군. 장으로 보내주겠다.")
    print(f"현재체력: {health}\n현재방어력: {defence}")
    if(health < 0): end1()
    intestine()


def intestine():
    global health
    global defence
    nums = [0,1,1,0,1,0,1,1,0,1,1,0,0,1]
    boo = 0
    print("휴 장까지 용케 왔군")
    if next():print("이제는 정말 마지막이야")
    if next():
        print("꼬불꼬불한 대장, 위, 아래 중 잘못된 방향으로 가면 대장에 갇히게 된다. 위 아래를 맞추시오(9번), 틀릴 때 마다 -5")
    if next():
        for i in range(1,6):
            ans = input("위? 아래?:")
            if ans == '위': boo = 1
            elif ans == '아래': boo = 0
            else: 
                print("잘못입력, 체력 - 5, 방어력 -10")
                health -= 5
                defence -= 5
                print(f"현재체력: {health}\n현재방어력: {defence}")

            if nums[i] != boo:
                health -= 5
                defence -= 5
                print(f"틀렸다!\n현재체력: {health}\n현재방어력: {defence}")
            else: print("정답!\n")
    
    if(health < 0): end1()

    if next():print("통과하셨습니다.")

    if defence <=0 : end2()

    else: end3()
#------------------------------------------------------------------------------------------------------------------------


start()









    
    
        

        
    


