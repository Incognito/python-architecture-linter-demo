Example of how to integrate an architecture definition with the
python-architecture-linter CLI in a demo project.

For the Python Architecture Linter's core repo, CLI, and the architecture definition used, please check the monorepo https://github.com/Incognito/python-architecture-linter

# Relevant information

For people who want to learn how to use this tool-chain

`cli.py`, `pyproject.toml`, and `.github/workflows/main.yml` show you everything you need to run the command:
1. How to run the tooling in a CI system
2. How to install project dependencies
3. How to create the command-line for your project.

You can ignore everything inside the `demo_project` folder, it's just so the CLI tool has something to inspect.


# Example output

It is integrated into the CI pipeline of this project so you can always see a build under the `demo-linter-usage` job on github actions.

https://github.com/Incognito/python-architecture-linter-demo/actions/workflows/main.yml

This is the original example (may be somewhat outdated, this project receives automatic updates via dependabot):

https://github.com/Incognito/python-architecture-linter-demo/runs/2984073903?check_suite_focus=true

```
Run poetry run python cli.py . --show-success=1
  poetry run python cli.py . --show-success=1
  shell: /usr/bin/bash -e {0}
  env:
    pythonLocation: /opt/hostedtoolcache/Python/3.9.5/x64
    LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.9.5/x64/lib
must_only_have_provider_in_module_root
.
No issues found

python_architecture_linter.ast_validators.nodeng_validator.validate_node_children_exclusive_allow_list
/home/runner/work/python-architecture-linter-demo/python-architecture-linter-demo/demo_project/module_runtime/provider.py:0
No issues found

python_architecture_linter.ast_validators.class_validators.class_name_suffix_validator
/home/runner/work/python-architecture-linter-demo/python-architecture-linter-demo/demo_project/module_runtime/provider.py:9
No issues found

python_architecture_linter.ast_validators.function_validators.method_name_prefix_validator
/home/runner/work/python-architecture-linter-demo/python-architecture-linter-demo/demo_project/module_runtime/provider.py:10
No issues found

...

```
