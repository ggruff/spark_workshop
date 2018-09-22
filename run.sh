docker build -t spark_workshop ./docker
docker run -p 8888:8888 -p 4040:4040 -i --rm -v `pwd`/notebooks:/notebooks -t spark_workshop pyspark --driver-memory 3g
