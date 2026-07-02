from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from strip_notebook import strip_notebook_before_save


c = get_config()
c.FileContentsManager.pre_save_hook = strip_notebook_before_save
c.ContentsManager.pre_save_hook = strip_notebook_before_save