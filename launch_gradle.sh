#!/usr/bin/env bash

gradle build -PpyDistType="bdist_wheel --universal" | tee gradle_report.txt