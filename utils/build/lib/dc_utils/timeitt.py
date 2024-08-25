from functools import reduce, wraps
import logging
import time
from typing import Any, Collection, Callable

log_format = '%(name)s : %(levelname)s : %(asctime)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, format=log_format)
logger = logging.getLogger('timeit')

type Composable = Callable[[Any], Any]


def mapper(converter: Callable) -> Callable:
    def do_map(items: Collection) -> tuple:
        return tuple(map(converter, items))
    return do_map


def joiner(sep: str) -> Callable:
    def do_join(value: Collection) -> str:
        return sep.join(filter(bool, value))
    return do_join


def combiner(*functions: Composable) -> Composable:
    def apply(value: Any, fn: Composable) -> Any:
        return fn(value)

    return lambda val: reduce(apply, functions, val)


def shorten(value: str):
    if len(value) > 10:
        return f"{value[:4]}...{value[-4:]}"
    return value


def timeitt(runs: int = 100):
    str_mapper = mapper(str)
    str_shorten = mapper(shorten)
    coma_joiner = joiner(", ")

    kwargs_handler = combiner(mapper(str_mapper), mapper(joiner(" = ")))
    signature_handler = combiner(mapper(coma_joiner), coma_joiner)

    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            kwargs_t = kwargs.items()
            stats = []

            for _ in range(runs):
                start = time.perf_counter()
                result = f(*args, **kwargs)
                stats.append(time.perf_counter() - start)

            all_args = signature_handler(
                (str_shorten(str_mapper(args)),
                 str_shorten(kwargs_handler(kwargs_t)),),)

            logger.debug(f"{f.__name__}({all_args}) | {
                         runs} runs | AVG run time: {sum(stats) / runs:.8f}")
            return result

        return wrapper

    return decorator
