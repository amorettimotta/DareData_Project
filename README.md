[![CI](https://github.com/amorettimotta/DareData_Project/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/amorettimotta/DareData_Project/actions/workflows/ci.yml)

# Foundations Learning Path Assignments

## Introduction

We are going to be using this project throughout the course.

This assignment uses life expectancy in Europe grouped by Country (or other, like group of countries), Age, Sex, and Time. But the data format makes it hard to use. We will be building a pipeline do clean the data, while applying the concepts you've learned in the previous modules.

## Installing

Before installing, make sure your `pip` is up to date.

```bash
pip --version
```

Prior to the introduction of `pyproject.toml`-based builds (in PEP 517 and PEP 518), pip had only supported installing packages using setup.py files that were built using `setuptools`. But in version 21.3, pip added support for performing editable installs of packages that use `pyproject.toml`. This means that you can use pip to install packages described in the `pyproject.toml`.

To update pip, run:

```bash
pip install --upgrade pip
```

Now you're ready to go!

1. Clone this repo.
2. Copy `assignments` folder into a separate project `mv -r nos-lp-foundations/assignments assignments`.
3. Move into the assignments folder (`cd assignments`) and start a new repo (`git init`).
4. Create a virtual environment with `python -m venv .venv`.
   > **Note for Anaconda users**: We would prefer if you exit the automatic conda environments and tried using the steps above, as they are the canonical Python way of creating virtual environments. However, we realize working that way might be tricky for Anaconda users since Anaconda usually changes the configurations of your machine. If you are having too many problems getting started, then feel free to use the "conda way" of handling environments.  I.e.: create a virtual environment with `conda create --name foundations`.
5. Activate the virtual environment with `source .venv/bin/activate` or `.venv\Scripts\activate` on Windows.
   > **Note for Anaconda users**: Same as above, if you are having too many problems getting started, then feel free to activate the environment with `conda activate foundations` instead.

Don't install the project yet. We will do that in [setup assignment](./assignment_0/README.md).

## Using this project

Open the `README.md` file inside each assignment and follow the instructions.

> Note: Remember that all commands inside the Readme files assume you are in the root of the project.

- Try to keep the pace with the group's progress, neither falling too behind or advancing too much by themselves.
- Don't let their peers' code reviews go stale.
- Don't ignore the questions and improvements asked by the person reviewing your code.
- Be courteous and respectful  to your peers and mentor.
- Set your progress expectations with your mentor.
- Conduct yourself with integrity and honesty.

### Expectations for mentors

A mentor are tasked in ensuring their peers become better professionals, as such, we expect them to:

- Reserve at least 30 minutes per week for each group you mentor, for answering questions and giving feedback.
- Encourage group members and communicate openly.
- Be courteous and respectful to your mentees.
- Ensure code reviews go smoothly: oversee and help, but don't overtake the reviewer's responsibilities.
- Keep track of questions and progress of the group members (see [Progress tracking](#progress-and-questions-tracking))
- Conduct yourself with integrity and honesty.

## Progress and Questions Tracking

In order to help mentors in tracking the progress of their groups, we suggest using the following template:

- [Progress  Question Tracking template](https://docs.google.com/spreadsheets/d/1nODnLBLCcC6Dqe_pK_bog-BA78E9AuUq1l4S81Px61w/edit?usp=sharing)

Tracking questions is important so that we can improve the quality of the selected material, as well as create new ones.

## Pre-requisites

In order to make the best use out of this learning path, you should know:

- Basic / Intermediary Python: control flow, functions, handling errors, data structures, files, virtual environments, data manipulation libraries.
- Basic Git: add, commit, checkout, merge, and rebase

## Suggested learning calendar

> **Note**: This is just a suggestion. Groups are encouraged to set their own deadlines with their mentors.

Week 01 _(~3.0 hours)_

- Clean code part 1: Long code is not good code (2h10)
- Assignment #0

Week 02 _(~2.0 hours)_

- Clean code part 2: Names and Comments (2:00)

Week 03 _(~3.0 hours)_

- Linting (0:30)
- Continuous integration (0:05)
- Assignment #1

Week 04 _(~2.5 hours)_

- Git strategies (0:20)
- Assessing code quality: reviews and structures (1:30)
- Assignment #2

Week 05 _(~1.5 hours)_

- Testing (1:30)

Week 06 _(~3 hours)_

- Assignment #3 (3:00)

Week 07 _(~2.5 hours)_

- Object-oriented programming (2:30)

Week 08 _(~2.0 hours)_

- Text editors (1:30)
- Assignment #4

Week 09 _(~3 hours)_

- Design patterns (3:00)

Week 10 _(~2.5 hours)_

- Assignment #5 (2:30)

## Assignments

Assignments are located inside the `assignments` folder. The assignment instructions assume you are issuing commands from that folder.

In it, you'll find a project folder called `life_expectancy` as well as folders with instructions for each assignment. Each assignment builds upon the previous one and they are all meant to be do inside the project folder.

## Call to Adventure

The goal of this course is to be your personal companion on being a better programmer. We hope you enjoy it and learn a lot from it.

Feel free to open [GitHub issues](https://github.com/DareData/lp-foundations/issues) to give us feedback and ideas for new features. Or even better, open a [pull request](https://github.com/DareData/lp-foundations/pulls) with your suggestions.
test
