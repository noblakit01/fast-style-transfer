for f in ../style-transfer-models/t7/*.t7
do
  echo "Converting $f"
  python2 convert-fast-neural-style.py -input $f -output ../style-transfer-models/mlmodel/$(basename $f .t7)_t7.mlmodel
done
