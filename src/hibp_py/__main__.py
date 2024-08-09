import hibp_py.api as api
import hibp_py.args as args
import hibp_py.db as db
import hibp_py.mail as mail
import hibp_py.utils as utils
import time


def main():
    config = utils.load_config()
    logger = utils.Logger()

    if 'LOG_PATH' in config:
        logger.__setattr__('path', config['LOG_PATH'])

    if 'ROTATION_SIZE' in config:
        logger.__setattr__('rotation_size', config['ROTATION_SIZE'])

    print('Welcome to HIBP Python!')

    arguments = args.parse_args()

    if arguments.input_list:
        with open(arguments.input_list, 'r', encoding='utf-16') as f:
            accounts = f.read().splitlines()

        for account in accounts:
            logger.log_event(f'Checking {account}...', 'INFO')
            success = False
            new_breaches = []

            while not success:
                try:
                    breaches = api.get_breaches(account)
                    success = True
                except api.RateLimitError as e:
                    utils.handle_rate_limit(logger)
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
                                utils.handle_rate_limit(logger)
                                time.sleep(6)

                    if db.write_breach(account, breach_data):
                        logger.log_event(
                            f'New breach found: {breach_name}', 'BREACH')

                        new_breaches.append(breach_name)

                    success = True
                except api.RateLimitError as e:
                    utils.handle_rate_limit(logger)

            if new_breaches:
                mail.send_email(account, mail.create_body(
                    account, new_breaches))

            time.sleep(6)


if __name__ == '__main__':
    main()
