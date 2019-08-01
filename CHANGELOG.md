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