# Installation Tensorflow-GPU on Windows

This is my notes when installing tensorflow-gpu on Windows.

## Environments

* Windows 10 (in my case)
* Python 3.5.2 (or Python 3.4, 3.5, or 3.6)
* pip 18.1 (in my case)

## Checking Windows GPU

From your command prompt you can launch Device Manager with this command:

> control /name Microsoft.DeviceManager

Then look for the Display Adapter setting, open it and read the name of your adapter. You should see something like this:

![device](https://user-images.githubusercontent.com/6184367/50573458-d228e980-0e06-11e9-88c6-5fd1e2b97d76.PNG)

As you can see, my system has a GTX 1050. Take note of yours, and visit NVidia’s site of GPUs that support CUDA [here](https://developer.nvidia.com/cuda-gpus). If your card is on the list (my GTX 1050 is), then you know that TensorFlow can support GPU operations on your machine, but before you can install and run TensorFlow, you’ll need to install the CUDA drivers for your machine and the CUDNN updates for it.

## Installing the CUDA drivers

Download and install CUDA drivers 9.0 at [cuda downloads site](https://developer.nvidia.com/cuda-toolkit).

I'm not sure the others version will work.

## Installing tensorflow

Install via pip (this will install tensorflow-gpu lastest release):
> pip install tensorflow-gpu

After installing tersorflow-gpu, we can check it by
> python

then type:
> import tensorflow as tf

In my case it show the issues:

> ImportError: DLL load failed: The specified module could not be found.

Then I uninstall current tensorflow-gpu and install tensorflow-gpu at version 1.10.0:
> pip install tensorflow-gpu==1.10.0

Then I check the tensorflow module again:
> python

> import tensorflow as tf

At this point, it show the issues:
> ImportError: Could not find 'cudnn64_7.dll'

Then, I know I need cuDNN version 7.

## Installing the CuDNN libraries

The CuDNN libraries are an update to CUDA for Deep Neural Nets, and used by TensorFlow to accelerate deep learning on NVidia GPUs. You can download them from here: https://developer.nvidia.com/cudnn.

I choose cuDNN 7.4.2.24 for CUDA 9.0

This will download a ZIP file with several folders, each containing the CuDNN files (one DLL, one header and one library). Find your CUDA installation (should be at something like: C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0)

You’ll see the directories from the ZIP file are also in this directory — i.e. there’s a bin, and include, a lib etc. Copy the files from the zip to the relevant directory. So, for example, drag cudnn64_7.dll to C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\bin, and do the same for the others.

## Final testing Tensorflow

```
import tensorflow as tf
print(tf.__version__)
```

In my case:
> 1.10.0

## References:

* [Laurence Moroney's articles](https://medium.com/@lmoroney_40129/installing-tensorflow-with-gpu-on-windows-10-3309fec55a00)
* [Tensorflow installation via pip](https://www.tensorflow.org/install/pip?lang=python3)

