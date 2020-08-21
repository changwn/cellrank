# -*- coding: utf-8 -*-
"""Module for documentation helper function."""

from textwrap import dedent

from docrep import DocstringProcessor

_adata = """\
adata : :class:`~anndata.AnnData`
    Annotated data object."""
_plotting = """\
figsize
    Size of the figure.
dpi
    Dots per inch.
save
    Filename where to save the plot."""
_parallel = """\
show_progress_bar
    Whether to show a progress bar. Disabling it may improve performance.
n_jobs
    Number of parallel jobs. If `-1`, use all available cores. If `None` or `1`, the execution is sequential.
backend
    Which backend to use for parallelization. See :class:`joblib.Parallel` for valid options."""
_model = """\
model
    Model based on :class:`cellrank.ul.models.BaseModel` to fit.

    If a :class:`dict`, gene and lineage specific models can be specified. Use `'*'` to indicate
    all genes or lineages, for example `{'Map2': {'*': ...}, 'Dcx': {'Alpha': ..., '*': ...}}`."""
_just_plots = """\
None
    Nothing, just plots the figure. Optionally saves it based on :paramref:`save`."""
_backward = """\
backward
    Direction of the process."""
_eigen = """\
which
    Eigenvalues are in general complex. `'LR'` - largest real part, `'LM'` - largest magnitude.
alpha
    Used to compute the `eigengap`. :paramref:`alpha` is the weight given
    to the deviation of an eigenvalue from one."""
_n_cells = """\
n_cells
    Number of most likely cells from each main to select."""
_fit = """\
n_lineages
    Number of lineages. If `None`, it will be determined automatically.
cluster_key
    Match computed states against pre-computed clusters to annotate the states.
    For this, provide a key from :paramref:`adata` `.obs` where cluster labels have been computed.
keys
    Determines which %(root_or_final) states to use by passing their names.
    Further, %(root_or_final)s states can be combined. If e.g. the %(final)s states are
    ['Neuronal_1', 'Neuronal_1', 'Astrocytes', 'OPC'], then passing keys=['Neuronal_1, Neuronal_2', 'OPC']
    means that the two neuronal %(final)s states are treated as one and the 'Astrocyte' state is excluded.
"""
_density_correction = (
    "Optionally, we apply a density correction as described in [Coifman05]_, "
    "where we use the implementation of [Haghverdi16]_."
)
_time_range = """\
time_range
    - If a :class:`tuple`, it specifies the minimum and maximum pseudotime.
      Both values can be `None`, in which case the minimum is the earliest pseudotime
      and the maximum is automatically determined.
    - If a :class:`float`, it specifies the maximum pseudotime.
"""
_time_ranges = f"{_time_range}\n    This can also be specified on per-lineage basis."
_velocity_mode = """\
mode
    How to compute transition probabilities. Valid options are:

        - `{m.DETERMINISTIC.s!r}` - deterministic computation that doesn't propagate uncertainty
        - `{m.MONTE_CARLO.s!r}` - Monte Carlo average of randomly sampled velocity vectors
        - `{m.STOCHASTIC.s!r}` - second order approximation, only available when :mod:`jax` is installed
        - `{m.SAMPLING.s!r}` - sample 1 transition matrix from velocity distribution
        - `{m.PROPAGATION.s!r}` - same as `{m.MONTE_CARLO.s!r}`, but does not average the vectors.
          Instead, it saves the sampled transition matrices to :paramref:`_t_mats` to be used
          for later uncertainty estimation. It is generally faster then `{m.MONTE_CARLO.s!r}`,
          but also less memory efficient
"""
_velocity_backward_mode = """\
backward_mode
    Only matters if initialized as :paramref:`backward` `=True`.  Valid options are:

        - `{b.TRANSPOSE.s!r}` - compute transitions from neighboring cells `j` to cell `i`
        - `{b.NEGATE.s!r}` - negate the velocity vector
"""
_copy = """Return a copy of self."""
_root = "root"
_final = "final"
_model_callback = """\
callback
    Function which takes a :class:`cellrank.ul.models.BaseModel` and some keyword arguments
    for :meth:`cellrank.ul.models.BaseModel.prepare` and returns the prepared model.
    Can be specified in gene- and lineage-specific manner, similarly to :paramref:`model`.
"""


def inject_docs(**kwargs):
    r"""Docstrings should start with "\" in the first line for proper formatting."""

    def decorator(obj):
        obj.__doc__ = dedent(obj.__doc__).format(**kwargs)
        return obj

    return decorator


d = DocstringProcessor(
    plotting=_plotting,
    parallel=_parallel,
    model=_model,
    adata=_adata,
    just_plots=_just_plots,
    backward=_backward,
    root=_root,
    final=_final,
    eigen=_eigen,
    root_or_final=f"{_root} or {_final}",
    n_cells=_n_cells,
    fit=_fit,
    copy=_copy,
    density_correction=_density_correction,
    time_range=_time_range,
    time_ranges=_time_ranges,
    velocity_mode=_velocity_mode,
    velocity_backward_mode=_velocity_backward_mode,
    model_callback=_model_callback,
)