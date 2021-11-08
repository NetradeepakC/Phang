class equation:

    def __init__(self, point_list, value_list=0):
        if(value_list == 0):
            value_list = [30 for i in range(len(point_list))]
        self.value = value_list[0]
        if(len(point_list) > 1):
            i = 0
            while(point_list[i][0] == 0):
                i += 1
            sub_point_list = []
            sub_value_list = []
            for j in range(len(point_list)):
                if(j != i):
                    temp = []
                    for k in range(1, len(point_list[j])):
                        temp.append(point_list[j][k]-point_list[j][0]
                                    * point_list[i][k]/point_list[i][0])
                    sub_point_list.append(temp)
                    sub_value_list.append(
                        value_list[j]*(1-point_list[j][0]/point_list[i][0]))
            partial_equation = equation(sub_point_list, sub_value_list)
            temp = self.value
            for j in range(len(partial_equation.coefficient_list)):
                temp -= partial_equation.coefficient_list[j]*point_list[i][j+1]
            temp /= partial_equation.coefficient_list[i][0]
            self.coefficient_list = [temp]
            self.coefficient_list.extend(partial_equation.coefficient_list)

        else:
            self.coefficient_list = [self.value /
                                     point_list[0].coefficient_list[0]]

    def value_in_equation(self, point):
        temp = -self.value
        for i in range(len(point)):
            temp += self.coefficient_list[i]*point[i]
        return temp

    def get_transform_matrix():
        pass
