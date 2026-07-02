import nbformat
from nbstripout._utils import strip_output


def strip_notebook_before_save(model, path, contents_manager, **kwargs):
    if model.get("type") != "notebook" or "content" not in model:
        return

    notebook = nbformat.from_dict(model["content"])
    stripped = strip_output(
        notebook,
        keep_output=False,
        keep_count=False,
        keep_id=True,
        extra_keys=["metadata.kernelspec", "metadata.language_info"],
    )

    model["content"] = stripped