"""
create a single report with interactive plots for multiple bioinformatics analyses across many samples
"""

import subprocess
from pathlib import Path

from latch import small_task, workflow
from latch.types import LatchFile, LatchDir
import os


@small_task
def multqc_task(input_folder: LatchDir, out_dir: LatchDir)-> LatchDir:
    # defining the function

    local_dir = "/root/multiqc_output/"
    local_prefix = os.path.join(local_dir, "qc_reports")

    os.chdir(str(input_folder))
    multqc_cmd=[
        "multiqc .",
        "-outdir",
        str(local_prefix),

    ]

    subprocess.run(multqc_cmd, check=True)
    return LatchDir(str(local_dir), out_dir.remote_path)



@workflow
def assemble_and_sort(input_folder: LatchDir, out_dir: LatchDir) -> LatchDir:
    """create a single report with interactive plots for multiple bioinformatics analyses across many samples

    MULTIQC
    ----


    __metadata__:
        display_name: Generate analysis reports with multiqc

        author:
            name: SGodette

            email: steveodettegeorge@gmail.com

            github:
        repository:
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
