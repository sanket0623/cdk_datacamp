from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    aws_s3 as s3,
    aws_lambda as lambda_,
)


class CdkDatacampStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(
            self, "CdkDatacampQueue",
            visibility_timeout=Duration.seconds(300),
        )

        topic = sns.Topic(
            self, "CdkDatacampTopic"
        )

        topic.add_subscription(subs.SqsSubscription(queue))

        bucket = s3.Bucket(
            self, 
            "MyBucket-12022026-sanket", 
            versioned=True, 
            encryption=s3.BucketEncryption.S3_MANAGED
        )

        # Define a Lambda function using Python 3.9 runtime
        lambda_function = lambda_.Function(
            self,
            "MyFunction",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="index.handler",
            code=lambda_.Code.from_asset("lambda")  # Load code from local folder named 'lambda'
        )
