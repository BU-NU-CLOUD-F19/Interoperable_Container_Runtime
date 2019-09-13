# Interoperable_Container_Runtime
** **

## Project Description Template

Background : With the OCI standard being established for container runtime, we are seeing multiple implementations becoming popular (including legacy Docker, and new containerd, crio, frakti). Although these allow flexibility in hosting containers, they create a challenge for performing common container management operations in an interoperable manner (e.g. putting an image onto crio is much different than doing so with Docker)

Project specifics : In this project we will study the differences in these popular runtimes and implement an interoperable solution to implement common container management operations. This work will be open-sourced and useful in having an interoperable container management framework.
For more information see:
OCI (Open Container Initiative): https://www.opencontainers.org


This template proposal contains a number of sections, which you can edit/modify/add/delete/organize as you like.  Some key sections we’d like to have in the proposal are:

- Vision: An executive summary of the vision, goals, users, and general scope of the intended project.

- Solution Concept: the approach the project team will take to meet the business needs. This section also provides an overview of the architectural and technical designs made for implementing the project.

- Scope: the boundary of the solution defined by itemizing the intended features and functions in detail, determining what is out of scope, a release strategy and possibly the criteria by which the solution will be accepted by users and operations.

Project Proposal can be used during the follow-up analysis and design meetings to give context to efforts of more detailed technical specifications and plans. It provides a clear direction for the project team; outlines project goals, priorities, and constraints; and sets expectations.

** **

## 1.   Vision and Goals Of The Project:

Interoperable container runtime will be a tool that allows user to perform a few common container lifecycle management functions among different runtimes(including docker, new containerd, crio, frakti) in one interoperable way. 

## 2. Users/Personas Of The Project:
Interoperble container runtime will be used by companies who wants to use different runtimes(for different projects maybe), and inidvidual users who wants to try or use different runtimes for their projects but tired of performing the same function in different ways among different runtimes.

## 3.   Scope and Features Of The Project:

The Scope places a boundary around the solution by detailing the range of features and functions of the project. This section helps to clarify the solution scope and can explicitly state what will not be delivered as well.

It should be specific enough that you can determine that e.g. feature A is in-scope, while feature B is out-of-scope.

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
