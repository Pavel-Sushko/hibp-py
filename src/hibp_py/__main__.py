import time
import api
import args
import db


def main():
    print('Welcome to HIBP Python!')

    arguments = args.parse_args()

    if arguments.input_list:
        with open(arguments.input_list, 'r', encoding='utf-16') as f:
            accounts = f.read().splitlines()

        for account in accounts:
            print(f'Checking {account}...')
            success = False

            while not success:
                try:
                    breaches = api.get_breaches(account)
                    success = True
                except api.RateLimitError as e:
                    print(f'Rate limit exceeded. Waiting 6 seconds...')
                    time.sleep(6)

            for breach in breaches:
                time.sleep(6)

                success = False

                try:
                    db.write_breach(account, api.get_breach(breach['Name']))
                    success = True
                except api.RateLimitError as e:
                    print(f'Rate limit exceeded. Waiting 6 seconds...')
                    time.sleep(6)

            time.sleep(6)


if __name__ == '__main__':
    main()
