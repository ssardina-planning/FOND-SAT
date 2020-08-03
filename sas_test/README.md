# SAS Testing and Analysis

The SAS encoding by the FD Translator can be found [here](http://www.fast-downward.org/TranslatorOutputFormat#operator).

Annotated pdfs comparing PDDL files with resulting SAS can be found in dir `SAS-notes/`. 

## Generate no running examples of different sizes

Script `problem_generator.py` can generate no-running corridor problems of different sizes:

```bash
python3 problem_generator.py 10
```

This will generate two files:
 
 * `generalized_domain_10.pddl` for domain `no_running_10`
 * `generalized_problem_10.pddl` for problem `p10`, using domain `no_running_10`.


## Translate PDDL to SAS

This is taken from [this post](https://github.com/orgs/ssardina-planning/teams/fond-sat/discussions/1/comments/13)

The translate folder contains the FD parser code. The main file is [`translate.py`]( (../src/translate/translate.py). It takes 4 arguments

- Time limit
- Domain PDDL file
- Problem PDDL file
- Sas output file name

For example:

```bash
python translate/translate.py 100 ../sas_test/conditional_domain.pddl ../sas_test/problem.pddl ../sas_test/conditional_1.sas`
```

The translate.py won't run on Python3.8, as it uses a deprecated function `time.clock()`. I ran it with 2.7. 

I'll probably change the code to make it run on Python 3.8.


To do the translation:

```bash
python translate/translate.py 100 ../sas_test/conditional_domain.pddl ../sas_test/problem.pddl ../sas_test/conditional_1.sas
```

