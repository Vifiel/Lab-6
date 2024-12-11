from math import ceil

class Machine():
    def __init__(self, productivity, cost, ap_detail, durability):
        self.productivity = productivity
        self.cost = cost
        self.ap_detail = ap_detail
        self.durability = durability

    def __add__(self, other):
        if not isinstance(other, int):
            raise ArithmeticError("Починка восстанавливает целое число лет")
        return Machine(self.productivity, self.cost, self.ap_detail, self.durability+other)

    def recoupment(self):
        return self.cost/self.ap_detail

    def recoup_time(self):
        return self.recoupment()/self.productivity
    
    def time_before_repair(self, time):
        #time - время, которое отработал станок в годах
        return self.durability - time 

class Mill_machine(Machine):
    def __init__(self, productivity, cost, ap_detail, durability, deg_of_free):
        super().__init__(productivity, cost, ap_detail, durability)
        self.deg_of_free = deg_of_free #Степени свободы станка

    def hand_act_count(self, num_surf_miled):
        '''Метод возвращает количество необходимых перемещений детали руками в
        зависимости от степеней свободы станка и количества обрабатываемых поверхностей'''
        return ceil(num_surf_miled/self.deg_of_free)

class Cnc_machine(Machine):
    def __init__(self, productivity, cost, ap_detail, durability, accur):
        super().__init__(productivity, cost, ap_detail, durability)
        self.accur = accur

    def amount_of_flaw(self):
        #Возвращает количество отбракованных деталей в час
        return self.productivity*(1-self.accur)

if __name__ == "__main__":
    m1 = Machine(10, 10000, 200, 10)
    m2 = Mill_machine(20, 20000, 100, 15, 3)
    m3 = Cnc_machine(15, 30000, 500, 20, 0.96)
    print(m1.recoupment())
    print(m2.recoup_time())
    print(m3.recoupment())
    print(m1.time_before_repair(5))
    print(m2.hand_act_count(5))
    print(m3.amount_of_flaw())
    print(m2.time_before_repair(14))
    m1 = m1 + 10
    print(m1.time_before_repair(5))


    
