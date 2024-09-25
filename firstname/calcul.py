def calcul_moyenne(num):
    sum_num = 0

    for i in num :
        sum_num = sum_num + i
    moyenne = sum_num/len(num)
    return moyenne
print('la moyenne est', calcul_moyenne([1, 2, 3, 4]))