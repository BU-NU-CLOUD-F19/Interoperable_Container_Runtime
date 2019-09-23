# Interoperable_Container_Runtime
** **

## Abstract

Lightweight containers make virtual machines accessible and easy to use for all. Popular providers have implemented different implementations and approaches for managing container functionalities. This creates a challenge for performing common container lifecycle functionalities in a common manner. For example, running a command to pull an image in Docker is very different from Containerd or Crio. The Open Container Initiative (OCI, https://www.opencontainers.org) has been established to create a open standard for container use. However, this standardization does not cover lifecycle-management, instead specifying initialization of images.  In this project, we will study the differences in the popular runtimes such as Docker, containerd, and crio to implement a lifecycle mangement solution that is operable with popular container types, interfacing common container lifecycle-management functionalities. 


** **

## 1.   Vision and Goals Of The Project:

Currently if someone wishes to launch an image in a container or perform any other lifecycle management functions on it, they must be sure that the scripts are configured correctly for the target container, as (for example) launching an image in a Docker container differs from running in Cri-o. This locks individuals and businesses into whichever container they started with unless they invest the time required to edit the configuration and their scripts which holds the commands for target container. In order to address this and develop a means to enable users to perform lifecycle management in a platform agnostic manner, we must begin with the following:

* Set up and study most common container run times. (e.g., Docker, cri-o)

* Study the mostly used lifecycle management functionalities for these runtimes. (e.g., start/stop execution, ps)

Our main goal is to build a wrapper which will be able to perform some of the mostly used container lifecylcle management functions (e.g., start/stop execution, inspect, ps, etc) on the most popular container runtimes today (e.g., Docker, containerd, cri-o, frakti)

The ultimate goal of the project, although considered a stretch goal within the timeframe of this project, is to enable the set of tests run in the Docker CIS Benchmark across any container runtime. Publishing minumum viable framework for this purpose will enable users to run their security checks using single script across over most popular containers.

Interoperable container runtime will be a tool that allows user to perform a few common container lifecycle management functions among different runtimes(including docker, new containerd, crio, frakti) in one interoperable way. 

## 2. Users/Personas Of The Project:

The intended user is a software developer who is managing applications across containers running on different runtimes, in particular testing applications across different containers.
 
Example: A software developer would like to move an application from Docker to Cri-o, because he realizes that cri-o is more adaptable with Kubernetes, and using this capability will provide this application a lot more scalibility. Presently, he needs to deal with changing all the continous-integration scripts in order to be able to test and deploy his application on this new container run-time. With the interoperability framework in place, the developer is able to manage the lifecycle of each container type with a single set of commands.


## 3.   Scope and Features Of The Project:


The project aims to create a framework that enables the some of mostly used container lifecycle management functions across the most popular container runtimes. 

[Subject to change] For the PoC, we plan to implement ps, inspect and start/stop commands over Docker and Cri-o. 
If this is achieved the project also aims to use these functions to bring the Docker CIS Benchmark functionality to most popular runtimes (e.g., Cri-o, containerd). 

[See https://www.cisecurity.org/benchmark/docker/]


** **

## 4. Solution Concept

Global Architectural Structure Of the Project:

![alt text](https://github.com/BU-NU-CLOUD-F19/Interoperable_Container_Runtime/blob/master/figures/cloud-architecture.png "Hover text")

Interoperable framework will take place in-between developer and container runtimes. It will interpret the mostly used commands and target runtime in common language/script from user, then in the background execute the functionality in any runtime. 

It aims to provide a common way of lifecycle management of container runtimes in interoperable way.

Design Implications and Discussion:

* The implementation in the background for essential lifecycle functions will be examined. And the way containers interact with underlying Operating System will be analyzed
* According to findings and common ways of executions, we'll add those functionalities to our framework
* Interoperable frame will probably be developed in Python. 
* All the functions will be implemented in interoperable way that, end-user would not need to care about against which container run-time their systems will run

Architecture of the Docker runtime:

![alt text](https://github.com/BU-NU-CLOUD-F19/Interoperable_Container_Runtime/blob/master/figures/Docker-architecture.png "Hover text")

Docker actually uses runc to run the container but implement image management and APIs on top. You can think of these features -- which include image transport, image management, image unpacking, and APIs -- as high-level features compared to runc's low-level implementation.

CRI-O and Containerd also use runc for low-level container functionalities. Therefore, we'll analyze the overhead introduced by higher level runtimes such as Docker on top of runc. And use runc to create interoperable way of managing containers.


## 5. Acceptance criteria

Acceptance criteria is to enable 4 or 5 mostly used commands to execute on at least two different container runtimes such as Docker, and Cri-o. However, as a stretch goal we plan to go beyond it and enable it over at least one more runtime (e.g., containerd or flika) and be able to run Docker CIS benchmark on those runtimes.


## 6.  Release Planning:

Release #1 (due by Week 5): 

* Set up at least two container run-time enviroments (e.g., Docker, Cri-o). 
* Start experimentation with life-cycle functions on runtimes
* Give a detailed report about implementation of requested functionalities (e.g., Start/Stop execution, ps, inspect)

Release #2 (due by Week 7): 

* Implement two lifecycle functions over two container runtimes in interoperable framework

Release #3 (due by Week 9): 

* Implement and demo one more lifecycle functions over two or three (optional) container runtimes in interoperable framework

Release #4 (due by Week 11): 

* Implement and demo one more lifecycle functions over two or three (optional) container runtimes in interoperable framework

Release #5 (due by Week 12): 

* Implement and demo one more lifecycle functions over two or three (optional) container runtimes in interoperable framework

* Finalize report and demo end-to-end

Release #6 (due by Week 13) [Stretched goal]: 

* Demo with Docker CIS Benchmark if time permits


** **

## General comments

* Detailed backlogs will take place on the Trello board [Link will be provided]
* This project has an oppurtinity to turn into a research paper that can be submitted to top-tier systems conference
* Architecture diagram will be updated with the more information gained from implementations


** **


