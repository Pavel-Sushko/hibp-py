import hibp_py.api as api
import hibp_py.args as args
import hibp_py.db as db
import hibp_py.mail as mail
import time


def main():
    print('Welcome to HIBP Python!')

    arguments = args.parse_args()

    if arguments.input_list:
        with open(arguments.input_list, 'r', encoding='utf-16') as f:
            accounts = f.read().splitlines()

        for account in accounts:
            print(f'Checking {account}...')
            success = False
            new_breaches = []

            while not success:
                try:
                    breaches = api.get_breaches(account)
                    success = True
                except api.RateLimitError as e:
                    print(f'Rate limit exceeded. Waiting 6 seconds...')
                    time.sleep(6)

            for breach in breaches:

                breach_name = breach['Name']
                success = False

                try:
                    breach_data = db.get_breach(breach_name)

                    if not breach_data:
                        while not success:
                            try:
                                breach_data = api.get_breach(breach_name)
                                success = True
                            except api.RateLimitError as e:
                                print(f'Rate limit exceeded. Waiting 6 seconds...')
                                time.sleep(6)

                    if db.write_breach(account, breach_data):
                        print(f'New breach found: {breach_name}')

                        new_breaches.append(breach_name)

                    success = True
                except api.RateLimitError as e:
                    print(f'Rate limit exceeded. Waiting 6 seconds...')
                    time.sleep(6)

            if new_breaches:
                mail.send_email(account, mail.create_body(
                    account, new_breaches))

            time.sleep(6)


if __name__ == '__main__':
    main()
