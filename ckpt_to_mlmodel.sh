PHOTO=${2:-chicago}
OUTPUT="../outputs/$PHOTO"
OUTPUT+="_$1.jpg"
python3 export_pb.py --checkpoint ../style-transfer-models/ckpt/$1.ckpt --in-path "../inputs/$PHOTO.jpg" --out-path $OUTPUT --device "/cpu:0" --batch-size 1
python3 pb_convert_mlmodel.py --pb-output $1
python3 mlmodel_fix_output.py --mlmodel-output $1
temp_file='../style-transfer-models/mlmodel/temp.mlmodel'
[ -f $temp_file ] && rm $temp_file
