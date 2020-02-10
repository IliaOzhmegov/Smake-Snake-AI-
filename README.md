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
During development were used  **Clean Code Development** principles
and PEP Conventions.

1. [Method Names and Instance Variables](https://pep8.org/#method-names-and-instance-variables):
    Use the function naming rules: lowercase with words separated by underscores as necessary to improve readability.
    ```python
    def __get_pos_on_screen(self, snake_pos):
        return snake_pos * self.scale_coef + self.scale_coef // 2
    ```
2. [Class Names](https://pep8.org/#class-names):
    Class names should normally use the CapWords convention.
    ```python
    class Playground(object):
        ...
    class Food:
        ...
    class Direction:
        ...
    ```
3. Function rules: Small, Do one thing, Use descriptive names:
    ```python
    def get_body(self):
        return self.__body
   
    def get_body_list(self):
        return [segment.get_pos() for segment in self.get_body()]

    def get_speed(self):
        return self.__speed.dir

    def get_position(self):
        return self.__position.pos

    def get_allowed_space(self):
        return self.__pg.rows, self.__pg.rows

    def get_seen_food_pos(self):
        return self.__food.get_pos()
    ```
4. Source code structure: Similar function should be close
    ```python
    def __is_injuring_itself(self, new_position):
        segments = [segment.pos for segment in self.__body]
        if new_position.get_pos() in segments:
            return True
        return False

    def __is_colliding_wall(self, new_position):
        if new_position.get_pos() in self.__borders:
            return True
        return False

    def get_body(self):
        return self.__body

    def get_body_list(self):
        return [segment.get_pos() for segment in self.get_body()]

    def get_speed(self):
        return self.__speed.dir

    def get_position(self):
        return self.__position.pos

    def get_allowed_space(self):
        return self.__pg.rows, self.__pg.rows

    def get_seen_food_pos(self):
        return self.__food.get_pos()

    def turn(self, new_dir):
        new_speed = self.__speed + Direction(direc=new_dir)
        if any(new_speed) != 0:
            self.__speed = Direction(direc=new_dir)

    def move(self):
        new_position = self.__position + Position(self.__speed.get_dir())

        if self.__is_injuring_itself(new_position):
            return Snake.self_collision

        if self.__is_colliding_wall(new_position):
            return Snake.wall_collision

        self.__position = new_position
        self.__move_body()
    ```
5. [Maximum Line Length](https://pep8.org/#maximum-line-length):
    Limit all lines to a maximum of 79 characters.
    ```python
    pygame.draw.rect(self.screen, Window.GREEN,
                     (x_pos - self.scale_coef // 2,
                      y_pos - self.scale_coef // 2,
                      self.scale_coef, self.scale_coef))
    ```
   Interesting fact: Python does not have namespaces like C++ or
   Java, so I use Constants logically attached to the class 
   (`Window.GREEN`). PEP keeps silence in this case.
   
[CCD Cheatsheet](https://user-images.githubusercontent.com/35653122/51113192-86f8d880-1801-11e9-90ad-88dd58854a18.png)

## 4. Build Management with PyGradle and Gradle
The easiest way to use Build Management system with
Python is [PyGradle](https://github.com/innobead/pygradle).
It does the following things:
* installs environment, dependencies
* launches tests
* builds python wheel
* generates docs (html and xml)

In current project:
* [build.gradle](build.gradle) file has instructions to build.
* [gradle_report.txt](gradle_report.txt) file is an output example.

To have possibility to launch gradle even without IDE
I have made a simple [bash script](launch_gradle.sh), that
does this. 

## 5. Unit-Tests
Although, the project has GUI, it was not covered by
tests by understandable reasons. Only the snake model 
was covered. 
[test_snake_model.py](tests/the_game/backend/test_snake_model.py)

## 6. Continuous Integration
Unfortunately my project does not have delivery part at least 
standard one like PyPI or some Python-based website. 
So Let's assume I  deliver my project just on github 
with all green/yellow 
values of the badges. So that all of them were green or at 
least yellow for such badges as test coverage.

My Pipeline: 
![pipeline](docs/pics/Pipeline.png)

First of all, Travis-CI is responsible for Linux and 
AppVeyer for Windows.

Travis-CI service after the unit tests sends 
reports to CodeClimate.com and codecov.io.
Details can be found in **travis.yml** file for 
Travis and in **appveyor.yml**, **tox.ini** for AppVeyor.

* [Travis-CI report](https://travis-ci.org/ElijahOzhmegov/Smake-Snake-AI-)
* [AppVeyor report](https://ci.appveyor.com/project/ElijahOzhmegov/smake-snake-ai)

Gradle report usually looks like on the picture below.
![Gradle report](docs/pics/gradle_report.png)

## 7. IDE 

I have used PyCharm as my IDE.

I used such plugins as:
* IdeaVim (to fasten development)
* PlantUML (to draw UML diagrams)
* Nyan Progress Bar (because it is fun)

About my knowledge of vim, besides simple things from vimtutor, I can
write a complex Macros (with usage increment and decrement), launch 
shell utils regarding to the text in the editor (for example
to show only the 10th column of a big csv file I can do this
`:% !colomn -c 10 -t -c,` ), operate with buffers and etc.

Also I used some shortcuts in the IDE:
* Run script (**⌘R**) (there is a conflict with vim, so it can be different from default set up)
* Debug script (**⌘D**) (there is a conflict with vim, so it can be different from default set up)
* Commit (**⌘K**)
* Refactor rename (**⇧F6**)
* Preferences.. (**⌘,**)

## 8. DSL
Domain Specific Language was created to control the snake. You can see
usage example below.
![dsl](https://thumbs.gfycat.com/AdorableEminentBoar-size_restricted.gif)

As you can see there is used vim navigation to control the snake
, because I am a fan of vim. Also, there was provided opporinity to
enter commands in lots of different ways. For example, instead of
to push `ENTER` 11 times to reach food a player can just enter `11k`.
In addition a player can enter series commands for instance 
`5h k l k 23h`.







