import argparse
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ml', action='store_true', help='Flag for machine learning service')
    parser.add_argument('--path', type=str, help='Path for machine learning dataset')
    parser.add_argument('--bot', action='store_true', help='Flag for telegram bot service')
    parser.add_argument('--model', type=str, help='Model path for telegram bot')
    args = parser.parse_args()
    if args.ml and args.path:
        from cliogan import make_clio_gan
        make_clio_gan(args.path)
    elif args.bot and args.model:
        from clio_tg_bot import run_clio_telegram_bot
        run_clio_telegram_bot(args.model)
    else:
        print(os.environ.get('READ_ME'))


if __name__ == "__main__":
    main()
