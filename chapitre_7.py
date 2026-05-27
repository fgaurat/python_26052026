def main():
    a = 2
    b = 3
    c = a/b
    
    result = f"{a=:.2f} / {b=:.2f} = {c=:.0%}"
    print(result)


    results = [a,b,c]

    # result = "a={0} / b={1} = c={2}".format(results[0],results[1],results[2])
    result = f"{results[0]:.2f} / {results[1]:.2f} = {results[2]:.0%}"
    print(result)
    result = "a={0} / b={1} = c={2:.0%}".format(*results)
    print(result)

    result = "a={value_a} b={value_b} c={value_c}".format(value_a=a,value_b=b,value_c=c)
    print(result)

    d = {
        "value_a":a,
        "value_b":b,
        "value_c":c
    }

    result = "a={value_a} b={value_b} c={value_c}".format(**d)
    print(result)


if __name__=='__main__':
    main()
