def decompress(code):
    groups = code.split('_')
    decode = ''
    for number, count in groups:
        decode = decode + number * int(count)
    return int(decode)


print(decompress('14_53_22_51_02'))