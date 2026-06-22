## v1.0.1 (2026-06-22)

### Bug Fixes

- **composekit**: drop obsolete test-skip token from auto-commits

### Documentation

- **readme**: install from git url

## v1.0.0 (2026-06-22)

### Features

- **composekit**: make it a standalone tool
- **generate**: add formatting modes for folder capitalization
- **generate**: add support for docker bind mount
- **update**: add support for per container limit
- **update**: add ability to customize default registry
- **composekit**: add __setitem__ to config classes
- **composekit**: add sort script
- **generate**: add entry duplication for ports
- **generate**: add support for group_add option
- **composekit**: add ruff to replace black
- add uv to replace poetry and tox
- **pyproject**: add mypy configuration
- **pyproject**: add poetry configuration
- **pyproject**: add tox configuration
- **generate**: add commit generation
- **generate**: add support for tmpfs option
- **generate**: add support for shm_size
- **update**: add support for private ghcr repositories
- **git**: ignore .env file
- **update**: add support for ghcr registry
- **update**: add surpport for version_regex
- **generate**: add support for working_dir
- **generate**: add capitalize_folder_name config
- **update**: support multiple containers in a file
- **generate**: support multiple containers in a file
- **update**: add support for official images
- **update**: add logging
- update compose files
- **generate**: add support for config file
- **update**: add an image updater script
- **script**: add support for network_mode
- **script**: add support for most of the docker compose options
- **script**: add support for .yml file extension
- **script**: add support for devices
- update compose files
- **script**: add networks to the services file
- **script**: add support for custom restart policy
- **script**: add support for custom network driver
- **script**: add support for labels
- **script**: add support for healthcheck
- **script**: recreate composes' folder every time
- support entrypoint
- update compose files
- add support for custom folder name
- add support for custom service name
- update compose files
- support environment variables
- support full directory binding
- add support for custom folder name
- add automatic binding path generation for container volumes
- **generate**: add command-line argument support
- initial release

### Bug Fixes

- **composekit**: resolve pyrefly type errors
- **utils**: raise clean error when containers folder missing
- **generate**: load templates via importlib.resources
- **generate**: don't force write the networks option
- **update**: treat user library as none
- **oci-api**: don't add https:// prefix if host already has scheme
- **update**: follow redirects in requests
- **update**: don't convert version_regex to string
- **update**: correctly update image tag in container
- **generate**: don't commit with zero changes
- **update**: update log level for invalid image warning
- **update**: ensure lowercase keys for default values
- **update**: check for existent of config files
- **generate**: handle custom names which includes mount options
- handle --use-full-directory variable

### Code Refactoring

- **composekit**: apply ruff fixes
- **config**: accept multiple paths in load()
- **config**: set default values for config_paths and default_values
- **utils**: extract git and file helpers
- **utils**: export config and list_tags from package
- **generate**: add support for privileged option
- **generate**: fix typings
- **utils**: use a unified config class
- **generate**: move folder name logic to a dedicated function
- **generate**: tidy up handle_volumes parameter
- **generate**: add folder, name and image to options
- **composekit**: convert update.main from asynchronous to synchronous
- **update**: comply with ruff rules
- **generate**: comply with ruff rules
- **composekit**: update commit types
- **composekit**: move templates under package
- **composekit**: drop type checking
- **composekit**: improve handling of missing required packages
- **tests**: prepare for mypy strict
- **update**: prepare for mypy strict
- **generate**: prepare for mypy strict
- **utils**: prepare for mypy strict
- **generate**: make mypy happy
- **pyproject**: add black configuration
- **composekit**: restructure project
- **update**: update log messages
- **update**: utilize oci api
- **generate**: tidy up
- **update.yaml**: set page_size to 40
- **update**: move volume handling into a dedicated
- **update**: move version fetching into a dedicated function
- **update**: set httpx timeout from config
- **update**: tidy up
- **update**: move image parsing to dedicated function
- **generate**: update commit message
- **update**: make pyright happy
- **generate**: make pyright happy
- **git**: ignore __pycache__
- **update**: use git library native methods
- **update**: use asyncio
- **generate**: tidy up
- **git**: ignore all .env files
- **generate**: tidy up
- **update**: add 'latest' tag for images missing tags
- **update**: don't enforce a registry
- **update**: switch from requests to httpx
- **generate**: improve required package handler
- **update**: improve required package handler
- **update**: add support reading from update.private.yaml
- **generate**: better support for mount options
- **generate.yaml**: add a missing variable
- **update**: use container file stem as scope for commit message
- **generate,update**: move config to a class
- **generate,update**: enhance configuration reading
- **generate**: drop support for arguments
- **script**: move the logic codes to a function
- move templates from the script to files
- **script**: add types
- update the containers' config based on recent changes

### Maintenance

- **pre-commit**: add ruff, pyrefly, pytest, and commitizen hooks
- **pyproject**: add pyrefly to replace mypy
- **ruff**: update configurations
- **uv**: add socks support to httpx
- **uv**: update packages
- **commitizen**: update questions' text
- **pyproject**: add command-line entrypoint scripts
- **commitizen**: update configurations
- remove requirements.txt
- **composekit**: skip tests for generated commits
- **ruff**: enable common lint rules
- **pyproject**: define paths for ruff
- **pyproject**: set up commitizen

### Styling

- **tests**: reformat to satisfy ruff
- **generate,update**: reformat code via black

### Tests

- convert tests to unittest assertions
- **generate**: set bind_path for handle_volumes tests
- **update**: drop test_config_default
- **update**: fix two tests
- **generate**: fix tests
- **update**: update tests
- **generate**: update tests
- **update**: refactor and add test for find_versions
- **generate**: refactor and add test for handle_devices
- add tests for generate
- add tests for update

### Documentation

- **readme**: update year
- **readme**: use the new command-line entrypoint scripts
- update readme
- update readme
- update readme

### Build System

- **pyproject**: declare setuptools build-system
- **deps**: add types-pyyaml to dev dependencies

### Continuous Integration

- **python-tests**: broaden test trigger paths
- **python-tests**: replace mypy with pyrefly
- **github**: drop update-composes and update-images
- **github**: only run update-composes on containers changes
- **github**: only run python tests on src changes
- **github**: split linting into separate job and fix skip logic
- **github**: update uv sync command
- **github**: remove an extra flag for uv sync
- **github**: add name to jobs
- **github**: allow skipping tests
- **github**: add python version matrix to tests
- **github**: scope uv cache by python version
- **github**: add ruff lint check
- **github**: enable uv caching
- **github**: install the specified python version in pyproject
- **github**: update run conditions
- **github**: add python tests
- **github**: fix workflow execution
- **github**: adapt to generate.py changes
- **github**: add run-name to workflows
- **github**: update commit message
- **github**: move python packages to requirements.txt
- **github**: add workflow dispatch to update composes
- **github**: add update images
- **github**: rename update to update-composes
- **github**: fix git push
