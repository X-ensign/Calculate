# const_StartX = 0
# const_EndX = 0
# const_SpaceX = 0

# const_StartY = 0
# const_EndY = 0
# const_SpaceY = 0
import Cal_R_and_Rate
import numpy as np
import matplotlib.pyplot as plt

class linear_regression:
    
    # x为数组，y为数组
    def __init__(self, x, y):
        self.x = np.array(x)
        self.y = np.array(y)

    # 计算数据
    def Data_Process(self):
        sum_of_xx = 0.0
        for i in self.x:
            sum_of_xx = sum_of_xx + i*i
        sum_of_x = 0.0
        for i in self.x:
            sum_of_x = sum_of_x + i
        sum_of_xy = 0.0
        for i in range(len(self.x)):
            sum_of_xy = sum_of_xy + self.x[i]*self.y[i]
        sum_of_y = 0.0
        for i in self.y:
            sum_of_y = sum_of_y + i

        avarage_x = sum_of_x / len(self.x)
        avarage_y = sum_of_y / len(self.y)

        up = 0.0
        for i in range(len(self.x)):
            up = up + (self.x[i] - avarage_x) * (self.y[i] - avarage_y)
        down = 0.0 
        for i in range(len(self.x)):
            down = down + (self.x[i]-avarage_x)*(self.x[i]-avarage_x)

        B = up / down
        A = avarage_y - B * avarage_x

        return A, B 

    def Cal_rr(self):
        A,B = self.Data_Process()
        sum_of_y = 0.0
        for i in range(len(self.y)):
            sum_of_y = sum_of_y + self.y[i]
        avarage_y = sum_of_y / len(self.y)
        RSS = 0.0
        for i in range(len(self.y)):
            RSS = RSS + (self.y[i] - A - B * self.x[i]) * (self.y[i] - A - B * self.x[i])
        TSS = 0.0
        for i in range(len(self.y)):
            TSS = TSS + (self.y[i] - avarage_y) * (self.y[i] - avarage_y)
        
        rr = 1 - RSS / TSS
        return rr
    def Draw(self):
        A,B = self.Data_Process()
        # 画图像
        plt.figure()#使用plt.figure定义一个图像窗口
        plt.title('single variable')#图像标题
        plt.xlabel('x')#x轴标题
        plt.ylabel('y')#y轴标题
        plt.grid(True)#是否打开网格
        #while(1):
        plt.clf()# 清除图像

        # 设置 x 轴刻度
        plt.xticks(np.arange(min(self.x)-10, max(self.x)+5, 30))
        # 设置 y 轴刻度
        plt.yticks(np.arange(min(self.y)-0.001, max(self.y)+0.001 , 0.05))
        plt.scatter(self.x, self.y) # 绘制散点
        # 标注坐标点的值
        for i in range(len(self.x)):
            plt.text(self.x[i], self.y[i], f'({self.x[i]}, {self.y[i]:.2f})', fontsize=8, color='red')
        
        plt.plot(self.x, A + B * self.x, 'g') # 绘制方程图形
        plt.show()


    def predict(self,  input_x):
        A,B = self.Data_Process()
        return A + B * input_x
    # 打印方程
    def print_the_func(self):
        A,B = self.Data_Process()
        a = "%.4f"% A 
        b = "%.4f"% B
        print(f"The Function is:\nY = {b}*X + {a}")

if __name__ == "__main__":
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

    List_1 = Cal_R_and_Rate.List_Cal(list_R1[1:], list_R1[0]) # 弱磁场区域的增量表
    List_2 = Cal_R_and_Rate.List_Cal2(list_R2, list_R1[0]) # 强磁场区域的增量表

    example_1 = linear_regression(B_1, List_1)
    example_2 = linear_regression(B_2, List_2)

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



