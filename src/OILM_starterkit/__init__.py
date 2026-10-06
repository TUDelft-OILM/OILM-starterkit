# -*- coding: utf-8 -*-
"""
OILM_starterkit
~~~~~~~~~~~~~~~

The starterkit collection of extensions for Open Interactive Learning Modules (OILM) made using JupyterBook v1 / TeachBooks at Delft University of Technology.

"""

import difflib
from typing import Any, Dict, List
from sphinx.application import Sphinx
from sphinx.errors import ConfigError
from sphinx.util import logging

logger = logging.getLogger(__name__)

ALL_EXTENSIONS: List[str] = [
    "jupyterbook_patches",
    "download_link_replacer",
    "sphinx_image_inverter",
    "sphinx_iframes",
    "sphinx_exercise",
    "teachbooks_sphinx_tippy",
    "sphinx_named_colors",
    "sphinx_dropdown_toggle",
    "sphinx_proof",
    "sphinx_code_examples",
    "sphinx_accessibility",
    "sphinx_nb_execution_patterns",
    "sphinx-launch-buttons",
    "sphinx_github_alerts",
    "sphinx_metadata_figure",
    "sphinx_last_updated_by_git",
    "sphinx_gated_directives",
    "teachbooks_zoomies",
    "teachbooks_questions",
    "sphinx_sticky_margin",
    "teachbooks_fetch",
    "sphinx.ext.todo",
    "sphinx_apa_references",
    "sphinx_tudelft_theme",
]


def setup(app: Sphinx) -> Dict[str, Any]:
    app.add_config_value("OILM_starterkit_include", [], "env")
    app.add_config_value("OILM_starterkit_exclude", [], "env")

    # app.config attributes still reflect defaults here because config.init_values()
    # has not yet run when setup() is called.  To replicate what init_values() will
    # do later we read from both _raw_config (conf.py namespace) and overrides
    # (command-line -D flags and programmatic overrides such as JupyterBook's
    # sphinx.config block from _config.yml), with overrides taking precedence.
    # Sub-extensions must also be loaded here — before init_values() — so that
    # their own add_config_value() calls are registered in time; loading them in a
    # config-inited handler causes "unknown config value" warnings for any conf.py
    # keys those extensions define.
    raw: Dict[str, Any] = getattr(app.config, "_raw_config", {})
    overrides: Dict[str, Any] = getattr(app.config, "overrides", {})
    include: List[str] = overrides.get(
        "OILM_starterkit_include",
        raw.get("OILM_starterkit_include", []),
    )
    exclude: List[str] = overrides.get(
        "OILM_starterkit_exclude",
        raw.get("OILM_starterkit_exclude", []),
    )

    if include and exclude:
        raise ConfigError(
            "OILM_starterkit: 'OILM_starterkit_include' and "
            "'OILM_starterkit_exclude' cannot both be set. "
            "Use one or the other."
        )

    unknown_include = [ext for ext in include if ext not in ALL_EXTENSIONS]
    if unknown_include:
        typos, unrecognised = [], []
        for ext in unknown_include:
            close = difflib.get_close_matches(ext, ALL_EXTENSIONS, n=1, cutoff=0.8)
            if close:
                typos.append(f"  {ext!r} → {close[0]!r}")
                include = [close[0] if e == ext else e for e in include]
            else:
                unrecognised.append(ext)
        if typos:
            logger.warning(
                "OILM_starterkit: unknown extension(s) in "
                "'OILM_starterkit_include' will be corrected as follows:\n%s",
                "\n".join(typos),
            )
        if unrecognised:
            raise ConfigError(
                f"OILM_starterkit: unknown extension(s) in "
                f"'OILM_starterkit_include': {unrecognised}. "
                f"Valid names are: {ALL_EXTENSIONS}"
            )

    unknown_exclude = [ext for ext in exclude if ext not in ALL_EXTENSIONS]
    if unknown_exclude:
        typos, unrecognised = [], []
        for ext in unknown_exclude:
            close = difflib.get_close_matches(ext, ALL_EXTENSIONS, n=1, cutoff=0.8)
            if close:
                typos.append(f"  {ext!r} → {close[0]!r}")
                exclude = [close[0] if e == ext else e for e in exclude]
            else:
                unrecognised.append(ext)
        if typos:
            logger.warning(
                "OILM_starterkit: unknown extension(s) in "
                "'OILM_starterkit_exclude' will be corrected as follows:\n%s",
                "\n".join(typos),
            )
        if unrecognised:
            raise ConfigError(
                f"OILM_starterkit: unknown extension(s) in "
                f"'OILM_starterkit_exclude': {unrecognised}. "
                f"Valid names are: {ALL_EXTENSIONS}"
            )

    if include:
        extensions_to_load = [ext for ext in ALL_EXTENSIONS if ext in include]
    elif exclude:
        extensions_to_load = [ext for ext in ALL_EXTENSIONS if ext not in exclude]
    else:
        extensions_to_load = ALL_EXTENSIONS

    for ext in extensions_to_load:
        app.setup_extension(ext)

    return {
        "version": "builtin",
        "parallel_read_safe": False,
        "parallel_write_safe": False,
    }
