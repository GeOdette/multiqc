FROM 812206152185.dkr.ecr.us-west-2.amazonaws.com/latch-base:9a7d-main

RUN apt-get install -y curl unzip

#
# RUN apt-get update -y &&\
# apt-get install -y autoconf samtools

# install conda

#Install conda
RUN curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh --output miniconda.sh
ENV CONDA_DIR /opt/conda
RUN bash miniconda.sh -b -p /opt/conda
ENV PATH=$CONDA_DIR/bin:$PATH

# install multiqc
RUN pip install multiqc
# RUN conda install -c bioconda multiqc

# STOP HERE:
# The following lines are needed to ensure your build environement works
# correctly with latch.
COPY wf /root/wf
ARG tag
ENV FLYTE_INTERNAL_IMAGE $tag
RUN python3 -m pip install --upgrade latch
RUN pip install --upgrade requests==2.20.1
WORKDIR /root
