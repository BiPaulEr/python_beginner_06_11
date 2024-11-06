for multiplication_table in range(1, 10, 1):
    print("La table de multiplication de "+ str(multiplication_table))
    for i in range(1, 11, 1):
        print(str(multiplication_table)+ "x" + str(i) + "=" + str(i * multiplication_table))