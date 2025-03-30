while True:
    try:
        n = int(input())

        if n == -1:  # Para funcionar no jupyter (não incluso no código)
            break

        if n == 0:
            print('vai ter copa!')
        else:
            print('vai ter duas!')

    except EOFError:
        break
