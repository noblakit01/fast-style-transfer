python ../../tensorflow-noblakit01/tensorflow/contrib/lite/python/tflite_convert.py \
--graph_def_file=../style-transfer-models/pb/$1.pb \
--output_file=../style-transfer-models/tflites/$1.tflite \
--input_format=TENSORFLOW_GRAPHDEF \
--output_format=TFLITE \
--input_shape=1,474,712,3 \
--input_array=img_placeholder \
--output_array=add_37 \
--inference_type=FLOAT \
--input_data_type=FLOAT --allow_custom_ops