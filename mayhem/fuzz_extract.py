#!/usr/bin/env python3
import atheris
import io
import logging
import sys
from contextlib import contextmanager

with atheris.instrument_imports(include=['pcapkit']):
    import pcapkit
    from pcapkit.foundation.extraction import Extractor

logging.disable(logging.ERROR)


@contextmanager
def disabledrun():
    save_run = pcapkit.foundation.extraction.Extractor.run
    pcapkit.foundation.extraction.Extractor.run = lambda self: None
    yield
    pcapkit.foundation.extraction.Extractor.run = save_run


bogus_pcap_file = open('in.pcap', 'wb+')
bogus_pcap_file.close()


with disabledrun():
    extractor = Extractor(nofile=True)

@atheris.instrument_func
def TestOneInput(data):
    # Too slow using expected on-disk file, so monkey-patch to allow using io.BytesIO for same functionality
    # Constructor calls run(), so we need to disable it
    try:
        pcap_file = io.BytesIO(data)
        pcap_file.name = 'foo.pcap'
        extractor._ifile = pcap_file
        extractor.run()
    except (pcapkit.BaseError, AttributeError):
        return -1


def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == '__main__':
    # Get bytes from testsuite file
    main()

