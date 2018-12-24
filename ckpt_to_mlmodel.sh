PHOTO=${2:-chicago}
python export_pb.py --checkpoint ../models/ckpt/$1.ckpt --in-path ../inputs/$PHOTO.jpg --out-path ../outputs/$PHOTO_$1.jpg --device "/cpu:0" --batch-size 1
python pb_convert_mlmodel.py --pb-output $1
python mlmodel_fix_output.py --mlmodel-output $1
temp_file='../models/mlmodel/temp.mlmodel'
[ -f $temp_file ] && rm $temp_file
