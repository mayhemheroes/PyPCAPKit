#!/usr/bin/env python3
import atheris
import tempfile
import logging
import sys

logging.disable(logging.ERROR)

with atheris.instrument_imports():
    import pcapkit


@atheris.instrument_func
def TestOneInput(data):
    try:
        with tempfile.NamedTemporaryFile('wb+', suffix='.pcap') as t_file:
            t_file.write(data)
            t_file.flush()
            pcapkit.extract(fin=t_file.name, nofile=True)
    except pcapkit.BaseError:
        return -1


def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == '__main__':
    main()
