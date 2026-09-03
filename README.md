# Open Interactive Learning Module extension starterkit

This is the starterkit collection of extensions for Open Interactive Learning Modules (OILM) made using JupyterBook v1 / TeachBooks at Delft University of Technology.

## Introduction

This Sphinx extension provides a single extension that includes and activates Sphinx extensions for use in JupyterBooks/TeachBooks:

* Sphinx-Thebe from TeachBooks:

  * Enabled live code in your browser
  * Manual: https://teachbooks.io/manual/features/live_code.html
* Jupyterbook patches:

  * Various patches by TeachBooks
  * Extension name: `jupyterbook_patches`
  * Repository: https://github.com/TeachBooks/JupyterBook-Patches
  * Manual: https://teachbooks.io/manual/external/JupyterBook-Patches/README.html
* Download link replacer:

  * Allows you to replace and add downloadable files to a page header
  * Extension name: `download_link_replacer`
  * Repository: https://github.com/TeachBooks/Download-Link-Replacer
  * Manual: https://teachbooks.io/manual/external/Download-Link-Replacer/README.html
* Sphinx image inverter

  * Inverts images for dark mode
  * Extension name: `sphinx_image_inverter`
  * Repository: https://github.com/TeachBooks/sphinx-image-inverter
  * Manual: https://teachbooks.io/manual/external/Sphinx-Image-Inverter/README.html
* Sphinx iframes

  * Eases the embedding of iframes
  * Extension name: `sphinx_iframes`
  * Repository: https://github.com/TeachBooks/sphinx-iframes
  * Manual: https://teachbooks.io/manual/external/sphinx-iframes/README.html
* Sphinx exercise:

  * Allows you to add exercise admonitions to your book
  * Extension name: `sphinx_exercise`
  * Repository: https://github.com/executablebooks/sphinx-exercise
  * Manual: https://ebp-sphinx-exercise.readthedocs.io/en/latest/
* Teachbooks Sphinx tippy

  * Enables hover over tips
  * Extension name: `teachbooks_sphinx_tippy`
  * Repository: https://github.com/TeachBooks/teachbooks-sphinx-tippy
  * Manual: https://teachbooks.io/manual/external/teachbooks-sphinx-tippy/README.html
  * Remark: This is a fork of https://github.com/executablebooks/sphinx-tippy specifically adapted for TeachBooks
* Sphinx named colors

  * Allows you to use custom colors in your book
  * Extension name: `sphinx_named_colors`
  * Repository: https://github.com/TeachBooks/sphinx-named-colors
  * Manual: https://teachbooks.io/manual/external/Sphinx-Named-Colors/README.html
* Sphinx dropdown toggle

  * Adds a button to toggle all dropdowns with one click
  * Extension name: `sphinx_dropdown_toggle`
  * Repository: https://github.com/TeachBooks/sphinx-dropdown-toggle
  * Manual: https://teachbooks.io/manual/_git/github.com_TeachBooks_Sphinx-Dropdown-Toggle/main/MANUAL.html
* Sphinx proof:

  * Allows you to add various common math admonitions such as theorems to your book
  * Extension name: `sphinx_proof`
  * Repository: https://github.com/executablebooks/sphinx-proof
  * Manual: https://sphinx-proof.readthedocs.io/en/latest/
* Sphinx code examples

  * Allows you to include code blocks and alternative visuals in examples
  * Extension name: `sphinx_code_examples`
  * Repository: https://github.com/TeachBooks/sphinx-code-examples
  * Manual: https://teachbooks.io/manual/_git/github.com_TeachBooks_sphinx-code-examples/main/MANUAL.html
* Sphinx accessibility

  * Allows dyslexic-friendly fonts and high contrast mode
  * Extension name: `sphinx_accessibility`
  * Repository: https://github.com/TeachBooks/sphinx-accessibility
  * Manual: https://teachbooks.io/manual/_git/github.com_TeachBooks_Sphinx-Accessibility/manual/README.html
* Sphinx toggle button

  * Allows you to add a toggle button to elements in your book
  * Repository: https://github.com/TeachBooks/sphinx-togglebutton
  * Manual: https://sphinx-togglebutton.readthedocs.io/en/latest/
  * Remark: Currently this is set to the TeachBooks fork, waiting for merge of https://github.com/executablebooks/sphinx-togglebutton/pull/66
* NoteBook Execution Patterns

  * Allows include and exclude patterns for execution of notebooks during build
  * Extension name: `sphinx_nb_execution_patterns`
  * Repository: https://github.com/TeachBooks/Sphinx-NB-Execution-Patterns
  * Manual: https://teachbooks.io/manual/_git/github.com_TeachBooks_Sphinx-NB-Execution-Patterns/Manual/README.html
* Sphinx Launch Buttons

  * Allows you to add a customizable button with links to the top right corner of your book
  * Extension name: `sphinx-launch-buttons`
  * Repository: https://github.com/TeachBooks/manual
  * Manual: https://teachbooks.io/manual/external/Sphinx-launch-buttons/README.html
