import openpyxl
import random
"""
Intervals = {
    0 : [0,3],
    1 : [0,3],
    2 : [0,3],
    3 : [0,3],
    4 : [0,3],
}
"""

SLOTS_IN_DAY = 8
PERIOD = 3
NUM_MEMBERS = 3
NUM_KPS = 4
Intervals = { i: [i*PERIOD,PERIOD*(i+1)] for i in range(SLOTS_IN_DAY)}

print(Intervals)

class Member:

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.preference = None
        self.limitations = None


    def setPreference(self, num):
        self.preference = num

    def setLimitations(self, num):
        self.limitations = num

    def setSlot(self, inn, kp):
        self.slot = inn
        self.slot_kp = kp

    def __lt__(self, other):
        if len(self.preference) == len(other.preference):
            if len(self.limitations) == len(other.limitations):
                return True if random.randint(0,2)==0 else False
            else:
                return len(self.limitations) < len(other.limitations)
        else:
            return len(self.preference) < len(other.preference)

    def __str__(self):
        return f"{self.id}. {self.name} "

def input_members(n):

    mems = []

    for i in range(n):
        print("Input member(name, id)")
        name = input('name')
        id = int(input("id:"))
        memb = Member(name, id)
        print("prefer")
        good_slots = map(int, input().split())
        print("limits")
        bad_slots = map(int, input().split())
        memb.setPreference(good_slots)
        memb.setLimitations(bad_slots)
        mems.append(memb)

    return mems

members = input_members(NUM_MEMBERS)

sorted_members = members.sort()


Slots = {  { (i,j):None for j in range(NUM_KPS) }  for i in range(SLOTS_IN_DAY)}


for m in sorted_members:
    ready = False
    if m.preference:
        for item in m.preference:
            for j in range(NUM_KPS):
                if Slots[(item,j)]:
                    continue
                Slots[(item, j)] = m.id
                ready = True
                break

            if ready: break

    if ready:
        break


    for it in range(SLOTS_IN_DAY):
        if it in m.preference or m.limitations:
            continue
        for j in range(NUM_KPS):
            if Slots[(item,j)]:
                continue
            Slots[(item, j)] = m.id
            ready = True
            break











"""
Пусть мы составляем расписание одного из уроков для определенного класса.

T — множество учителей, уже занятых на этом уроке в других классах, R — множество уже занятых кабинетов. Если некоторый предмет ведут все учителя из множества T1 и проходить он может в любом из кабинетов R1, то требуется определить, может ли этот урок проходить в тот же час, и, если может, то изменить множество занятых учителей T, выделить для проведения этого урока минимальный по номеру свободный кабинет и добавить его во множество занятых кабинетов R.

Если же данный урок нельзя поставить в расписание, потому что хотя бы один из учителей его ведущих уже занят или заняты все кабинеты, где он мог бы проходить, то следует вывести одно число −1.

Входные данные

В первой строке записано целое неотрицательное число — количество элементов множества T. Во второй строке через пробел перечислены эти элементы (натуральные числа). Если количество элементов множества T равно нулю, то вторая строка входных данных пустая.

В третьей строке указано количество элементов множества R. В четвертой строке перечислены через пробел элементы второго множества (натуральные числа). Если количество элементов множества R равно нулю, то четвертая строка входных данных пустая.

Далее в том же формате указаны сначала количество, а потом и сами элементы непустого множества T1. Наконец, в последних двух строках входных данных указаны количество и сами элементы непустого множества R1.

Множества во входных данных могут быть неупорядочены и содержать равные элементы.

Выходные данные

Результат в случае положетельного ответа требуется вывести в том же формате: сначала количество элементов обновленного множества занятых учителей, затем сами элементы в порядке возрастания. В следующих двух строках выведите количество и элементы множества занятых кабинетов в порядке возрастания.

Если урок добавить в расписание невозможно, то выведите одно число −1.
"""
def array_input(n):
    if n:
        return list(map(int, input().split()))
    input()
    return []

t = int(input())
T = array_input(t)
r = int(input())
R = array_input(r)
t1 = int(input())
T1 = array_input(t1)
r1 = int(input())
R1 = array_input(r1)
set_T, set_R, set_T1, set_R1 = set(T), set(R), set(T1), set(R1)
T, R, T1, R1 = list(set_T), list(set_R), list(set_T1), list(set_R1)
if set_R1.issubset(set_R) or set_T.intersection(set_T1):
    print(-1)
else:
    r_min = min(list(set_R1.difference(set_R)))
    R.append(r_min)
    R.sort()
    set_T.update(set_T1)
    T = list(set_T)
    print(len(T))
    print(" ".join(list(map(str, T))))
    print(len(R))
    print(" ".join(list(map(str, R))))



