python export_pb.py --checkpoint ../models/ckpt/la_muse.ckpt --in-path ../inputs --out-path ../outputs --device "/cpu:0" --batch-size 1
python pb_convert_mlmodel.py
python mlmodel_fix_output.py