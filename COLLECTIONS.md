# Snippet Collection

Full collection of supported code snippets for the PyTorch and Fastai library. `→` refers to pressing `Tab` to trigger the snippet.

## Table of Contents

1. [Pytorch Snippets](#pytorch)
    1. [PyTorch Basics](#pytroch-basics)
    2. [PyTorch Layer](#pytorch-layer)
    3. [PyTorch Functional](#pytroch-functional)
    4. [PyTorch Examples](#pytorch-example)
2. [Fastai Snippets](#fastai)
    1. [Fastai Basics](#fastai-basics)
    2. [Fastai Vision](#fastai-vision)
    3. [Fastai Text](#fastai-text)
    4. [Fastai Tabular](#fastai-tabular)
    5. [Fastai Colab](#fastai-colab)
    6. [Fastai Examples](#fastai-examples)
3. [Ignite Snippets](#ignite)
    1. [Ignite Examples](#ignite-example)

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
| `pytorch:sequential→` | builds a sequential network                                                   |
| `pytorch:device→`     | check the available device (cpu/gpu)                                          |
| `pytorch:module→`     | creates a pytorch module class                                                |
| `pytorch:function→`   | creates a pytorch function class                                              |
| `pytorch:train→`      | creates a training loop                                                       |
| `pytorch:freeze→`     | freezes all layers of the model                                               |
| `pytorch:unfreeze→`   | unfreeze all layers of the model                                              |

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

## <a name="fastai" > </a> Fastai Snippets

### <a name="fastai-basics" > </a> Fastai Basics

| Trigger                    | Content                                                                            |
| -------------------------- | ---------------------------------------------------------------------------------- |
| `fastai:train→`            | creates a two step training process                                                |
| `fastai:train_2s→`         | creates a two step model training template                                         |
| `fastai:optimizer→`        | selection of an optimizer (same as in pytorch)                                     |
| `fastai:metric→`           | creates a template for a custom metric                                             |
| `fastai:metric_reg→`       | selection of a regression metrics                                                  |
| `fastai:metric_class→`     | selection of a classification metrics                                              |
| `fastai:loss_reg→`         | selection of a regression loss function                                            |
| `fastai:loss_class→`       | selection of a classification loss function                                        |
| `fastai:metric→`           | creates a template for a custom metric                                             |
| `fastai:download-dataset→` | select a data set, load it if not already available and set a path to the data set |

### <a name="fastai-vision" > </a> Fastai Vision

| Trigger                      | Content                                          |
| ---------------------------- | ------------------------------------------------ |
| `fastai:vision:imports→`     | inserts most important imports                   |
| `fastai:vision:stats→`       | normalization type selection                     |
| `fastai:vision:transform→`   | selection of image transformations               |
| `fastai:vision:databunch→`   | creates an ImageDataBunch                        |
| `fastai:vision:datablock→`   | utilization of the DataBlock for computer vision |
| `fastai:vision:classifier→`  | creates an ImageClassifier                       |
| `fastai:vision:interpreter→` | creates an ImageClassifierInterpreter            |

### <a name="fastai-text" > </a> Fastai Text

| Trigger                       | Content                                              |
| ----------------------------- | ---------------------------------------------------- |
| `fastai:text:imports→`        | inserts most important imports                       |
| `fastai:text:dataset→`        | creates a Dataset for NLP                            |
| `fastai:text:databunch→`      | creates a DataBunch for NLP                          |
| `fastai:text:datablock→`      | utilization of the DataBlock for NLP                 |
| `fastai:text:datablock-lm→`   | utilization of the DataBlock for language model      |
| `fastai:text:datablock-clas→` | utilization of the DataBlock for language classifier |
| `fastai:text:learner→`        | creates a learner                                    |
| `fastai:text:lm-learner→`     | creates a language model learner                     |
| `fastai:text:clas-learner→`   | creates a language classifier                        |

### <a name="fastai-tabular" > </a> Fastai Tabular

| Trigger                     | Content                                    |
| --------------------------- | ------------------------------------------ |
| `fastai:tabular:imports→`   | inserts most important imports             |
| `fastai:tabular:databunch→` | creates a DataBunch for tabular data tasks |
| `fastai:tabular:datablock→` | creates a DataBlock for tabular data tasks |
| `fastai:tabular:learner→`   | creates a Learner for tabular data tasks   |

### <a name="fastai-colab" > </a> Fastai Collaborative Filtering

| Trigger                 | Content                                      |
| ----------------------- | -------------------------------------------- |
| `fastai:colab:dataset→` | creates a colaborative filtering dataset     |
| `fastai:colab:learner→` | creates a learner for colaborative filtering |

### <a name="fastai-examples" > </a> Fastai Examples

| Trigger                     | Content                                       |
| --------------------------- | --------------------------------------------- |
| `fastai:example:colab→`     | colaborative filtering example                |
| `fastai:example:mnist→`     | mnist example                                 |
| `fastai:example:imdb→`      | NLP example on imdb                           |
| `fastai:example:adult→`     | tabular learner example for the adult dataset |
| `fastai:example:dogs-cats→` | image classification example for dogs-cats    |
| `fastai:example:cifar→`     | classification example for cifar              |

## <a name="ignite" > </a> Ignite Snippets

### <a name="ignite-example" > </a> Ignite Code Examples

| Trigger                        | Content                                                        |
| ------------------------------ | -------------------------------------------------------------- |
| `ignite:example:mnist→`        | mnist example                                                  |
| `ignite:example:mnist-tbx→`    | mnist example utilizing TensorBoardX                           |
| `ignite:example:mnist-visdom→` | mnist example utilizing Visdom                                 |
| `ignite:example:vpg→`          | template for the reinforcement-learning REINFORCE algorithm    |
| `ignite:example:ac→`           | template for the reinforcement-learning actor-critic algorithm |
| `ignite:example:dcgan→`        | template for DCGAN                                             |