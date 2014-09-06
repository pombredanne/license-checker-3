#!/usr/bin/env python3
import argparse

import licensechecker

def get_args():
    parser = argparse.ArgumentParser(description=licensechecker.__description__)
    return parser.parse_args()


def main():
    args = get_args()


if __name__ == '__main__':
    main()
