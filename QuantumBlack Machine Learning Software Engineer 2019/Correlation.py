import math


def Correlation(scores):
    physics = []
    maths = []
    chemistry = []

    for each_scores in scores:
        values = each_scores.split("\t")
        maths.append(int(values[0]))
        physics.append(int(values[1]))
        chemistry.append(int(values[2]))

    length = len(physics)
    value1 = calculate_correlation(maths, physics, length)
    value2 = calculate_correlation(physics, chemistry, length)
    value3 = calculate_correlation(chemistry, maths, length)

    # print(value1)
    # print(value2)
    # print(value3)
    return [str(value1), str(value2), str(value3)]


# return '{}\{}{}'.format(value1, value2, value3)

def calculate_correlation(list1, list2, length):
    # print("into calculate_correlation", list2, list1, length)
    multiply_list = [each[0] * each[1] for each in zip(list1, list2)]

    num_termA = sum(multiply_list) * length
    num_termB = sum(list1) * sum(list2)
    numerator = num_termA - num_termB

    # print("tA: {}, tB: {}, n: {}".format(num_termA, num_termB, numerator))

    denom_calculator = lambda lis, l: math.sqrt((sum(list([pow(each, 2) for each in lis])) * l) - pow(sum(lis), 2))

    denominator = denom_calculator(list1, length) * denom_calculator(list2, length)
    value = round(numerator / denominator, 2)
    # print("deno: {}, value: {}".format(denominator, value))
    return value


class_scores = ['73\t72\t76', '48\t67\t76', '95\t92\t95', '95\t95\t96', '33\t59\t79', '47\t58\t74', '98\t95\t97',
				'91\t94\t97', '95\t84\t90', '93\t83\t90', '70\t70\t78', '85\t79\t91', '33\t67\t76', '47\t73\t90',
				'95\t87\t95', '84\t86\t95', '43\t63\t75', '95\t92\t100', '54\t80\t87', '72\t76\t90']

res = Correlation(class_scores)
print(res)
