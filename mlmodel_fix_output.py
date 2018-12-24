from __future__ import print_function
import sys
sys.path.insert(0, 'src')
import coremltools
from argparse import ArgumentParser
from utils import exists

def convert_multiarray_output_to_image(spec, feature_name, is_bgr=False):  
    """  
    Convert an output multiarray to be represented as an image  
    This will modify the Model_pb spec passed in.  
    Example:  
        model = coremltools.models.MLModel('MyNeuralNetwork.mlmodel')  
        spec = model.get_spec()  
        convert_multiarray_output_to_image(spec,'imageOutput',is_bgr=False)  
        newModel = coremltools.models.MLModel(spec)  
        newModel.save('MyNeuralNetworkWithImageOutput.mlmodel')  
    Parameters  
    ----------  
    spec: Model_pb  
        The specification containing the output feature to convert  
    feature_name: str  
        The name of the multiarray output feature you want to convert  
    is_bgr: boolean  
        If multiarray has 3 channels, set to True for RGB pixel order or false for BGR  
    """  
    for output in spec.description.output:  
        if output.name != feature_name:  
            continue  
        if output.type.WhichOneof('Type') != 'multiArrayType':  
            raise ValueError("%s is not a multiarray type" % output.name)  
        array_shape = tuple(output.type.multiArrayType.shape)  
        channels, height, width = array_shape  
        from coremltools.proto import FeatureTypes_pb2 as ft  
        if channels == 1:  
            output.type.imageType.colorSpace = ft.ImageFeatureType.ColorSpace.Value('GRAYSCALE')  
        elif channels == 3:  
            if is_bgr:  
                output.type.imageType.colorSpace = ft.ImageFeatureType.ColorSpace.Value('BGR')  
            else:  
                output.type.imageType.colorSpace = ft.ImageFeatureType.ColorSpace.Value('RGB')  
        else:  
            raise ValueError("Channel Value %d not supported for image inputs" % channels)  
        output.type.imageType.width = width  
        output.type.imageType.height = height  

def build_parser():
    parser = ArgumentParser()
    parser.add_argument('--mlmodel-output', type=str,
                        dest='mlmodel_output',
                        help='mlmodel output name',
                        metavar='MLMODEL_OUTPUT', required=True)

    return parser

##def check_opts(opts):

def main():
    parser = build_parser()
    opts = parser.parse_args()
    #check_opts(opts)

    model = coremltools.models.MLModel('../style-transfer-models/mlmodel/temp.mlmodel')
    spec = model.get_spec()
    convert_multiarray_output_to_image(spec,'add_37__0',is_bgr=False)
    newModel = coremltools.models.MLModel(spec)
    newModel.save('../style-transfer-models/mlmodel/' + opts.mlmodel_output + '.mlmodel')

if __name__ == '__main__':
    main()
