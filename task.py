def task(input): # the value of input is an integer which is the total money available

    result = {}

    result("Needs") = input * 0.5
    result("Wants") = input * 0.3
    result("Savings") = input * 0.2

    return result 