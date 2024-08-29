# Algorithmic Trading Overview

Algorithmic trading means using computers to make investment decisions.
There are different types of algorithmic trading, the main difference is their speed of execution.

Python is the most popular programming language for algorithmic trading, but Python is slow. It's often used as "glue language" to trigger code that runs in other languages.

Numpy is the most popular Python library for performing numerical computing, although it's written for use in Python but underlying functionality is written in C, which is a faster language.


# Algorithmic Trading Process
1. Collect data
2. Develop a hypothesis for a strategy
3. Backtest that strategy: take the strategy back for as far as we can, and take it to as many markets as you can
4. Implement the strategy in production

# API basics
- Get request: to get data from the data source
- POST request: adds data to the database exposed by the API (create only)
- PUT request: adds and overwrites data in the database exposed by the API
- DELETE: deletes data from the API database

# Project 1: S&P 500 project
## Overview
The S&P 500 is the world's most popular stock market index.
