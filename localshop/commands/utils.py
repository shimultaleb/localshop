from optparse import make_option

opt = make_option


def options(*options):
    def wrapped(func):
        func.options = options
        return func
    return wrapped


def consume_args(func):
    func.consume_args = True
    return func

