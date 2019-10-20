# import argparse
# import os


# def check_file(extensions: [str] = None):
#     class FileChecker(argparse.Action):
#         def __call__(self, parser, namespace, files, option_string=None):
#             for file in files:
#                 if not os.path.exists(file):
#                     parser.error(f'file \'{file}\' does not exists')
#                 if not extensions:
#                     continue
#                 ext = file.split('.')[-1]
#                 if ext not in extensions:
#                     parser.error(f'file extension \'{ext}\' not allowed. Choices are \'{", ".join(extensions)}\'')
#             setattr(namespace, self.dest, files)
#     return FileChecker


# def get_arguments():
#     """ Returns an argparse object generated from the command line arguments given """
#     verbose = argparse.ArgumentParser(description='Process verbose arguments')
#     app_input = argparse.ArgumentParser(description='Process app input arguments')
#     verbose.add_argument('-v', '--verbosity', type=int,
#                         action='store', dest='verbosity_level',
#                         help='verbosity level')
#     verbose.add_argument('-s', '--silent', type=bool,
#                          action='store_true', dest='silent',
#                          help='makes the app completely silent')
#     app_input.add_argument('files', nargs='+',
#                            action=check_file(['nzb']))
#     return app_input.parse_args()


def main():
    """ Application entry point """
    # verbose, input = get_arguments()
    pass


if __name__ == '__main__':
    main()
