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
    
    for i in range(len(List_1_1)):
        print(List_1_1[i])

    print("")

    for i in range(len(List_1_2)):
        print(List_1_2[i])

    print("")
    
    for i in range(len(List_2)):
        print(List_2[i])

