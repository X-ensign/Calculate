
# 计算理论值
class cal:
    def __init__(self, m, r_out, r_in):
        self.m = m
        self.r_out = r_out
        self.r_in = r_in

    # 理论的转动惯量
    def cal_theoreticla_value(self):
        self.I = self.m * (self.r_out ** 2 + self.r_in ** 2)/2
        return self.I
    
    def print(self):
        print("铝环转动惯量的理论值是: ", self.cal_theoreticla_value())
    
# 计算实验值
class cal_MomentOfInertia(cal):
    def __init__(self, m_wight, gravity, r_around, beta_Mforce, beta_Uforce):
        self.m = m_wight
        self.g = gravity
        self.r = r_around
        self.alpha_1 = beta_Mforce
        self.alpha_f = beta_Uforce

    def cal(self):
        I = (self.m * self.g * self.r)/(self.alpha_1 + self.alpha_f)
        return I
    
    def print(self):
        print("铝环转动惯量的实验值是: ", self.cal())
class cal_2():
    def __init__(self, m, r):
        self.m = m
        self.r = r

    def cal(self):
        I = self.m * self.r * self.r
        return I
    
    def print(self):
        print("平动:", self.cal())

class delta_and_E():
    def __init__(self, I_1, I_2, theo_value): # theo_value为理论值 
        self.I_1 = I_1
        self.I_2 = I_2
        self.the_value = theo_value
    
    def cal_end(self):
        delta = self.I_2 - self.I_1
        E = min(delta, self.the_value)/max(delta, self.the_value)
        return delta, E
    def print_1(self):
        delta, E = self.cal_end()
        print(f"delta: {delta}\n")
        print(f"E: {E*100} % \n")
    def put(self):
         I = self.m * self.r * self.r
         return I
    
    def print_2(self):
        print("平动:", self.put())

if __name__ == "__main__":

    m = 49.1 # 砝码质量
    g = 9.7949 # 重力加速度
    r = 0.3 # 力臂半径
    alpha_1_1 = 1.980 # 有动力下的角加速度
    alpha_1_f = 0.2010 # 阻力时的加速度

    alpha_2_1 = 1.003
    alpha_2_f = 0.1375


    M = 0.4243 # 铝环质量
    r1 = 0.105 # 内半径
    r2 = 0.12 # 外半径
    
    j_theo_1 = cal(M, r2, r1)

    M1 = 165.4
    R5 =0.105

    j_theo_2 = cal_2(M1, R5)

    j1 = cal_MomentOfInertia(m, g, r, alpha_1_1, alpha_1_f)
    j2 = cal_MomentOfInertia(m, g, r, alpha_2_1, alpha_2_f)

    j1.print()
    j2.print()

    all = delta_and_E(j1.cal(), j2.cal(), j_theo_1.cal_theoreticla_value())

    all.print_1()

    alpha_3_1 = 1.965
    alpha_3_f = 0.2199

    alpha_4_1 = 1.517
    alpha_4_f = 0.1751
    j3 = cal_MomentOfInertia(m, g, r, alpha_3_1, alpha_3_f)
    j4 = cal_MomentOfInertia(m, g, r, alpha_4_1, alpha_4_f)

    # print(j3.cal())
    # print(j4.cal())
    end = delta_and_E(j3.cal(), j4.cal(), j_theo_2.cal())
    # end.print_1()
    


