def process_numbers(a, b):
    """
    Kiểm tra xem a có chia hết cho b không và tính tổng các bội số chung nhỏ hơn 100.

    :param a: Số nguyên dương thứ nhất.
    :param b: Số nguyên dương thứ hai.
    :return: Kết quả kiểm tra chia hết và tổng bội số chung.
    """
    is_divisible = False
    if (a % b == 0) or (b % a == 0):
        is_divisible = True
    
    total = 0  

    for i in range(1, 100):  
        if i % a == 0 and i % b == 0:  # p-use(a, b)
            total += i  # c-use(total, i)

    if total > 50:  
        return is_divisible, total  
    return is_divisible
