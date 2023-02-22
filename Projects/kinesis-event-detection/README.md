# POC: Kinesis onlive rare event detection

## Context and business problem

Traditional processing requires to consume/download/store/process data on periodical basis. Sometimes, this periods may take
days, weeks, or even months before the actual data is consumable and usable for users in order to produce useful insights for 
the business. Unfortunately, some of the insights may conclude in action that cannot be taken because the opportunity has already
expired because several reason that may vary depending on the business context.
Nowadays new solutions have emerged to process data "on live" in order to obtain insights and take business decision as quickly 
as possible, giving companies the ability to monitor their business in "real time" and take decision based on most current records.


**ADD TEORICAL BUSINESS PROBLEM FOR ONE PARTICULAR USECASE**

## Solution

In order to process on live data some cloud tools will be used:

### AWS
AWS is a cloud-web service which provides IT services through internet, meaning that services like computation/storage/networking, among
others, will not require that you develop/pay on-premises infrastructure, instead, you can rely on AWS and its resources to deploy and manage
the resources as needed. In general, cloud services offer some advantages when compared with traditional on premises infrastructure and
solution deployemnts some of them are:

	- Availability: Amazon offers high availability for your resources, and several options in case that some of your resources have issues.

	- Scalability: You can scale up and down your resources, responding accordingly and effitiently to it's demand there is no overuse of resources.

	- Fault tolerance: Amazon can act on your behalf, with your own configuration in case that a resource fails.


#### **Kinesis**

Kinesis is one of the many services that Amazon offers to its clients, kinesis is a data-stream group of solutions to process data in real time, solving the 
issue of taking late action on your data.
Kinesis is composed by several data stream solutions, all configurable, scalable with high availabilty to respond quickly to your demands:

* **Kinesis data stream**: It is the pipeline in which data will flow from a source (data producer) to other applications (data consumers).

* **kinesis data analytics**: It is a tool which allow you to perform data wrangling on your pipeline data 'on-live' producing insights on your data.

* **kinesis firehose**: It is an storage solution for on-live data,  kinesis firehose can send your live data to all storage services whith amazon,such as S3.



#### Amazon quicksights

Amazon quicksights is a BI tool, which allows you to visually represent a set of data points, from many sources. One of the big advantages of quicksights is that
you can connect it to several data object stores contained within other amazon services, such as S3, Athena, RDS, redshift, among others.


## The proposed architechture

In order to process the on-live data and help the business to take quick decisions, the architechture below is proposed:



![alt text](https://github.com/horaciosolis1991/AWS-projects/blob/main/kinesis-event-detection/res/architechture.jpg?raw=true)




1- **Python API**: Python will act as point of contact between the data source and the kinesis data stream, it will send the records periodically to the pipeline.

2- **Kinesis data stream**: Data stream will recieve the data from the Python API and will act as a pipeline to move that information to another destiny.

3- **Kinesis data analytics**: Data Analytics solution will be in charged to prepare the data to a more consumable stage, performing data wrangling operations such
			   as filters, column additions, data cleaning, etc.

4- **Amazon cloudwatch**: Will monitor and recieve alerts from data analytics solution.

5- **Kinesis firehose**: Firehose will compile several datapoints from the analytics source and create a single file with that information.

6- **Amazon quicksights**: As a BI tool quicksight will enable the final consumer to visualize its business on a "on-live" fashion, monitoring and acting in its business
		       as fast as possible.

## Potential usecases

* Fraud detection.
* Website performance.
* Twitter analysis.
* On-live sales monitoring.
* On-live anomaly detections.



**Note**: All the material contained in this presentation is subject to change as the POC evolves to its final solution.





