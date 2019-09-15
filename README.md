# Interoperable_Container_Runtime
** **

## Abstract

Lightweight containers made virtual machines very accessible and easy to use for all. By the time, popular providers come up with different implementations and approaches for managing container functionalities. Thus, created a challenge for performing common container lifecycle functionalities in a common manner. For example, running a command to pull an image in Docker is very different from Containerd or Crio.
 
In order to establish the common ground, OCI came out (For more information see: OCI (Open Container Initiative): https://www.opencontainers.org). However, this standardization does not implicitly state how a container management should function, rather it states how to run a file-system bundle or such. 

In this project, we study the differences in the popular runtimes such as Docker, containerd and implement an interoperable solution that interfaces common container lifecycle-management functionalities. 


** **

## 1.   Vision and Goals Of The Project:

Currently if someone wishes to launch an image in a container or perform any other lifecycle management functions on it, they must be sure that the scripts are configured correctly for the target container. Because, launching an image in Docker container is different than running in Cri-o. 
This locks individuals and businesses into whichever container they started with unless they invest the time required to edit the configuration and their scripts which holds the commands for target container. 

* Set up and study most common container run times. (e.g., Docker, cri-o)

* Study the mostly used lifecycle management functionalities for these runtimes. (e.g., start/stop execution, ps)

* Main goal: The project aims to build a wrapper which will be able to perform some of the mostly used container lifecylcle management functions (e.g., start/stop execution, inspect, ps, etc) on the most popular container runtimes today (e.g., Docker, containerd, cri-o, frakti)


* Stretched goal: The ultimate goal of the project is to enable the set of tests run in the Docker CIS Benchmark across any container runtime. Publishing minumum viable framework for this purpose will enable users to run their security checks using single script across over most popular containers.

Interoperable container runtime will be a tool that allows user to perform a few common container lifecycle management functions among different runtimes(including docker, new containerd, crio, frakti) in one interoperable way. 

## 2. Users/Personas Of The Project:
Interoperble container runtime will be used by companies who wants to use different container runtimes (e.g., for different projects), and inidvidual users who wants to try or use different runtimes for their projects but tired of performing the same function in different ways and languages among different runtimes.

The project is aimed at buisnesses and individuals who will be testing or running containerized programs across numerous runtimes so that they only need a single script. 

PersonA: A software developer would like to move an application from Docker to Cri-o, because he realizes that cri-o is more adaptable with Kubernetes, and using this capability will provide this application a lot more scalibility. However, now he needs to deal with changing all the continous-integration scripts in order to be able to test and deploy his application on this new container run-time. In that point, we plan to deliever interoparable framework to the table!


## 3.   Scope and Features Of The Project:


The project aims to create a framework that enables the some of mostly used container lifecycle management functions across the most popular container runtimes. 
[Subject to change] For the PoC, we plan to implement ps, inspect and start/stop commands over Docker and Cri-o. 
If this is achieved the project also aims to use these functions to bring the Docker CIS Benchmark functionality to most popular runtimes (e.g., Cri-o, containerd). 

The project is not a tool which will ensure that containerized programs are able to work across all runtimes. Rather it is a common framework, that enables to run basic/most common commands over most popular container run-times. 


** **

## 4. Solution Concept

Global Architectural Structure Of the Project:

![alt text](https://github.com/BU-NU-CLOUD-F19/Interoperable_Container_Runtime/blob/master/cloud-architecture.png "Hover text")

Interoperable framework will take place in-between developer and container runtimes. It will interpret the mostly used commands and target runtime in common language/script from user, then in the background execute the functionality in any runtime. 

It aims to provide a common way of lifecycle management of container runtimes in interoperable way.

Design Implications and Discussion:

This section discusses the implications and reasons of the design decisions made during the global architecture design.

## 5. Acceptance criteria

Acceptance criteria is to enable 4 or 5 mostly used commands to execute two different container runtimes such as Docker, and Cri-o. However, as a stretch goal we plan to go beyond it and enable it over at least one more runtime (e.g., containerd or flika) and be able to run Docker CIS benchmark on those runtimes.


## 6.  Release Planning:

Release #1 (due by Week 5): 

* Set up at least two container run-time enviroments (e.g., Docker, Cri-o). 
* Start experimentation with life-cycle functions on runtimes
* Give a detailed report about implementation of requested functionalities (e.g., Start/Stop execution, ps, inspect)

Release #2 (due by Week 7): 

* Implement at least two lifecycle functions over two container runtimes in interoperable framework

Release #3 (due by Week 9): 

* Implement and demo at least two more lifecycle functions over two or three (optional) container runtimes in interoperable framework

Release #4 (due by Week 11): 

* Implement and demo at least two more lifecycle functions over two or three (optional) container runtimes in interoperable framework

Release #5 (due by Week 12): 

* Implement and demo at least one more lifecycle functions over two or three (optional) container runtimes in interoperable framework

* Finalize report and demo end-to-end

Release #5 (due by Week 13) [Stretched goal]: 

* Demo with Docker CIS Benchmark if time permits


** **

## General comments

* Detailed backlogs will take place on the Trello board [Link will be provided]
* This project has an oppurtinity to turn into a research paper that can be submitted to top-tier systems conference
* Architecture diagram will be updated with the more information gained from implementations


** **


