import argparse as argp


def get_args():
    cli_arg_parser = create_parser()

    return cli_arg_parser.parse_args()


def create_parser():
    parser = argp.ArgumentParser()
    parser.add_argument("--filename")

    return parser
