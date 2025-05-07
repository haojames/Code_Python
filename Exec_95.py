def compute_sequence(k_values):
    if k_values == 1 or k_values == 2 or k_values == 3:
        return 1
    a, b ,c = 1,1,1
    for _ in range(4, k_values + 1):
        next_val = c + a
        a, b, c = b, c, next_val
    return c

def process_file(input_file, output_file):
    with open(input_file, 'r') as f_in:
        k_values = [int(line.strip()) for line in f_in if line.strip()]
    results = []
    for k in k_values:
        if k < 3:
            results.append(1)
        else:
            a, b, c = 1, 1, 1
            for _ in range(4, k + 1):
                next_val = c + a
                a, b, c = b, c, next_val
            results.append(c)
    with open(output_file, 'w') as f_out:
        for result in results:
            f_out.write(f"{result}\n")
# Thực thi chương trình
process_file('dayso.inp', 'dayso.out')