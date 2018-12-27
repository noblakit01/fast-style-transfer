PHOTO=${2:-chicago}
OUTPUT="../outputs/$PHOTO"
OUTPUT+="_$1.jpg"
python3 export_tflite.py --checkpoint ../style-transfer-models/ckpt/$1.ckpt --in-path "../inputs/$PHOTO.jpg" --out-path $OUTPUT --device "/cpu:0" --batch-size 1
