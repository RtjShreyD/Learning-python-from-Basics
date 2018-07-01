# Learning python from Basics

The Following are 3 demo codes in Python specially for Linux for inputting a json file, loading its contents and editing the contents.
Then we are also creating a Web API using Python.
Before starting with the actual learning of Python these codes help beginners to see how powerful Python as a language is.

Here we start:
1. Download a sample.json file from the net
2. Open LX terminal
	enter command--   cat sample.json     ####to list the contents of file on terminal window
3. Create a new file as input.py or just copy paste the contents of input.py here making small changes to the filename of json file downloaded if necessary.
4. Save it and run it to see the output using cat  output.txt .
5. Also run input2.py similarly.

Creating a web API --
1. Download and install Flask by following any documentation available on the net.
2. Create a file service.py or simply paste the contents from here. Save and exit.
3. Open Lx terminal
	enter command--   FLASK_APP = service.py flask run
4. It shows that it is connected on localhost:5000 port
5. On a new terminal--->  curl localhost:5000
6. Note the output and similarly run service2.py and see the output using curl or the output can also be seen on a local browser.