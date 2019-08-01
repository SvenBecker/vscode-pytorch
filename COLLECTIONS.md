# Snippet Collection

Full collection of supported code snippets for the PyTorch and Fastai library. `→` refers to pressing `Tab` to trigger the snippet.

## Table of Contents

1. [Pytorch Snippets](#pytorch)
    1. [PyTorch Basics](#pytorch-basics)
    2. [PyTorch Layer](#pytorch-layer)
    3. [PyTorch Functional](#pytorch-functional)
    4. [PyTorch Examples](#pytorch-example)
2. [Torchvision Snippets](#torchvision)
   1. [Torchvision Datasets](#torchvision-datasets)
   2. [Torchvision Models](#torchvision-models)

## <a name="pytorch" > </a> PyTorch Snippets

### <a name="pytorch-basics" > </a> PyTorch Basics

| Trigger               | Content                                                                       |
| --------------------- | ----------------------------------------------------------------------------- |
| `pytorch:imports→`    | insert the most common pytorch imports                                        |
| `pytorch:metric→`     | custom metric function                                                        |
| `pytorch:loss_class→` | selection of a classification loss function                                   |
| `pytorch:loss_reg→`   | selection of a regression loss function                                       |
| `pytorch:init→`       | creates an parameter initialization function and applies it to the neural net |
| `pytorch:optimizer→`  | selection of an optimizer                                                     |
| `pytorch:scheduler→`  | selection of a learning rate scheduler                                        |
| `pytorch:sequential→` | builds a sequential network                                                   |
| `pytorch:device→`     | check the available device (cpu/gpu)                                          |
| `pytorch:module→`     | creates a pytorch module class                                                |
| `pytorch:dataset`     | Template for a custom pytorch dataset                                         |
| `pytorch:function→`   | creates a pytorch function class                                              |
| `pytorch:train→`      | creates a training loop                                                       |
| `pytorch:freeze→`     | freezes all layers of the model                                               |
| `pytorch:unfreeze→`   | unfreeze all layers of the model                                              |
| `pytorch:container→`  | stores modules or parameters in some kind of container                        |
| `pytorch:checkpoint→` | load a model from local checkpoint or url                                     |
| `pytorch:github→`     | load a model from a github repo                                               |
| `pytorch:sampler→`    | select a sampler                                                              |

### <a name="pytorch-layer" > </a> PyTorch Layer

| Trigger                            | Content                            |
| ---------------------------------- | ---------------------------------- |
| `pytorch:layer:activation→`        | selection of a nonlinearity        |
| `pytorch:layer:linear→`            | selection of a linear layer        |
| `pytorch:layer:conv→`              | selection of a convolutional layer |
| `pytorch:layer:recurrent→`         | selection of a recurrent layer     |
| `pytorch:layer:norm→`              | selection of a normalization layer |
| `pytorch:layer:sparse→`            | selection of an embedding layer    |
| `pytorch:layer:pooling→`           | selection of a pooling layer       |
| `pytorch:layer:padding→`           | selection of a padding layer       |
| `pytorch:layer:dropout→`           | selection of a dropout layer       |
| `pytorch:layer:vision→`            | selection of a vision layer        |
| `pytorch:layer:distance→`          | selection of a distance layer      |
| `pytorch:layer:resnet:block→`      | creates a Resnet BasicBlock        |
| `pytorch:layer:resnet:bottleneck→` | creates a Resnet BottleneckBlock   |

### <a name="pytorch-functional" > </a> PyTorch Functional

| Trigger                 | Content                          |
| ----------------------- | -------------------------------- |
| `pytorch:F:activation→` | applies a nonlinearity function  |
| `pytorch:F:linear→`     | applies a linear function        |
| `pytorch:F:conv→`       | applies a convolutional function |
| `pytorch:F:norm→`       | applies a normalization function |
| `pytorch:F:sparse→`     | applies an embedding function    |
| `pytorch:F:pooling→`    | applies a pooling function       |
| `pytorch:F:dropout→`    | applies dropout                  |
| `pytorch:F:vision→`     | applies a vision function        |
| `pytorch:F:loss→`       | applies a loss function          |
| `pytorch:F:distance→`   | applies a distance function      |

### <a name="pytorch-example" > </a> PyTorch Code Examples

| Trigger                     | Content                                                        |
| --------------------------- | -------------------------------------------------------------- |
| `pytorch:example:imagenet→` | imagenet example                                               |
| `pytorch:example:mnist→`    | mnist example                                                  |
| `pytorch:example:vpg→`      | template for the reinforcement-learning REINFORCE algorithm    |
| `pytorch:example:ac→`       | template for the reinforcement-learning actor-critic algorithm |
| `pytorch:example:dcgan→`    | template for DCGAN                                             |
| `pytorch:example:vae→`      | template for variational autoencoder                           |

## <a name="torchvision" > </a> Torchvision Snippets

### <a name="torchvision-datasets" > </a> Torchvision Datasets

| Trigger                               | Content                                                                          |
| ------------------------------------- | -------------------------------------------------------------------------------- |
| `pytorch:torchvision:load_dataset_1→` | load specified datasets                                                          |
| `pytorch:torchvision:load_dataset_2→` | load specified datasets                                                          |
| `pytorch:torchvision:load_dataset_3→` | load specified datasets                                                          |
| `pytorch:torchvision:image_folder→`   | generic image dataloader from folder (requires root/class_x/image.png structure) |
| `pytorch:torchvision:dataset_folder→` | generic dataloader (requires root/class_x/xxx.ext structure)                     |

### <a name="torchvision-models" > </a> Torchvision Models

| Trigger                                        | Content                 |
| ---------------------------------------------- | ----------------------- |
| `pytorch:torchvision:load_model→`              | load (pretrained) model |
| `pytorch:torchvision:load_segmentation_model→` | load segmentation model |
| `pytorch:torchvision:load_detection_model→`    | load detection model    |
