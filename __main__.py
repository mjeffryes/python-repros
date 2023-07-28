"""A Python Pulumi program"""

import pulumi
import pulumi_aws_native as aws_native

aws_native.dynamodb.Table(
       "abc",
       table_name="example",
       billing_mode="PROVISIONED",
       opts=pulumi.ResourceOptions(protect=True),
       attribute_definitions=[
           aws_native.dynamodb.TableAttributeDefinitionArgs(
               attribute_name="PrimaryKey",
               attribute_type="S",
            )
        ],
        provisioned_throughput=aws_native.dynamodb.TableProvisionedThroughputArgs(
            read_capacity_units=100,  
            write_capacity_units=1,
        ),
        key_schema=[
            aws_native.dynamodb.TableKeySchemaArgs(
                attribute_name="PrimaryKey",
                key_type="HASH",
             ),
        ],
)
