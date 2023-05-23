from argparse import ArgumentParser, Namespace


def parse_args() -> Namespace:
    args = ArgumentParser()

    args.add_argument('-iL', '--input-list', type=str,
                      help='Input list of emails or haveibeenpwned JSON file')

    args.add_argument('-o', '--output', type=str,
                      default='output.json', help='Output file name')

    args.add_argument('-D', '--active-directory', type=str,
                      help='Active Directory domain')

    args.add_argument('-e', '--email-config', type=str,
                      help='Email configuration file')

    return args.parse_args()
