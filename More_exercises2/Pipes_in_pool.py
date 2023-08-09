volume_pool_in_liters = int(input())
debit_first_pipe = int(input())
debit_second_pipe = int(input())
hours_absence = float(input())

filling_pool_first_pipe = hours_absence * debit_first_pipe
filling_pool_second_pipe = hours_absence * debit_second_pipe
total_filling_pool = filling_pool_second_pipe + filling_pool_first_pipe

percent_filling_first_pipe = (filling_pool_first_pipe / total_filling_pool) * 100
percent_filling_second_pipe = (filling_pool_second_pipe / total_filling_pool) * 100
percent_filling_pool = (total_filling_pool / volume_pool_in_liters) * 100

if total_filling_pool <= volume_pool_in_liters:
    print(f"The pool is {percent_filling_pool:.2f}% full."
          f" Pipe 1: {percent_filling_first_pipe:.2f}%. "
          f"Pipe 2: {percent_filling_second_pipe:.2f}%.")
else:
    print(f"For {hours_absence:.2f} "
          f"hours the pool overflows with "
          f"{total_filling_pool - volume_pool_in_liters:.2f} liters.")
