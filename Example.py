from Linear_Func import linear_regression
# 数据组1
listx_1 = [1.569, 1.518, 1.473, 1.405, 1.289, 1.176, 0.9863]
listy_1 = [-0.1338, -0.1772, -0.2058, -0.2211, -0.2924, -0.3128, -0.4156]

# 数据组2
listx_2 = [1.569, 1.518, 1.473, 1.405, 1.289, 1.176, 0.9863, 1.569, 1.518, 1.473, 1.405, 1.289, 1.176, 0.9863]
listy_2 = [-0.1338, -0.1772, -0.2058, -0.2211, -0.2924, -0.3128, -0.4156, -0.1338, -0.1772, -0.2058, -0.2211, -0.2924, -0.3128,-0.4156]

if __name__ == '__main__':

    one =  linear_regression(listx_1, listy_1)
    one.print_the_func()
    two =  linear_regression(listx_2, listy_2)
    two.print_the_func()
    one.Draw()