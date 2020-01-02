import argparse
from tf_easy_install.logging_ import Logger
logger = Logger(__name__, create=True).logger
from tf_easy_install import anaconda_

def main(args):

    if not args.anaconda and not args.user:
        logger.critical("You must specify the install environment: '-a/--anaconda' or '-u/--user'")
        return

    if args.anaconda:
        logger.info("Selected install environment: Anaconda")
        
        success = anaconda_.install(args)
        if success:
            logger.info(f"Anaconda environment successfully installed and tested, please run 'conda activate {args.name}' to use the newly installed environment")
        return success



if __name__ == "__main__":
    logger.debug("Beginning installation")
    parser = argparse.ArgumentParser(description="Auotmatically install a Tensorflow environment")
    installGroup = parser.add_mutually_exclusive_group()

    installGroup.add_argument("-a", "--anaconda", help="install Tensorflow into a conda environment", action="store_true")
    installGroup.add_argument("-u", "--user", help="install Tensorflow into a user environment", action="store_true")

    parser.add_argument("-g", "--gpu", help="install Tensorflow-GPU", action="store_true")

    parser.add_argument("-v", "--version", help="install a specific version of Tensorflow", type=str, default="2.0.0")
    parser.add_argument("-n", "--name", help="the name of the anaconda environment", type=str, default="tensorflow1")

    parser.add_argument("-y", "--yes", help="skip any confirmations. Warning: please verify you have a CUDA-compatible GPU if installing Tensorflow-GPU", action="store_true")

    args = parser.parse_args()

    main(args)