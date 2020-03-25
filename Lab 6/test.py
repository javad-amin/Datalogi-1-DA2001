

from vectors import (add_vectors,
                     subtract_vectors,
                     multiply_vector_by,
                     divide_vector_by)

    
ta = [
    [[], [], []],
    [[-9, -6, 0, -8, 4, -2, -5, 10, 1, 12, 1], [-4, 17, -5, 2, 5, -5, -8, -7, 17, 14, 16], [-13, 11, -5, -6, 9, -7, -13, 3, 18, 26, 17]],
    [[-10, 9, -3, 4, 20, 14, -1, 5, -4, -5], [2, 10, 9, 1, 5, 19, 16, 9, 19, -6], [-8, 19, 6, 5, 25, 33, 15, 14, 15, -11]],
    [[0, 11, -2], [17, -8, -2], [17, 3, -4]],
    [[-6, -7], [18, 14], [12, 7]],
    [[10, 15, 8, -4], [-1, 11, 16, 17], [9, 26, 24, 13]],
    [[2, 8, 13, 20, 15, 16, 6, 17], [18, 13, -7, 10, 7, -4, -3, -7], [20, 21, 6, 30, 22, 12, 3, 10]],
    [[6, 19], [5, 15], [11, 34]],
    [[18, 6, 8, 6, 20, 3, 5, 3, 11, 17], [-5, 1, -3, -6, 7, 11, 5, 8, 6, 19], [13, 7, 5, 0, 27, 14, 10, 11, 17, 36]],
    [[7, 19], [20, -6], [27, 13]],
    [[-4, -7], [-9, -10], [-13, -17]],
    [[-4, 15, 9, 12, -7], [7, 6, 17, 1, 3], [3, 21, 26, 13, -4]],
    [[-3, -5], [-3, 16], [-6, 11]],
    [[13, -1, 16, 5, 15, 19, -4, 18, -8, 0, -4], [14, 18, -10, -6, 7, 20, 11, -5, 16, 16, 15], [27, 17, 6, -1, 22, 39, 7, 13, 8, 16, 11]],
    [[-4, 19, 15, -8, 8, 6, 7, 20, 3, 3], [-9, 8, 15, 5, -9, 16, -1, 4, 7, 4], [-13, 27, 30, -3, -1, 22, 6, 24, 10, 7]],
    [[-4, 19, 18, 7, -2, 18], [-5, 10, 2, -5, 17, 3], [-9, 29, 20, 2, 15, 21]],
    [[18, 18, 6, -5, 9, -9, 7, 5, 4], [-3, -9, -1, 11, -4, 14, 6, 13, 0], [15, 9, 5, 6, 5, 5, 13, 18, 4]],
    [[1, 18, -1, -1, 4], [19, 10, 9, 18, -5], [20, 28, 8, 17, -1]],
    [[2, 15, 1, 15, 17, 9, -9, 14], [12, 17, -1, 3, 6, -7, -5, 13], [14, 32, 0, 18, 23, 2, -14, 27]],
    [[6, 5, 14], [-4, 16, -3], [2, 21, 11]],
    [[0, -8, 2, 18, 1, 17, 1, -6], [-3, 5, 1, 1, 3, -3, 5, 3], [-3, -3, 3, 19, 4, 14, 6, -3]]
]

