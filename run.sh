#! /bin/bash
set -e

if [ ! -f ./notebooks/reviews.json ]; then
    echo "Downloading reviews dataset..."
    curl https://s3-us-west-2.amazonaws.com/public-spark-workshop/reviews.json.gz >notebooks/reviews.json.gz
    gunzip notebooks/reviews.json.gz
fi

docker build -t spark_workshop ./docker
docker run -p 8889:8888 -p 4040:4040 -i --rm -v `pwd`/notebooks:/notebooks -t spark_workshop bash -c 'pyspark --driver-memory 3g'
