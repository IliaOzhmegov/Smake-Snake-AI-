# Smake (Smart Snake or Snake-AI)

The main idea of this project is to prove that complicated Machine Learning methods 
and tools not always allow to reach a desired goal. 

The first part of this project is to build an application, which outputs a controllable 
snake game model (in different words a well-known snake game).

The second part is to connect an artificial player which will be simulated by
a simple NN or a simple mathematical model.

And the first part of the project was finished in terms of the small university project, 
the main idea of the pet project is to make acquaintance with some topics of Software engineering.

[//]:#
![video](https://thumbs.gfycat.com/BadHandmadeAntipodesgreenparakeet-size_restricted.gif)

----

Travis-CI:

[![Travis build status](https://travis-ci.org/ElijahOzhmegov/Smake-Snake-AI-.svg?branch=master)](https://travis-ci.org/ElijahOzhmegov/Smake-Snake-AI-)

AppVeyor:

[![Build status](https://ci.appveyor.com/api/projects/status/k9km8fyluwwbox57?svg=true)](https://ci.appveyor.com/project/ElijahOzhmegov/smake-snake-ai)

CodeCov:

[![codecov](https://codecov.io/gh/ElijahOzhmegov/Smake-Snake-AI-/branch/master/graph/badge.svg)](https://codecov.io/gh/ElijahOzhmegov/Smake-Snake-AI-)

CodeClimate:

[![Test Coverage](https://api.codeclimate.com/v1/badges/b1ee1d632109fd5ab639/test_coverage)](https://codeclimate.com/github/ElijahOzhmegov/Smake-Snake-AI-/test_coverage)
<a href="https://codeclimate.com/github/ElijahOzhmegov/Smake-Snake-AI-/maintainability"><img src="https://api.codeclimate.com/v1/badges/b1ee1d632109fd5ab639/maintainability" /></a>

Sonarcloud:

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ElijahOzhmegov_Smake-Snake-AI-&metric=alert_status)](https://sonarcloud.io/dashboard?id=ElijahOzhmegov_Smake-Snake-AI-)

[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ElijahOzhmegov_Smake-Snake-AI-&metric=security_rating)](https://sonarcloud.io/dashboard?id=ElijahOzhmegov_Smake-Snake-AI-)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ElijahOzhmegov_Smake-Snake-AI-&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ElijahOzhmegov_Smake-Snake-AI-)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ElijahOzhmegov_Smake-Snake-AI-&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ElijahOzhmegov_Smake-Snake-AI-)


[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=ElijahOzhmegov_Smake-Snake-AI-&metric=bugs)](https://sonarcloud.io/dashboard?id=ElijahOzhmegov_Smake-Snake-AI-)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=ElijahOzhmegov_Smake-Snake-AI-&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=ElijahOzhmegov_Smake-Snake-AI-)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=ElijahOzhmegov_Smake-Snake-AI-&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=ElijahOzhmegov_Smake-Snake-AI-)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=ElijahOzhmegov_Smake-Snake-AI-&metric=sqale_index)](https://sonarcloud.io/dashboard?id=ElijahOzhmegov_Smake-Snake-AI-)
## 1. UML
To create UML diagrams I used a PlantUML plugin in PyCharm.
### 1.1. Class Diagram
<p align="center">
  <img src="docs/umls/snake_model.png">
</p>

### 1.2. Use Case diagram
<p align="center">
  <img src="docs/umls/use_case_diagram.png">
</p>

### 1.3. Activity diagram
<p align="center">
  <img src="docs/umls/activity_diagram.png">
</p>

## 2. Metrics

Besides the badges at the beginning of the page,
you can find additional information about used metrics
on the following pages:
* [sonarcloud.io](https://sonarcloud.io/dashboard?id=ElijahOzhmegov_Smake-Snake-AI-) 
page 
* [codeclimate](https://codeclimate.com/github/ElijahOzhmegov/Smake-Snake-AI-) page
* [codecov.io](https://codecov.io/gh/ElijahOzhmegov/Smake-Snake-AI-) page


## 3. Clean Code Development
To prove that in this project was used **Clean Code Development** 
principles I will show the results of code analysis services.

1. DRY Principle implementation

    This badge ([![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=ElijahOzhmegov_Smake-Snake-AI-&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=ElijahOzhmegov_Smake-Snake-AI-)) 
    indicates the percent of duplicated lines.
    Also if you check out [codeclimate page](https://codeclimate.com/github/ElijahOzhmegov/Smake-Snake-AI-) 
    of the project, you also will see the number of duplicated lines.

1. SLA Principle implementation

    This principle can be shown via the following badges ([![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ElijahOzhmegov_Smake-Snake-AI-&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ElijahOzhmegov_Smake-Snake-AI-), 
    <a href="https://codeclimate.com/github/ElijahOzhmegov/Smake-Snake-AI-/maintainability"><img src="https://api.codeclimate.com/v1/badges/b1ee1d632109fd5ab639/maintainability" /></a>), 
    because mentioned services evaluate code complexity.
    
1. Law of Demeter implementation

    Applying the Law of Demeter would only allow access to public 
    methods 
    of the class **Snake**.
    ![imgage](docs/pics/law_of_demeter.png)


### CI/CD
Travis-CI service after the unit tests sends 
a report to CodeClimate.com about test coverage.
Details can be found in **travis.yml** file.
