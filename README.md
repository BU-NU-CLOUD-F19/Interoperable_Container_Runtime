# Interoperable_Container_Runtime
** **

## Abstract

Lightweight containers made virtual machines very accessible and easy to use for all. By the time, popular providers come up with different implementations and approaches for managing container functionalities. Thus, created a challenge for performing common container lifecycle functionalities in a common manner. For example, running a command to pull an image in Docker is very different from Containerd or Crio.
 
In order to establish the common ground, OCI came out (For more information see: OCI (Open Container Initiative): https://www.opencontainers.org). However, this standardization does not implicitly state how a container management should function, rather it states how to run a file-system bundle or such. 

In this project, we study the differences in the popular runtimes such as Docker, containerd and implement an interoperable solution that interface common container lifecycle-management functionalities. 


** **

## 1.   Vision and Goals Of The Project:

Currently if someone wishes to launch an image in a container or perform any other lifecycle management functions on it, they must be sure that the scripts are configured correctly for the target container. Because, launching an image in Docker container is different than running in Cri-o. 
This locks individuals and businesses into whichever container they started with unless they invest the time required to edit the configuration and their scripts which holds the commands for target container. 

* Main goal: The project aims to build a wrapper which will be able to perform some of the mostly used container lifecylcle management functions (e.g., start/stop execution, inspect, ps, etc) on the most popular container runtimes today (e.g., Docker, containerd, cri-o, frakti)


* Stretched goal: The ultimate goal of the project is to enable the set of tests run in the Docker CIS Benchmark across any container runtime. Publishing minumum viable framework for this purpose will enable users to run their security checks using single script across over most popular containers.

Interoperable container runtime will be a tool that allows user to perform a few common container lifecycle management functions among different runtimes(including docker, new containerd, crio, frakti) in one interoperable way. 

## 2. Users/Personas Of The Project:
Interoperble container runtime will be used by companies who wants to use different container runtimes (e.g., for different projects), and inidvidual users who wants to try or use different runtimes for their projects but tired of performing the same function in different ways and languages among different runtimes.

The project is aimed at buisnesses and individuals who will be testing or running containerized programs across numerous runtimes so that they only need a single script. 

PersonA: A software developer would like to move an application from Docker to Cri-o, because he realizes that cri-o is more adaptable with Kubernetes, and using this capability will enable this application a lot more scalibility. However, now he needs to deal with changing all the continous-integration scripts in order to be able to test and deploy his application on this new container run-time. In that point, we plan to deliever interoparable framework to the table!


## 3.   Scope and Features Of The Project:


The project aims to create a framework that enables the some of mostly used container lifecycle management functions across the most popular container runtimes. 
[Subject to change] For the PoC, we plan to implement ps, inspect and start/stop commands over Docker and Cri-o. 
If this is achieved the project also aims to use these functions to bring the Docker CIS Benchmark functionality to most popular runtimes (e.g., Cri-o, containerd). 

The project is not a tool which will ensure that containerized programs are able to work across all runtimes. Rather it is a common framework, that enables to run basic/most common commands over most popular container run-times. 


** **

## 4. Solution Concept

This section provides a high-level outline of the solution.

Global Architectural Structure Of the Project:

This section provides a high-level architecture or a conceptual diagram showing the scope of the solution. If wireframes or visuals have already been done, this section could also be used to show how the intended solution will look. This section also provides a walkthrough explanation of the architectural structure.

 

Design Implications and Discussion:

This section discusses the implications and reasons of the design decisions made during the global architecture design.

## 5. Acceptance criteria

This section discusses the minimum acceptance criteria at the end of the project and stretch goals.



## 6.  Release Planning:

Release planning section describes how the project will deliver incremental sets of features and functions in a series of releases to completion. Identification of user stories associated with iterations that will ease/guide sprint planning sessions is encouraged. Higher level details for the first iteration is expected.

** **

## General comments

Remember that you can always add features at the end of the semester, but you can't go back in time and gain back time you spent on features that you couldn't complete.

** **

For more help on markdown, see
https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

In particular, you can add images like this (clone the repository to see details):

![alt text](https://github.com/BU-NU-CLOUD-SP18/sample-project/raw/master/cloud.png "Hover text")
