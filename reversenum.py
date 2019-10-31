import logging

logging.basicConfig(level=logging.INFO)
def reverse(x):

    try:
        logging.info('The value of x is {x}'.format(x={x}))
        neg = 0

        if x < 0:
            neg = 1
            x = x * -1

        x = int(str(x)[::-1])

        if x > 2 ** 31:
            logging.error('Out of 32 bit signed integer range, returning 0')
            return 0
        if neg == 1:
            x = x * -1
        return x
    except:
        logging.critical('Did not get correct format for x')

print(reverse(105))
print(reverse(-728))
print(reverse(3))
print(reverse(2**32))
print(reverse('hello'))


# kwargs = {'a':'2**32', 'b':reverse(2**32)}
# logging.debug('a={a}, b={b}'.format(**kwargs))
# logging.info("The reverse of {a} is {b}".format(**kwargs))
# logging.warning('a={a} and b={b} are the same number'.format(**kwargs))
# logging.error('a={a} is greater than 2**31'.format(**kwargs))
# logging.critical('a={a} is not an integer'.format(**kwargs))
