FROM continuumio/anaconda3:5.2.0
RUN conda install -y pyspark seaborn==0.9.0
RUN pip install rise
RUN jupyter-nbextension install rise --py --sys-prefix
RUN jupyter nbextension enable rise --py --sys-prefix
RUN apt-get -y update
RUN apt-get install --fix-missing -y openjdk-8-jdk jq

ENV PYSPARK_DRIVER_PYTHON=jupyter
ENV PYSPARK_DRIVER_PYTHON_OPTS='notebook --port 8888 --ip=0.0.0.0 --allow-root --config /notebooks/.config.py --no-browser --notebook-dir=/notebooks'
EXPOSE 8888
EXPOSE 4040

ENV SPARK_HOME="/opt/conda/lib/python3.6/site-packages/pyspark"