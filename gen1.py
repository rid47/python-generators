def infinite_sequence():
    num  = 0
    while True:
        return num
        num += 1




def infinite_sequence_gen():
    num = 0
    while True:                
        # num += 1
        yield num
        num += 1  
        yield "This is the second yield"



def finite_list():
    nums = [1,2,3]
    for num in nums:
        yield num


nums_squared_lc = [x**2 for x in range(5)]
nums_squared_gc = (x**2 for x in range(5))


