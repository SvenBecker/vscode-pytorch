# PyTorch Code Snippets for VSCode

[![VSMarketplace](https://vsmarketplacebadge.apphb.com/version-short/SBSnippets.pytorch-snippets.svg)](https://marketplace.visualstudio.com/items?itemName=SBSnippets.pytorch-snippets)
[![Installs](https://vsmarketplacebadge.apphb.com/installs/SBSnippets.pytorch-snippets.svg)](https://marketplace.visualstudio.com/items?itemName=SBSnippets.pytorch-snippets)
[![Rating](https://vsmarketplacebadge.apphb.com/rating-short/SBSnippets.pytorch-snippets.svg)](https://marketplace.visualstudio.com/items?itemName=SBSnippets.pytorch-snippets)
[![The MIT License](https://img.shields.io/badge/license-MIT-orange.svg)](LICENSE.md)
[![GitHub](https://img.shields.io/badge/github-v0.1.0-blue.svg)](https://github.com/SvenBecker/vscode-pytorch/releases)

This project aims to provide a faster workflow when using the [PyTorch](https://github.com/pytorch/pytorch) or [fastai](https://github.com/fastai/fastai) library in [Visual Studio Code](https://code.visualstudio.com/).
This extension provides code snippets for often used coding blocks as well as code example provided by the libraries for common deep learning tasks.

## Table of Content

* [Getting Started](#usage)
* [Installation](#installation)
* [Changelog](#changelog)
* [Contributing](#contributing)
* [Contact](#contact)
* [Credits](#credits)

## <a name="usage" > </a> Getting Started

If this extension is installed and activated you might notice by start typing `pytorch` or `fastai` in your python file a dropdown
list appears. Entries starting with `pytorch:` or `fastai:` represent code snippets refering to those libraries offered by this extension.
Snippets appear in the same way as code completion by using `Ctrl+Space` (Windows, Linux) or `Cmd+Space` (MacOS). Examples on how to use
this extension are shown below.

![Preview](images/preview.gif)

## <a name="installation" > </a> Installation

The installation process is very straightforward. The most recommend way is shown below.

1. Launch Visual Studio Code
2. From the command palette `Ctrl-Shift-P` (Windows, Linux) or `Cmd-Shift-P` (MacOS)
3. Select Install Extension
4. Type `PyTorch Snippets`
5. Choose extension
6. Restart Visual Studio Code

This will give you the most recent version you can find on the [VS Marketplace](https://marketplace.visualstudio.com/vscode).
Alternativly you can also clone this repository and move it manually into your VSCode extension folder which will give you
the most recent version on GitHub.

```sh
git clone https://github.com/SvenBecker/vscode-pytorch.git
mv vscode-pytorch /path/to/your/VSCodeExtensionFolder/
```

On Windows for example you can normally find the extension folder at `C:\Users\YourName\.vscode\extensions`. On MacOs and Linux it should be
located at `~/.vscode/extensions`.

<aside class="notice">
The second method will give you the overall most recent version because I won't update the VS Marketplace version as often
as the GitHub version but the VS Marketplace version will be the more stable one.
</aside>

## <a name="changelog" > </a> Changelog

There are not any changes yet but in case of any major changes I will post the most recent ones here.
All of the past as well as the upcoming changes can further be viewed at [Changelog](CHANGELOG.md).

## <a name="contributing" > </a> Contributing

If you want to contribute, what I would highly appreciate since this project is currently in a very early stage
and there is still so much to do, please take a look at [Contributing](CONTRIBUTING.md).

## <a name="contact" > </a> Contact

Suggestions for improvements will be highly appreciated.
You can write me an email (address is provided on my [profile](https://github.com/SvenBecker)) or you can
contact me on Twitter [@SBX9209](https://twitter.com/SBX9209).

## <a name="credits" > </a> Credits

* [PyTorch](https://pytorch.org/)
* [Fastai](https://www.fast.ai/)