ts = [
    [[], [], []],
    [[-9, -6, 0, -8, 4, -2, -5, 10, 1, 12, 1], [-4, 17, -5, 2, 5, -5, -8, -7, 17, 14, 16], [-5, -23, 5, -10, -1, 3, 3, 17, -16, -2, -15]],
    [[-10, 9, -3, 4, 20, 14, -1, 5, -4, -5], [2, 10, 9, 1, 5, 19, 16, 9, 19, -6], [-12, -1, -12, 3, 15, -5, -17, -4, -23, 1]],
    [[0, 11, -2], [17, -8, -2], [-17, 19, 0]],
    [[-6, -7], [18, 14], [-24, -21]],
    [[10, 15, 8, -4], [-1, 11, 16, 17], [11, 4, -8, -21]],
    [[2, 8, 13, 20, 15, 16, 6, 17], [18, 13, -7, 10, 7, -4, -3, -7], [-16, -5, 20, 10, 8, 20, 9, 24]],
    [[6, 19], [5, 15], [1, 4]],
    [[18, 6, 8, 6, 20, 3, 5, 3, 11, 17], [-5, 1, -3, -6, 7, 11, 5, 8, 6, 19], [23, 5, 11, 12, 13, -8, 0, -5, 5, -2]],
    [[7, 19], [20, -6], [-13, 25]],
    [[-4, -7], [-9, -10], [5, 3]],
    [[-4, 15, 9, 12, -7], [7, 6, 17, 1, 3], [-11, 9, -8, 11, -10]],
    [[-3, -5], [-3, 16], [0, -21]],
    [[13, -1, 16, 5, 15, 19, -4, 18, -8, 0, -4], [14, 18, -10, -6, 7, 20, 11, -5, 16, 16, 15], [-1, -19, 26, 11, 8, -1, -15, 23, -24, -16, -19]],
    [[-4, 19, 15, -8, 8, 6, 7, 20, 3, 3], [-9, 8, 15, 5, -9, 16, -1, 4, 7, 4], [5, 11, 0, -13, 17, -10, 8, 16, -4, -1]],
    [[-4, 19, 18, 7, -2, 18], [-5, 10, 2, -5, 17, 3], [1, 9, 16, 12, -19, 15]],
    [[18, 18, 6, -5, 9, -9, 7, 5, 4], [-3, -9, -1, 11, -4, 14, 6, 13, 0], [21, 27, 7, -16, 13, -23, 1, -8, 4]],
    [[1, 18, -1, -1, 4], [19, 10, 9, 18, -5], [-18, 8, -10, -19, 9]],
    [[2, 15, 1, 15, 17, 9, -9, 14], [12, 17, -1, 3, 6, -7, -5, 13], [-10, -2, 2, 12, 11, 16, -4, 1]],
    [[6, 5, 14], [-4, 16, -3], [10, -11, 17]],
    [[0, -8, 2, 18, 1, 17, 1, -6], [-3, 5, 1, 1, 3, -3, 5, 3], [3, -13, 1, 17, -2, 20, -4, -9]]
]

tm = [
    [3, [], []],
    [2, [-2, -3, 2, 19, -6], [-4, -6, 4, 38, -12]],
    [6, [-8, 17, 16, 17, 9, -1, -9], [-48, 102, 96, 102, 54, -6, -54]],
    [11, [3, 17, 18, -7, 14, 1, -3, -10], [33, 187, 198, -77, 154, 11, -33, -110]],
    [9, [-7, 10], [-63, 90]],
    [8, [18], [144]],
    [8, [4, -5, 0, 2], [32, -40, 0, 16]],
    [8, [2], [16]],
    [7, [-2, 0, -7, 13, 13, 4, 13], [-14, 0, -49, 91, 91, 28, 91]],
    [7, [-10, 2, 7, -9, -2, 14, 14, 0, 9, -8], [-70, 14, 49, -63, -14, 98, 98, 0, 63, -56]],
    [2, [-7], [-14]],
    [1, [-4, 7, 6, 16, -7, 6, -6, 0, 19, 9], [-4, 7, 6, 16, -7, 6, -6, 0, 19, 9]],
    [1, [12, 16, -9], [12, 16, -9]],
    [9, [11, 3, -8, 2, 3, 5], [99, 27, -72, 18, 27, 45]],
    [11, [19, -6], [209, -66]],
    [5, [-6, -6, 0, -1, 20, 16, 17], [-30, -30, 0, -5, 100, 80, 85]],
    [10, [-4, 14, 20], [-40, 140, 200]],
    [10, [9, 2, 3, -4, 9, -3, -6, 13, -1, -5], [90, 20, 30, -40, 90, -30, -60, 130, -10, -50]],
    [2, [-7, 19], [-14, 38]],
    [6, [8], [48]],
    [10, [17, 14, -10, 20, 14, -3, 6, -3, -2, 6, -8], [170, 140, -100, 200, 140, -30, 60, -30, -20, 60, -80]]
]

