# Snippet Collection

Full collection of supported code snippets for the PyTorch and Fastai library.

## Table of Contents

1. [Pytorch Snippets](#pytorch)
    1. [PyTorch Basics](#pytroch-basics)
    2. [PyTorch Layer](#pytorch-layer)
    3. [PyTorch Examples](#pytorch-example)
2. [Fastai Snippets](#fastai)
    1. [Fastai Basics](#fastai-basics)
    2. [Fastai Vision](#fastai-vision)
    3. [Fastai Text](#fastai-text)
    4. [Fastai Tabular](#fastai-tabular)
    5. [Fastai Colababorative Filtering](#fastai-colab)

## <a name="pytorch" > </a> PyTorch Snippets

### <a name="pytorch-basics" > </a> Pytorch Basics

| Trigger            | Content                                |
| ------------------ | -------------------------------------- |
| `pytorch:imports`  | insert the most common pytroch imports |
| `pytorch:device`   | check the available device (cpu/gpu)   |
| `pytorch:module`   | creates a pytorch module class         |
| `pytorch:function` | creates a pytorch function class       |
| `pytorch:train`    | creates a training loop                |
| `pytorch:freeze`   | freezes all layers of the model        |
| `pytorch:unfreeze` | unfreeze all layers of the model       |

### <a name="pytorch-layer" > </a> Pytorch Layer

| Trigger              | Content                           |
| -------------------- | --------------------------------- |
| `pytorch:resblock`   | creates a basic Resnet Block      |
| `pytorch:bottleneck` | creates a Resnet Bottleneck block |

### <a name="pytorch-example" > </a> PyTorch Code Examples

| Trigger                   | Content                                  |
| ------------------------- | ---------------------------------------- |
| `pytorch:example:mnist`   | creates an image classifier for mnist    |
| `pytorch:example:cifar10` | creates an image classifier for cifar 10 |

## <a name="fastai" > </a> Fastai Snippets

## <a name="fastai-basics" > </a> Fastai Basics

| Trigger         | Content                                |
| --------------- | -------------------------------------- |
| `fastai:train`  | creates a two step training process    |
| `fastai:metric` | creates a template for a custom metric |

## <a name="fastai-vision" > </a> Fastai Vision

| Trigger                        | Content                                                  |
| ------------------------------ | -------------------------------------------------------- |
| `fastai:vision:imports`        | inserts most important imports                           |
| `fastai:vision:databunch`      | creates an ImageDataBunch                                |
| `fastai:vision:classifier`     | creates an ImageClassifier                               |
| `fastai:vision:interpreter`    | creates an ImageClassifierInterpreter                    |
| `fastai:vision:classification` | creates a template for common image classification tasks |

## <a name="fastai-text" > </a> Fastai Text

| Trigger                 | Content                        |
| ----------------------- | ------------------------------ |
| `fastai:text:imports`   | inserts most important imports |
| `fastai:text:dataset`   | creates a Dataset for NLP      |
| `fastai:text:databunch` | creates a DataBunch for NLP    |
| `fastai:text:learner`   | creates a Learner              |

## <a name="fastai-tabular" > </a> Fastai Tabular

| Trigger                    | Content                                    |
| -------------------------- | ------------------------------------------ |
| `fastai:tabular:imports`   | inserts most important imports             |
| `fastai:tabular:databunch` | creates a DataBunch for tabular data tasks |
| `fastai:tabular:learner`   | creates a Learner for tabular data tasks   |

## <a name="fastai-colab" > </a> Fastai Collaborative Filtering

| Trigger                | Content                               |
| ---------------------- | ------------------------------------- |
| `fastai:colab:dataset` | creates a colab filtering dataset     |
| `fastai:colab:learner` | creates a learner for colab filtering |