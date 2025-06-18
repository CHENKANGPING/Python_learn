from greenlet import greenlet

def foo():
    print('foo step1')
    gr_bar.switch()
    print('foo step2')
    gr_bar.switch()


def bar():
    print('bar step1')
    gr_foo.switch()
    print('bar step2')


if __name__ == '__main__':
    gr_foo = greenlet(foo)
    gr_bar = greenlet(bar)
    gr_foo.switch()