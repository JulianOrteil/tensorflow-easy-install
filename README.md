# Tensorflow Easy Install (tf_easy_install)

Python module for stupidly easy Tensorflow installation.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install tf_easy_install.

```bash
pip install tensorflow-easy-install
```

## Usage

(From the command line)
```
python -m tf_easy_install [options]
```

Tensorflow Easy Installer is designed to make installing Tensorflow as easy as possible.
Below are the available options in the current release:
```
optional arguments:
  -h, --help            show this help message and exit
  -a, --anaconda        install Tensorflow into a conda environment
  -g, --gpu             install Tensorflow-GPU
  --tf-version TF_VERSION
                        install a specific version of Tensorflow
  --env-name ENV_NAME   the name of the anaconda environment
  -y, --yes             skip any confirmations. Warning: please verify you
                        have a CUDA-compatible GPU if installing Tensorflow-
                        GPU
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)