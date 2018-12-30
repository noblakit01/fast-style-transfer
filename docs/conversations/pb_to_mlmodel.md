# Convert pb to mlmodel 

## Requirements

* Python:
   * 2.7.10 (verified on MacOS 10.14.2)
* Tensorflow: 
   * 1.5.0 (verified on MacOS 10.14.2)
* tfcoreml

## Conversation

* **Step 1** convert to mlmodel
```
python pb_to_mlmodel.py --pb-output 'name of pb'
```

After this, a new mlmodel has created. But, the model outputs has the type is multi_array_type:
![1 _ezdp_iruhvoq8lffxedhq](https://user-images.githubusercontent.com/6184367/50544970-fd5dde00-0c38-11e9-991b-d473abb88e8d.png)

* **Step 2** Fix output type

```
python mlmodel_fix_output.py --mlmodel-output $1
```
$1 is the name of mlmodel output

## Source code

Convert ckpt to mlmodel source code [pb_to_mlmodel.py](../../pb_to_mlmodel.py)

Fix mlmodel output source code [mlmodel_fixoutput.py](../../mlmodel_fix_output.py)