python3 ../../tensorflow/tensorflow/contrib/lite/python/tflite_convert.py \
--graph_def_file=../style-transfer-models/pb/$1.pb \
--output_file=../style-transfer-models/tflites/$1.tflite \
--input_array=input \
--input_shape=1,712,474,3 \
--output_array=outputs \
--input_format=TENSORFLOW_GRAPHDEF \
--output_format=TFLITE \
--inference_type=FLOAT \
--input_data_type=FLOAT