# Conversations models

When we train new style successful, we have *somestyle.ckpt*, then we can convert it to *.mlmodel*, *.tflite* to use in mobile project

## Convert to mlmodel

Simple run this script on terminal:

```
./ckpt_to_mlmodel.sh *name of ckpt model*
```

Work details:
* [ckpt convert to pb](./conversations/ckpt_to_pb.md) 
* [pb to mlmodels](./conversations/pb_to_mlmodel.md)

## Convert to tflite

* [ckpt convert to pb](./conversations/ckpt_to_pb.md) 
* [pb convert to tflite](./conversations/pb_to_tflite.md)
