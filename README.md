## Get S3 folder size 

![Python](https://img.shields.io/badge/-Python-333333?style=flat&logo=python)
![AWS Cloud](https://img.shields.io/badge/-AWS%20Cloud-333333?style=flat&logo=amazon)

Get  `s3` folder size `lambda` function

#### USAGE

Invoke the lambda with following json input

```json line
{
  "bucket": "thirumal",
  "path": "hello/"
}
```

Building the project
=================

Create Virtual environment::
   
    $ python3 -m venv venv37

Activate the vitual environment::
    
	$ . venv37/bin/activate
	
Go to project directory::

	$ cd {PATH}/eballot-poll/
	
Install Chalice::

	$ python3 -m pip install chalice

Install requirements::

    $ pip install -r requirements.txt

To Run local::

    $ chalice local
 
To Run test::
	
	$ py.test tests/
	
	$ pytest --log-cli-level=DEBUG
	 
 
To deploy it in AWS lambda::

    $ chalice deploy --connection-timeout 120
    
    
To get the AWS URL::
    
    $ chalice url
    
