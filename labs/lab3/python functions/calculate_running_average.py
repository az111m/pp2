def calculate_running_average(numbers):
    running_sum = 0
    running_average_list = []
    for i, num in enumerate(numbers, start=1):
        running_sum += num
        running_average = running_sum / i
        running_average_list.append(running_average)
    return running_average_list

numbers = [5, 10, 15, 20, 25]
running_averages = calculate_running_average(numbers)
print("Running averages:", running_averages)