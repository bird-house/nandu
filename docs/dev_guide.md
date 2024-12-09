# Developer Guide

## Building the docs

Run the mkdocs generator:

```console
$ make docs
```

## Running tests

Run tests using [pytest](https://docs.pytest.org/en/latest/).

```console
$ make test
$ make lint
```

## Prepare a release

Update the Conda specification file to build identical
[environments](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#building-identical-conda-environments)
on a specific OS.


**You should run this on your target OS, in our case Linux.**

``` console
$ conda env create -f environment.yml
$ source activate rook
$ make clean
$ make install
$ conda list -n nandu --explicit > spec-list.txt
```

## Bump a new version

Make a new version of nandu in the following steps:

-   Make sure everything is commited to GitHub.
-   Update `CHANGES.md` with the next version.
-   Dry Run: `bump-my-version bump --dry-run --verbose --new-version 0.8.1 patch`
-   Do it: `bump-my-version bump --new-version 0.8.1 patch`
-   \... or: `bump-my-version bump --new-version 0.9.0 minor`
-   Push it: `git push`
-   Push tag: `git push --tags`

See the [bumpversion](https://pypi.org/project/bump-my-version/)
documentation for details.
