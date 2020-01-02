import subprocess
from tf_easy_install import env_check_
from tf_easy_install.logging_ import Logger
logger = Logger(__name__).logger

def install(args):
    """Install the Anaconda environment.

    Returns: true if the install was successful"""
    logger.info("Beginning environment check")

    env_check = env_check_.check(args)
    if env_check:

        # Create the environment
        logger.debug(f"Installing Anaconda environment: {args.name}")
        env_installed = not subprocess.run(f"conda create -n {args.name} -y python=3.7", shell=True).returncode
        if env_installed:
            logger.debug("Anaconda environment created, installing packages")
        else:
            logger.error("Unable to install the Anaconda environment, see above for details")
            return False

        # Install the Tensorflow packages and its dependencies
        logger.debug("Installing Tensorflow{} {}".format("-GPU" if args.gpu else "", args.version))
        packages_installed = False
        if args.gpu:
            packages_installed = not subprocess.run(f"conda activate {args.name} && conda install -y tensorflow-gpu=={args.version}", shell=True).returncode
        else:
            packages_installed = not subprocess.run(f"conda activate {args.name} && conda install -y tensorflow=={args.version}", shell=True).returncode
        if packages_installed:
            logger.debug("Packages successfully installed")
        else:
            logger.error("Unable to install the packages into the Anaconda environment, see above for details")
            return False

        # Verify everything is successfully installed
        logger.debug("Running environment tests")
        packages_checked = not subprocess.run(f"conda activate {args.name} && python -c \"import tensorflow as tf; print(tf.__version__)\"", shell=True).returncode
        if not packages_checked:
            logger.error("Environment test failed, see above for details")
            return False
        return True