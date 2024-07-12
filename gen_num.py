
def generate(num_digit=4, base=10):
    nums = _generate([], [], num_digit, base)
    return nums

def _generate(result, tmp, num_digit=4, base=10):
    if len(tmp) < num_digit:
        _tmp = list(tmp) + [None]
        for next_num in range(base):
            if not next_num in tmp:
                _tmp[-1] = next_num
                _generate(result, tuple(_tmp))
    else: 
        # base case
        result += [tuple(tmp)]
    return result

if __name__ == '__main__':
    generate()
