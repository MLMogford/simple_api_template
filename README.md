
python opackage in S3 - requires SSL - TODO later

ENDPOINT for model package bucket AWS
http://mypackages-8251455948654958439478.s3-website-ap-southeast-2.amazonaws.com

pip install diabetes_regression_model --extra-index-url=http://mypackages-8251455948654958439478.s3-website-ap-southeast-2.amazonaws.com --trusted-host=mypackages-8251455948654958439478.s3-website-ap-southeast-2.amazonaws.com

pip install <package_name>==<version> --extra-index-url=<s3 Endpoint> --trusted-host=<s3 Endpoint without http>


Upgrading packages using pip install diabetes_regression_model --upgrade will also work with this approach.



With GemFury

docker build --build-arg PIP_EXTRA_INDEX_URL=https://hnJd94AxkLYRC2xvSMgS:@pypi.fury.io/mmogford -t diabetes-api:latest .

docker run -p 8001:8001 -e PORT=8001 diabetes-api
