# Contributing to vscode-pytorch

As this project is still in a very early stage I would love for you to contribute and help make it better.
For contribution, here are the guidelines I would like you to follow:

- [Issues and Bugs](#issue)
- [Feature Requests](#feature)
- [Submission Guidelines](#submit)

## <a name="issue" > </a> Found an Issue?

If you find a bug in the source code or a mistake in the documentation, you can help me by
[submitting an issue](#submit-issue) to my [GitHub Repository](https://github.com/SvenBecker/vscode-pytorch). Even better, you can
[submit a Pull Request](#submit-pr) with a fix.

## <a name="feature" > </a> Want a Feature?

You can *request* a new feature by [submitting an issue](#submit-issue) to my [GitHub Repository](https://github.com/SvenBecker/vscode-pytorch).
If you would like to *implement* a new feature, please submit an issue with
a proposal for your work first, to make sure that I can use it.

**Small Features** can be crafted and directly [submitted as a Pull Request](#submit-pr). If you would like to have a specific code snippet you can
also make a [Gist](https://help.github.com/articles/about-gists/) containing your desired code.

## <a name="submit" > </a>Submission Guidelines

### <a name="submit-issue" > </a> Submitting an Issue

Before you submit an issue, search the archive, maybe your question was already answered.

If your issue appears to be a bug, and hasn't been reported, open a new issue.
Help me to maximize the effort I can spend fixing issues and adding new features, by not
reporting duplicate issues. Providing the following information will increase the
chances of your issue being dealt with quickly:

1. **Overview of the Issue** - if an error is being thrown a non-minified stack trace helps
  - **Version** - what version is affected (e.g. 0.1.1)
    - **Motivation for your Use Case** - explain what are you trying to do and why the current behavior is a bug for you
2. **Reproduce the Error** - provide a live example [Runnable][runnable]) or a unambiguous set of steps
  - **Related Issues** - has a similar issue been reported before?
3. **Suggest a Fix** - if you can't fix the bug yourself, perhaps you can point to what might be causing the problem (line of code or commit)

You can file new issues by providing the above information [here](https://github.com/SvenBecker/vscode-pytorch/issues/new).

  ### <a name="submit-pr" > </a> Submitting a Pull Request (PR)

Before you submit your Pull Request (PR) consider the following guidelines:

1. Search [GitHub](https://github.com/SvenBecker/vscode-pytorch/pulls) for an open or closed PR
    that relates to your submission.You don't want to duplicate effort.

    - Make your changes in a new `git fork`:

2. Commit your changes using a descriptive commit message
    - Push your fork to GitHub:
3. In GitHub, send a pull request
    - If I suggest changes then:
      - Make the required updates.
      - Rebase your fork and force push to your GitHub repository (this will update your Pull Request):

      ```shell
      git rebase master -i
      git push -f
      ```

If you are not familiar with creating a Pull Request, here are some guides:

- https://help.github.com/articles/creating-a-pull-request/
- http://stackoverflow.com/questions/14680711/how-to-do-a-github-pull-request