* Sphinx GitHub Alerts

  * Converts GitHub alerts to Sphinx admonitions.
  * Extension name: `sphinx_github_alerts`
  * Repository: https://github.com/TeachBooks/Sphinx-GitHub-Alerts
  * Manual: https://teachbooks.io/manual/_git/github.com_TeachBooks_Sphinx-GitHub-Alerts/main/README.html
* Spinx Metadata Figure

  * Provides an interface to add metadata to figures and display the metadata.
  * Extension name: `sphinx_metadata_figure`
  * Repository: https://github.com/TeachBooks/Sphinx-Metadata-Figure
  * Manual: https://teachbooks.io/manual/_git/github.com_TeachBooks_Sphinx-Metadata-Figure/main/MANUAL.html
* Sphinx last updated by git

  * Allows a last updated note for every single page based on git history.
  * Extension name: `sphinx_last_updated_by_git`
  * Repository + documentation: https://github.com/TeachBooks/sphinx-last-updated-by-git
  * Remark: Currently this is set to the TeachBooks fork, waiting for merge of https://github.com/mgeier/sphinx-last-updated-by-git/pull/97
* Sphinx gated directives

  * Allows to used gated directives: more granular control over where the directive starts and ends and nesting directives more easily allowing nesting of code-celsl
  * Extension name: `sphinx_gated_directives`
  * Repository: https://github.com/TeachBooks/Sphinx-Gated-Directives
  * Manual: https://teachbooks.io/manual/_git/github.com_TeachBooks_Sphinx-Gated-Directives/main/MANUAL.html
* Teachbooks Zoomies

  * Allows clickable images and figures: clicking on an image opens a zoomable view.
  * Extension name: `teachbooks_zoomies`
  * Repository: https://github.com/TeachBooks/TeachBooks-Zoomies/
* Teachbooks Questions

  * Allows you to add interactive questions to your book.
  * Extension name: `teachbooks_questions`
  * Repository: https://github.com/TeachBooks/TeachBooks-Questions
  * Manual: https://teachbooks.io/manual/_git/github.com_TeachBooks_TeachBooks-Questions/main/MANUAL.html
* Sphinx-Sticky-Margin

  * Allows you to add a sticky copy figure in the margin
  * Extension name: `sphinx_sticky_margin`
  * Repository: https://github.com/TeachBooks/Sphinx-Sticky-Margin
  * Manual: https://teachbooks.io/manual/_git/github.com_TeachBooks_Sphinx-Sticky-Margin/main/MANUAL.html
* TeachBooks Fetch

  * Allows you to fetch html elements from other pages
  * Extension name: `teachbooks_fetch`
  * Repository: https://github.com/TeachBooks/TeachBooks-Fetch/
  * Manual: https://teachbooks.io/manual/_git/github.com_TeachBooks_TeachBooks-Fetch/main/MANUAL.html
* Sphinx to do

  * Allows you to add to do items
  * Extension name: `sphinx.ext.todo`
  * Repository: https://github.com/sphinx-doc/sphinx/blob/master/sphinx/ext/todo.py
  * Manual: https://www.sphinx-doc.org/en/master/usage/extensions/todo.html

## Installation

To install OILM-starterkit, follow these steps:

**Step 1: install the Package (for local use only)**

Install the `OILM-starterkit` package using `pip`:

```
pip install git+https://github.com/TUDelft-OILM/OILM-starterkit
```

**Step 2: Add to `requirements.txt` (for use with server-based pipelines)**

Make sure that the package is included in your project's `requirements.txt` to track the dependency:

```
git+https://github.com/TUDelft-OILM/OILM-starterkit
```

**Step 3: Enable in `_config.yml`**

In your `_config.yml` file, add the extension to the list of Sphinx extra extensions (**important**: underscore, not dash this time):

```
sphinx: 
    extra_extensions:
        - OILM_starterkit
```

## Usage

For using the various packages we refer to the different manuals linked above.

All extensions are loaded with their default settings.

## Configuration

By default, all extensions in OILM-starterkit are activated. You can customise which extensions are loaded by setting either `OILM_starterkit_include` **or** `OILM_starterkit_exclude` in your `_config.yml`. Setting both at the same time will raise an error.

### Exclude specific extensions

Use `OILM_starterkit_exclude` to disable one or more extensions while keeping all others. For example, to disable the tippy hover-over feature:

```yaml
sphinx:
  config:
    OILM_starterkit_exclude:
      - teachbooks_sphinx_tippy
```

### Include only specific extensions

Use `OILM_starterkit_include` to activate only the extensions you need, disabling everything else:

```yaml
sphinx:
  config:
    OILM_starterkit_include:
      - sphinx_exercise
      - sphinx_proof
      - sphinx.ext.todo
```

The extension names to use are the `Extension name` values listed for each extension in the introduction above.

Please not that TeachBook's 'Sphinx-Thebe' and the TeachBook's fork of 'Sphinx toggle button' are always included as they override packages which are already imported by JupyterBooks.

## Contribute

Do you think we missed an extension that should really be included? Let us know by either

* creating a fork of this repository and submitting a pull request, in which you added the extension to the files

  * `README.md`
  * `pyproject.toml`
  * `src\\teachbooks_favourites\\__init__.py`
* opening an issue.
* containing OILM support by email.

## Credits

This extension is based upon the orginal TeachBooks Favourites Extensions, MIT Licensed.
