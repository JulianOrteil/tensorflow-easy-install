import os
import platform
import subprocess
from tf_easy_install.logging_ import Logger
logger = Logger(__name__).logger

def check(args):
    """Verifies the environment based on the triggers passed from the command line.

    Returns: true if the environment passed the check
    """
    _sys = f"{platform.system()} {platform.release()}"
    _conda = not subprocess.run("conda", shell=True, stdout=subprocess.PIPE).returncode

    logger.info(f"Detected OS: {_sys}")
    if not "Windows 10" in _sys:
        logger.warning(f"Recommended OS is Windows 10, you have: {_sys}")
    elif not "Windows" in _sys:
        if "Mac" in _sys:
            logger.error("MacOS is not supported by this project")
            return False
        else:
            logger.error("This distribution is for Windows, please install the Linux distribution: pip install tf-easy-install-linux")
            return False

    if args.anaconda:
        logger.debug("Checking Anaconda installation")
        if not _conda:
            logger.error("Anaconda is not installed or not in path. You can download it from here: https://www.anaconda.com/distribution/#download-section")
            return False
        logger.info("Successfully detected Anaconda")

        # Check to see if the requested conda env name is already in use
        if not subprocess.run(f"conda activate {args.env_name}", shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL).returncode:
            logger.error(f"The '{args.env_name}' Anaconda environment already exists, please choose a different name or run 'conda remove -y -n {args.env_name} --all'")
            return False

    if args.gpu:
        if not args.yes:
            logger.info("Before installing, a CUDA-compatible GPU with a compute score of at least 3.5 must be present to use Tensorflow-GPU: https://www.tensorflow.org/install/gpu#hardware_requirements")
            logger.info("To verify your hardware, please look here: https://developer.nvidia.com/cuda-gpus")
            logger.warning("A virtual machine running Windows cannot be used with Tensorflow-GPU, it does not have direct access to the graphics card")
            cuda_compatible = input("Does your computer support a CUDA-compatible GPU? (y/[n]) : ").lower() == 'y'
            if not cuda_compatible:
                logger.error("User indicated no CUDA-compatible GPU was found")
                return False

    if not args.yes:
        update_conda = input("Would you like to check for updates to the Anaconda environment (they will be auto-installed)? (y/[n]) : ").lower() == 'y'
        if update_conda:
            logger.debug("Checking for Anaconda updates")
            conda_updated = not subprocess.run("conda update -y -n base -c defaults conda")
            if conda_updated:
                logger.info("Anaconda successfully updated")
            else:
                logger.warning("Failed to update Anaconda, see above for details")
    else:
        logger.debug("Checking for Anaconda updates")
        conda_updated = not subprocess.run("conda update -y -n base -c defaults conda", shell=True).returncode
        if conda_updated:
            logger.info("Anaconda successfully updated")
        else:
            logger.warning("Failed to update Anaconda, see above for details")

    logger.info("Successfully completed the environment check")
    return True