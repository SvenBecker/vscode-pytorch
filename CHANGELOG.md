# Changelog

All notable changes to the "pytorch-snippets" extension will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!---
## [Unreleased]

### Changed

## [0.1.1] - 2018-11-01

### Added

- ...

### Changed

- ...

### Fixed

- ...
- -->
## [Unreleased]

### Added

- `pytorch:torchvision:imagenet` (ImageNet cannot be downloaded, so it no longer shares the snippet with STL10 / SVHN)
- `GELU`, `SiLU` in `pytorch:layer:activation`, `gelu`, `silu` in `pytorch:F:activation`, `LazyLinear` in `pytorch:layer:linear`, `batch_first` in `pytorch:layer:attention`

### Changed

- Snippets validated against PyTorch 2.15 / torchvision 0.29: deprecated `pretrained=` replaced by `weights=`, private `_stacklevel` and removed arguments dropped, implicit `dim=None` softmax replaced by `dim=-1`
- Templates use `super().__init__()`; `pytorch:train` calls `net.train()`
- ResNet blocks follow torchvision (`downsample`, `expansion`, stride on the 3x3 conv in `Bottleneck`)
- RL examples use the `gymnasium` API, as upstream `pytorch/examples` does

### Fixed

- `pytorch:freeze` / `pytorch:unfreeze` set `require_grad` instead of `requires_grad`, so nothing was frozen (#8)
- `pytorch:init`: `if m.bias:` crashed on biases with more than one element, `nn.init.zeros` does not exist, RNN weight and bias initializers were applied to each other's tensors, the embedding branch reused tabstop `$1`
- Syntax errors in `pytorch:function`, `pytorch:layer:conv`, `pytorch:layer:padding`, `pytorch:F:pooling`
- Wrong names: `SequantialSample`, `AdaptiveLogSoftmaxWithLogits`, `out_padding`, `DataFolder`, `Flickr`, `esnext101_32x8d`
- `pytorch:scheduler` was missing the required arguments of most schedulers
- `pytorch:checkpoint` passed a path to `load_state_dict`; `pytorch:github` used removed `torch.hub.load` keywords
- Defaults that always raised: `num_classes=0` in `pytorch:F:one_hot`, `size=None, scale_factor=None` in upsampling, `padding=(2,2)` for 2d/3d padding layers
- `desription` typo hid the description of five snippets
- DCGAN example created integer labels for `BCELoss`

## [1.0.0] - 2019-07-25

### Added

- Added `pytorch:scheduler` snippets for learning rate scheduling.
- Added torchvision dataset and model snippets `pytorch:torchvision:...`.
- Added model loading from checkpoint or github repo `pytorch:checkpoint`, `pytorch:github`.
- Added sampler snippets `pytorch:sampler`

### Changed

- Snippets for Ignite and Fastai have been moved to seperate projects. Soo you can find them at github.com/svenbecker/vscode_fastai and github.com/svenbecker/vscode_ignite. This war primarily done to reduce the snippet overload.
- `pytorch:sequential` has been moved to `pytorch:container`
- Updated official `pytorch:examples`

## [0.2.3] - 2018-11-23

### Added

- Added two new snippets `pytorch:dataset` and `ignite_metrics`
  
## [0.2.2] - 2018-11-14

### Added

- Added DataBlock API support for tabular data `fastai:tabular:datablock`

### Changed

- Changed `train` snippets for pytorch and fastai

### Fixed

- Fixed bugs in optimizer selection
  
## [0.2.1] - 2018-11-11

### Added

- Added PyTorch Functional Snippets `pytorch:F:`

## [0.2.0] - 2018-11-09

### Added

- Added code snippets for fast metrics or loss selection (PyTorch and fastai)
- Added easy selection of neural network layers in PyTorch based on their type `pytorch:layer:` (conv, recurrent, etc.) 
- Added some more PyTorch snippets like for example optimizer selection, weight initialization etc.
- Added DataBlock API snippet for fastai

### Changed

- Changed some code examples for common problems to be inline with the official examples provided by PyTorch

## [0.1.1] - 2018-11-01

### Added

- Added lots of Fastai Snippets (including NLP, Computer Vision, Tabular Data and Collaborative Filtering)

## [0.1.0] - 2018-10-31

- Initial release