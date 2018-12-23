import tfcoreml as tf_converter
tf_converter.convert(tf_model_path = '../models/pb/la_muse.pb',
                     mlmodel_path = '../models/mlmodel/temp.mlmodel',
                     output_feature_names = ['add_37:0'],
                     ## Note found this after running a conversion the first time
                     image_input_names = ['img_placeholder__0']) 