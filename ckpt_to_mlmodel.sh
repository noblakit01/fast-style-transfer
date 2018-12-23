python export_pb.py --checkpoint ../models/ckpt/$1.ckpt --in-path ../inputs/ --out-path ../outputs/ --device "/cpu:0" --batch-size 1
python pb_convert_mlmodel.py --pb-output $1
python mlmodel_fix_output.py --mlmodel-output $1