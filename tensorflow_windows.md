# Tensorflow Windows Installation

* If you are trying to install it on a windows machine you need to have a 64-bit version of python 3.5. This is the only way to actually install it. From the website:
> TensorFlow supports only 64-bit Python 3.5 on Windows. We have tested the pip packages with the following distributions of Python:
> 
> Python 3.5 from Anaconda
> 
> Python 3.5 from python.org.

References: [here](https://stackoverflow.com/a/41724425/3857373)

## Choose builds:

### Official Builds

| Build Type      | Status | Artifacts |
| ---             | ---    | ---       |
| **Linux CPU**   | [![Status](https://storage.googleapis.com/tensorflow-kokoro-build-badges/ubuntu-cc.svg)](https://storage.googleapis.com/tensorflow-kokoro-build-badges/ubuntu-cc.html) | [pypi](https://pypi.org/project/tf-nightly/) |
| **Linux GPU**   | [![Status](https://storage.googleapis.com/tensorflow-kokoro-build-badges/ubuntu-gpu-py3.svg)](https://storage.googleapis.com/tensorflow-kokoro-build-badges/ubuntu-gpu-py3.html) | [pypi](https://pypi.org/project/tf-nightly-gpu/) |
| **Linux XLA**   | [![Status](https://storage.googleapis.com/tensorflow-kokoro-build-badges/ubuntu-xla.svg)](https://storage.googleapis.com/tensorflow-kokoro-build-badges/ubuntu-xla.html) | TBA |
| **MacOS**       | [![Status](https://storage.googleapis.com/tensorflow-kokoro-build-badges/macos-py2-cc.svg)](https://storage.googleapis.com/tensorflow-kokoro-build-badges/macos-py2-cc.html) | [pypi](https://pypi.org/project/tf-nightly/) |
| **Windows CPU** | [![Status](https://storage.googleapis.com/tensorflow-kokoro-build-badges/windows-cpu.svg)](https://storage.googleapis.com/tensorflow-kokoro-build-badges/windows-cpu.html) | [pypi](https://pypi.org/project/tf-nightly/) |
| **Windows GPU** | [![Status](https://storage.googleapis.com/tensorflow-kokoro-build-badges/windows-gpu.svg)](https://storage.googleapis.com/tensorflow-kokoro-build-badges/windows-gpu.html) | [pypi](https://pypi.org/project/tf-nightly-gpu/) |
| **Android**     | [![Status](https://storage.googleapis.com/tensorflow-kokoro-build-badges/android.svg)](https://storage.googleapis.com/tensorflow-kokoro-build-badges/android.html) | [![Download](https://api.bintray.com/packages/google/tensorflow/tensorflow/images/download.svg)](https://bintray.com/google/tensorflow/tensorflow/_latestVersion) |
| **Raspberry Pi 0 and 1** | [![Status](https://storage.googleapis.com/tensorflow-kokoro-build-badges/rpi01-py2.svg)](https://storage.googleapis.com/tensorflow-kokoro-build-badges/rpi01-py2.html) [![Status](https://storage.googleapis.com/tensorflow-kokoro-build-badges/rpi01-py3.svg)](https://storage.googleapis.com/tensorflow-kokoro-build-badges/rpi01-py3.html) | [Py2](https://storage.googleapis.com/tensorflow-nightly/tensorflow-1.10.0-cp27-none-linux_armv6l.whl) [Py3](https://storage.googleapis.com/tensorflow-nightly/tensorflow-1.10.0-cp34-none-linux_armv6l.whl) |
| **Raspberry Pi 2 and 3** | [![Status](https://storage.googleapis.com/tensorflow-kokoro-build-badges/rpi23-py2.svg)](https://storage.googleapis.com/tensorflow-kokoro-build-badges/rpi23-py2.html) [![Status](https://storage.googleapis.com/tensorflow-kokoro-build-badges/rpi23-py3.svg)](https://storage.googleapis.com/tensorflow-kokoro-build-badges/rpi23-py3.html) | [Py2](https://storage.googleapis.com/tensorflow-nightly/tensorflow-1.10.0-cp27-none-linux_armv7l.whl) [Py3](https://storage.googleapis.com/tensorflow-nightly/tensorflow-1.10.0-cp34-none-linux_armv7l.whl) |


### Community Supported Builds

Build Type                                                                                                                                                                                      | Status                                                                                                                                                                                   | Artifacts
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------
**IBM s390x**                                                                                                                                                                                   | [![Build Status](http://ibmz-ci.osuosl.org/job/TensorFlow_IBMZ_CI/badge/icon)](http://ibmz-ci.osuosl.org/job/TensorFlow_IBMZ_CI/)                                                        | TBA
**Linux ppc64le CPU** Nightly                                                                                                                                                                   | [![Build Status](https://powerci.osuosl.org/job/TensorFlow_PPC64LE_CPU_Build/badge/icon)](https://powerci.osuosl.org/job/TensorFlow_PPC64LE_CPU_Build/)                                  | [Nightly](https://powerci.osuosl.org/job/TensorFlow_PPC64LE_CPU_Nightly_Artifact/)
**Linux ppc64le CPU** Stable Release                                                                                                                                                            | [![Build Status](https://powerci.osuosl.org/job/TensorFlow_PPC64LE_CPU_Release_Build/badge/icon)](https://powerci.osuosl.org/job/TensorFlow_PPC64LE_CPU_Release_Build/)                  | [Release](https://powerci.osuosl.org/job/TensorFlow_PPC64LE_CPU_Release_Build/)
**Linux ppc64le GPU** Nightly                                                                                                                                                                   | [![Build Status](https://powerci.osuosl.org/job/TensorFlow_PPC64LE_GPU_Build/badge/icon)](https://powerci.osuosl.org/job/TensorFlow_PPC64LE_GPU_Build/)                                  | [Nightly](https://powerci.osuosl.org/job/TensorFlow_PPC64LE_GPU_Nightly_Artifact/)
**Linux ppc64le GPU** Stable Release                                                                                                                                                            | [![Build Status](https://powerci.osuosl.org/job/TensorFlow_PPC64LE_GPU_Release_Build/badge/icon)](https://powerci.osuosl.org/job/TensorFlow_PPC64LE_GPU_Release_Build/)                  | [Release](https://powerci.osuosl.org/job/TensorFlow_PPC64LE_GPU_Release_Build/)
**Linux CPU with Intel® MKL-DNN** Nightly                                                                                                                                                       | [![Build Status](https://tensorflow-ci.intel.com/job/tensorflow-mkl-linux-cpu/badge/icon)](https://tensorflow-ci.intel.com/job/tensorflow-mkl-linux-cpu/)                                | [Nightly](https://tensorflow-ci.intel.com/job/tensorflow-mkl-build-whl-nightly/)
**Linux CPU with Intel® MKL-DNN** Python 2.7<br> **Linux CPU with Intel® MKL-DNN** Python 3.4<br> **Linux CPU with Intel® MKL-DNN** Python 3.5<br> **Linux CPU with Intel® MKL-DNN** Python 3.6 | [![Build Status](https://tensorflow-ci.intel.com/job/tensorflow-mkl-build-release-whl/badge/icon)](https://tensorflow-ci.intel.com/job/tensorflow-mkl-build-release-whl/lastStableBuild) | [1.12.0 py2.7](https://storage.googleapis.com/intel-optimized-tensorflow/tensorflow-1.12.0-cp27-cp27mu-linux_x86_64.whl)<br>[1.12.0 py3.4](https://storage.googleapis.com/intel-optimized-tensorflow/tensorflow-1.12.0-cp34-cp34m-linux_x86_64.whl)<br>[1.12.0 py3.5](https://storage.googleapis.com/intel-optimized-tensorflow/tensorflow-1.12.0-cp35-cp35m-linux_x86_64.whl)<br>[1.12.0 py3.6](https://storage.googleapis.com/intel-optimized-tensorflow/tensorflow-1.12.0-cp36-cp36m-linux_x86_64.whl)

References: [Tensorflow github](https://github.com/tensorflow/tensorflow)

## Known Issues

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