td = [
    [3, [], []],
    [2, [-2, -3, 2, 19, -6], [-1.0, -1.5, 1.0, 9.5, -3.0]],
    [6, [-8, 17, 16, 17, 9, -1, -9], [-1.3333333333333333, 2.8333333333333335, 2.6666666666666665, 2.8333333333333335, 1.5, -0.16666666666666666, -1.5]],
    [11, [3, 17, 18, -7, 14, 1, -3, -10], [0.2727272727272727, 1.5454545454545454, 1.6363636363636365, -0.6363636363636364, 1.2727272727272727, 0.09090909090909091, -0.2727272727272727, -0.9090909090909091]],
    [9, [-7, 10], [-0.7777777777777778, 1.1111111111111112]],
    [8, [18], [2.25]],
    [8, [4, -5, 0, 2], [0.5, -0.625, 0.0, 0.25]],
    [8, [2], [0.25]],
    [7, [-2, 0, -7, 13, 13, 4, 13], [-0.2857142857142857, 0.0, -1.0, 1.8571428571428572, 1.8571428571428572, 0.5714285714285714, 1.8571428571428572]],
    [7, [-10, 2, 7, -9, -2, 14, 14, 0, 9, -8], [-1.4285714285714286, 0.2857142857142857, 1.0, -1.2857142857142858, -0.2857142857142857, 2.0, 2.0, 0.0, 1.2857142857142858, -1.1428571428571428]],
    [2, [-7], [-3.5]],
    [1, [-4, 7, 6, 16, -7, 6, -6, 0, 19, 9], [-4.0, 7.0, 6.0, 16.0, -7.0, 6.0, -6.0, 0.0, 19.0, 9.0]],
    [1, [12, 16, -9], [12.0, 16.0, -9.0]],
    [9, [11, 3, -8, 2, 3, 5], [1.2222222222222223, 0.3333333333333333, -0.8888888888888888, 0.2222222222222222, 0.3333333333333333, 0.5555555555555556]],
    [11, [19, -6], [1.7272727272727273, -0.5454545454545454]],
    [5, [-6, -6, 0, -1, 20, 16, 17], [-1.2, -1.2, 0.0, -0.2, 4.0, 3.2, 3.4]],
    [10, [-4, 14, 20], [-0.4, 1.4, 2.0]],
    [10, [9, 2, 3, -4, 9, -3, -6, 13, -1, -5], [0.9, 0.2, 0.3, -0.4, 0.9, -0.3, -0.6, 1.3, -0.1, -0.5]],
    [2, [-7, 19], [-3.5, 9.5]],
    [6, [8], [1.3333333333333333]],
    [10, [17, 14, -10, 20, 14, -3, 6, -3, -2, 6, -8], [1.7, 1.4, -1.0, 2.0, 1.4, -0.3, 0.6, -0.3, -0.2, 0.6, -0.8]]
]

def addition_test():
    for v1,v2,summa in ta:
        try:
            assert add_vectors(v1,v2) == summa
        except AssertionError:
            print("Fel: ")
            print(v1,v2,summa)


def subtraction_test():
    for v1,v2,diff in ts:
        try:
            assert subtract_vectors(v1,v2) == diff
        except AssertionError:
            print("Fel: ")
            print(v1,v2,diff)


def multiplication_test():
    for a,v,prod in tm:
        try:
            assert multiply_vector_by(v,a) == prod
        except AssertionError:
            print("Fel: ")
            print(a,v,prod)

def float_approx_equal(v1,v2):
    epsilon = 1e-6
    for a,b in zip(v1,v2):
        if (abs(a-b) > epsilon) and (abs(a/b) - 1 > epsilon):
            return False
    return True

def division_test():
    for a,v,quotient in td:
        try:
            assert float_approx_equal(divide_vector_by(v,a),quotient)
        except AssertionError:
            print("Fel: ")
            print(a,v,quotient)


def all_tests():
    division_test()
    subtraction_test()
    multiplication_test()
    addition_test()
    print("Tests done.")
    print("(No output - no errors in tests.)")

if __name__ == "__main__":
    all_tests()

