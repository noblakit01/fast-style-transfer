# Tensorflow Windows Installation

## Step to step

* 1. Install python 3.5 from python.org
* 2. Install pip:
  * To install pip, securely download get-pip.py:
  > curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  * Then run the following:
  > python get-pip.py
  * References: [URL](https://pip.pypa.io/en/stable/installing/)
* 3. Install tensorflow via pip:
  * CPU-only:
  > pip install tensorflow
  * GPU package for CUDA-enabled GPU cards:
  > pip install tensorflow-gpu

*If you want tensorflow with GPU package, you have to install CUDA*
* Get the cuDNN v6.0 (maybe cuDNN v5.1) for CUDA 8.0 from [here](https://www.python.org/downloads/release/python-352/) - put it under your users folder or in another known location (you will need this in your path)
* Get CUDA 8.0 x86_64 from [here]

## Installation `fast-style-transfer` requirements: 

* Install Pillow 3.4.2, scipy 0.18.1, numpy 1.11.2
* Install moviepy:
  * Install `ez_setup`:
  > pip install ez_setup
  * Install `setup_tools`:
  > pip install --upgrade setuptools
  * Install `moviepy`:
  > pip install moviepy

## Data & source to style model

* Clone this repo: `git clone https://github.com/lengstrom/fast-style-transfer.git`
* New folder `data`
* Download training data from http://msvocds.blob.core.windows.net/coco2014/train2014.zip
* Expanding `train2014.zip` to `data` folder. Expact path: `data/train2014` is data path.
* Download http://www.vlfeat.org/matconvnet/models/beta16/imagenet-vgg-verydeep-19.mat and save at `data`
* New folder `checkpoint`, used to contain checkpoint
* Run: 
> python style.py --style style/painting_1.jpg --checkpoint-dir checkpoint

* Waiting for 12 hours -> 1 months.

## Known Issues

### https://stackoverflow.com/a/41724425/3857373

If you are trying to install it on a windows machine you need to have a 64-bit version of python 3.5. This is the only way to actually install it. From the website:
> TensorFlow supports only 64-bit Python 3.5 on Windows. We have tested the pip packages with the following distributions of Python:
> 
> Python 3.5 from Anaconda
> 
> Python 3.5 from python.org.

### No module named "_pywrap_tensorflow"

[StackOverflow's question](https://stackoverflow.com/questions/42011070/on-windows-running-import-tensorflow-generates-no-module-named-pywrap-tenso)

On Windows, TensorFlow reports either or both of the following errors after executing an `import tensorflow` statement:
* No module named `"_pywrap_tensorflow"`
* DLL load failed.

**Answers:** 

The problem was the cuDNN Library for me - for whatever reason cudnn-8.0-windows10-x64-v6.0 was NOT working - I used cudnn-8.0-windows10-x64-v5.1 - ALL GOOD!

My setup working with Win10 64 and the Nvidia GTX780M:

* Be sure you have the lib MSVCP140.DLL by checking your system/path - if not get it [here](https://www.microsoft.com/en-us/download/details.aspx?id=48145)
* Run the windows installer for python 3.5.3-amd64 from here - DO NOT try newer versions as they probably won't work
* Get the cuDNN v5.1 for CUDA 8.0 from [here](https://www.python.org/downloads/release/python-352/) - put it under your users folder or in another known location (you will need this in your path)
* Get CUDA 8.0 x86_64 from [here](https://developer.nvidia.com/cuda-downloads)
* Set PATH vars as expected to point at the cuDNN libs and python (the python path should be added during the python install)
* Make sure that ".DLL" is included in your PATHEXT variable
* If you are using tensorflow 1.3 then you want to use cudnn64_6.dll github.com/tensorflow/tensorflow/issues/7705

### Failed to load the native TensorFlow runtime.

Check tensorflow first by run the script `tensorflow_self_check.py`

Check the cuDNN DLLs direction in your `%PATH%`


