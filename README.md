# nixpkgs-review checks

This project does additional checks and adds more information about the build logs and outputs to the reports generated by [Mic92/nixpkgs-review](https://github.com/Mic92/nixpkgs-review/).

## Features

- Search through logs to find special keywords that indicate a common error like `Ran 0 tests in 0.000s` by pytest or stale substituteInPlace
- Sort build failures by failing on master and new failing via hydra-check
- Run nixpkgs-hammering, filter warnings and add them to the report
- Automatically upload logs on build failures to termbin
- Check binaries and shared objects for missing objects and left over debugging symbols
- Block the review shell from closing if there are unstaged changes in nixpkgs
- Filter empty reports and non usefull reports for certain people

## Installation

- The following programs need to be installed in your environment:
  - [cached-nix-shell](https://github.com/xzfc/cached-nix-shell)
  - curl
  - gh
  - jq
  - nix-instantiate
- Source `bashrc` in your `~/.bashrc`.

```bash
source ~/source/nixpkgs-review-checks/bashrc
```

## Usage

Just run `nixpkgs-review` normally and all features are activated automatically.

## Configuration

- `$NIXPKGS_HAMMER_ARCHIVE` URL to an archive to use for nixpkgs-hammering
- `$NIXPKGS_REVIEW_CHECKS_DEBUG` Set to not post any reports
- `$NIXPKGS_REVIEW_CHECKS_RUN` Set after execution. Unset to re-run.
