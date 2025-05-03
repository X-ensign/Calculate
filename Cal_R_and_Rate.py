import Linear_Func as lf
import math 
# 计算增率
def Cal_Rate(R, R0):
    return ((R - R0) / R0)

def Cal_Rate_sqrt(R, R0):
    return math.sqrt(Cal_Rate(R, R0))

def List_Cal(List1, R0):
    List = []
    for i in range(len(List1)):
        List.append(Cal_Rate_sqrt(List1[i], R0))
    return List

def List_Cal2(List2, R0):
    List = []
    for i in range(len(List2)):
        List.append(Cal_Rate(List2[i], R0))
    return List


if __name__ == "__main__":

    list_R1 = [344, 346, 354, 365, 379, 396, 415,]
    list_R1.sort() # 排序
    list_R2 = [512, 568, 572, 591, 630, 646, 663, 704, 728, 735]
    list_R2.sort() # 排序
    
    List_1_2 = List_Cal2(list_R1,list_R1[0]) # 不开根号
    List_1_1 = List_Cal(list_R1,list_R1[0]) # 开根号
    List_2 = List_Cal2(list_R2, list_R1[0])

    B_1 = [10,20,30,40,50,60]
    B_2 =[120, 170, 200, 220, 270, 300, 320, 370, 400, 410]
    B_2.sort()
    # 零点校正后的对应磁场强度和电压标准值
    B_Standard = 206.4
    U_Standard = 579
    # 数据表
    list_R1 = [344, 346, 354, 365, 379, 396, 415,]

    list_R1.sort() # 排序
    list_R2 = [512, 568, 572, 591, 630, 646, 663, 704, 728, 735]
    list_R2.sort() # 排序
    Y = (U_Standard-list_R1[0])/list_R1[0] # 计算增量

    List_1 = List_Cal(list_R1[1:], list_R1[0]) # 弱磁场区域的增量表
    List_2 = List_Cal2(list_R2, list_R1[0]) # 强磁场区域的增量表

    example_1 = lf.linear_regression(B_1, List_1)
    example_2 = lf.linear_regression(B_2, List_2)

    A,B = example_2.Data_Process() # B:斜率 A:截距

    choice = 2
    if choice == 1:
        # [[-1, 1, 3], [-0.1, 0.1, 0.02]]
        example_1.print_the_func()
        rr = example_1.Cal_rr()
        print (f"相关系数是:{rr}\n")
        example_1.Draw()

    elif choice == 2:
        # [[-2, 2, 18], [-0.5, 0.5, 0.05]]
        example_2.print_the_func()
        Y_B = (Y-A)/B # 找到增量所对应的磁场强度
        print(f"Y = {Y}")
        print(f"对应的磁场强度B: = {Y_B}")
        D = example_2.Cal_rr()
        print(f"相关系数是:{D}\n")
        E = ((Y_B-B_Standard)/B_Standard)*100
        print(f"误差是:{E}%")
        example_2.Draw()

