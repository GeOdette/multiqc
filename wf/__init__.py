"""
create a single report with interactive plots for multiple bioinformatics analyses across many samples
"""

import subprocess
from pathlib import Path

from latch import small_task, workflow
from latch.types import LatchFile, LatchDir
import os


@small_task
def multqc_task(input_folder: LatchDir, out_dir: LatchDir) -> LatchDir:

    local_dir = "/root/multiqc_output/"
    local_prefix = os.path.join(local_dir, "qc_reports")

    # changing to directory with files
   # os.chdir(input_folder.local_path)  # input_folder.remote_path does not work
    # input_folder.local_path raises no erro

    # defining the function
    multqc_cmd = [
        "multiqc",
        input_folder.local_path,
        "-o",
        str(local_prefix),

    ]

    subprocess.run(multqc_cmd, check=True)
    return LatchDir(str(local_dir), out_dir.remote_path)


@workflow
def multiqc(input_folder: LatchDir, out_dir: LatchDir) -> LatchDir:
    """create a single report with interactive plots for multiple bioinformatics analyses across many samples

    MULTIQC
    ----
    Multiqc workflow implemeents the multiqc tool for creating a single report with interactive plots for multiple bioinformatics analyses across many samples.<br>
    Using the workflow saves on time, installation issues, and provides flexibility in managing your data<br>

    Currently, the tool generates a single report of all files in the input directory provided.<br>
    The workflow does not allow one to ignore files in the single directory. Users are therefore encouraged to carefull curate their folder<br>
    before run.<br>
    However, we are working to ensure such is available in the future

    > Note: All results are deposited in the folder multiqc_data while the report in the<br>
    output directory you selected

    Example output:<br>
    > ![](https://multiqc.info/docs/images/toolbox_highlight.png) 



    __metadata__:
        display_name: Generate analysis reports with multiqc

        author:
            name: GeOdette

            email: steveodettegeorge@gmail.com

            github:
        repository: https://github.com/GeOdette/multiqc.git

        license:
            id: MIT

    Args:

        input_folder:
          Folder containing files with bioinformatics analyses

          __metadata__:
            display_name: Input Directory

        out_dir:
          Preffered output dir

          __metadata__:
            display_name: Output Directory
    """
    return multqc_task(input_folder=input_folder, out_dir=out_dir)
