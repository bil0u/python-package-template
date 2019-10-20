# import argparse
# import os


# def check_file(extensions: [str] = None):
#     class FileChecker(argparse.Action):
#         def __call__(self, parser, namespace, filepath, option_string=None):
#             print(filepath)
#             if not os.path.exists(filepath):
#                 parser.error('file does not exists')
#             if extensions and filepath.split('.')[-1] not in extensions:
#                 parser.error(f'file extension not allowed. Choices are \'{", ".join(extensions)}\'')
#             setattr(namespace, self.dest, filepath)
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
#                            action=check_file(['nzb']), dest='files')
#     return app_input.parse_args()


def main():
    """ Application entry point """
    # verbose, input = get_arguments()
    pass


if __name__ == '__main__':
    main()
