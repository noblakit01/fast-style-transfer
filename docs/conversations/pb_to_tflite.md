# Pb convert to tflite

Use the TFLite converter of Tensorflowlite. You can find a tutorial [here](https://codelabs.developers.google.com/codelabs/tensorflow-for-poets-2-tflite/#2).

TFLite converter is installed from tensorflow version >= 1.9.0
Check TFLite converter:
> tflite_convert --help

Uncomfortably, at this lastest version v.1.12.0 rc2, it didn't support `SquaredDifference` operator
So clone my fork [tensorflow repo](https://github.com/noblakit01/tensorflow) and checkout branch `tflite_for_v_1_12`.

In this branch, I implement `SquaredDifference` operator and use `tflite_convert.py` instead.
Look at `pb_to_tflite.sh` for more details.
