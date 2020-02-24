# Projetimezor

A simple project manager, which allows users who loves working on billion different things at the same time to manage their time and have automatic assigned projects.  

### Requirements

## Kivy

Kivy is an open source python library used for interfaces.
To install, simply [follow the instructions as listed in Kivy documentation.](https://kivy.org/doc/stable/installation/installation-windows.html)

Projtimezor use version 1.11.0 of Kivy, and is not compatible with python 3.8. To make it compatible, replace the installation command line

```
pip install kivy==1.11.1
```

by

```
pip install kivy[base] kivy_examples --pre --extra-index-url https://kivy.org/downloads/simple/
```


## Installation

Simply clone git repo into your personal folder.

To launch Projtimezor, use the following command in your Projtimezor folder :

```
python -m projtimezor
```

## FAQ

### How does Priority works ?

Priority is used to give more importance to a project.
When comparing two projects, priority will be given to the project with the highest value.

To calculate the impact of the priority value, we need two values, which are set in the config file :
- **max_priority** : the highest value you can set to a project. _(default is **10**)_
- **priority_impact** : factor applied to elapsed_time when max_value is reached _(default is **0.5**)_

Differences between two projects will be established when retrieving project data, according to the following algorithm :

```
priority_mapping_range = interp1d([config.min_priority, config.max_priority],[1, config.priority_impact])
ponderated_elapsed_time = project.elapsed_time.seconds * float(priority_mapping_range(project.priority))
```

To simplify, project elapsed time is mapped from priority range to priority_impact range. This has the effect to reduce elapsed time when priority is high, increasing chances to get this particular project at initialization.
