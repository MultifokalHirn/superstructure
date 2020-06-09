# superstructure

**a tool for Erkenntnis through dialectical notetaking**

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![Pytest](https://github.com/MultifokalHirn/superstructure/workflows/pytest/badge.svg?style=flat)](#testing-)
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat)](#contributors-)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com) [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://github.com/MultifokalHirn/superstructure/blob/master/LICENSE)
<!-- ALL-CONTRIBUTORS-BADGE:END -->


<p align="center">
  <img width="100%" src="https://raw.github.com/MultifokalHirn/superstructure/dev/assets/images/logo_window.png" />
</p>

<a name="contents"></a>
## Contents

- [Contents](#contents)
- [Overview](#overview)
    - [The Idea](#idea)
    - [Caveats](#caveats)
- [Development](#development)
    - [Setup](#setup)
    - [Testing](#testing)
    - [Running](#running)
    - [Style Guide](#style)
- [Further Reading](#further_reading)
    - [Documentation](#documentation)
    - [Development Notes](#notes)
    - [Things to Remember](#remember)
    - [License](#license)


<a name="overview"></a>
## Overview

__tl;dr__: tools to help order your thoughts generally do not accomodate dialectical thinking in any meaningful way. superstructure is aiming to do so.

<a name="idea"></a>
### The Idea
 - as any enlightened person will tell you, dialectical thinking is the only method for gaining any actual [Erkenntnis](https://en.wiktionary.org/wiki/Erkenntnis)
 - dialectical thinking inevitably brings about highly complex and interwoven networks of [Begriffe](https://en.wikipedia.org/wiki/Notion_(philosophy))
 - keeping track of all the things that have already been considered during contemplation is difficult enough by itself, but to then also continuously integrate each one of your insights with the next to uncover all the relations between them, and to revise your understanding of them, is, for any sufficiently complex reflection, virtually impossible
 - people use note taking and thoughtful structuring of data as tools to aid them with all kinds of work that involves the mind
 - however, I could not find any tool that was well equipped to help with a dialectical approach to understanding things: each note taking tool was in some shape or form hierarchical - top-down or bottom-up - to accomodate _falsches Bewusstsein_
 - superstructure aims to do for the dialectic method, what mindmaps do for methods uninterested in any meaningful insight

<a name="caveats"></a>
### Caveats
- a computer program, as a thing in itself, can neither fully replicate nor contain the absolute 
- designing the basic logical structure is difficult, because when talking about the Gegenstand of a _Begriff_, that _Gegenstand_ is not actually a Gegenstand, but itself just a _Begriff_, an object in computer land
- isomorphism to the (real) Whole is thus currently not part of the roadmap
- what we can do however, is to facilitate the _Erkenntnisprozess_ in your _Bewusstsein_
- any (future) claims of the opposite are either ironic, or should be ignored

<a name="development"></a>
## Development
- superstructure is implemented in python3

<a name="setup"></a>
### Setup
- superstructure requires python 3.7 or higher, as well as `redis`,because, as of now, it stores its data as pickled objects there

```shell
python3 -mvenv env
source env/bin/activate
pip3 install -r requirements-dev.txt
```

<a name="testing"></a>
### Testing
- testing is fairly simple: a _Bewusstsein_ gets created and it is prefilled with _Begriffe_, and then we will check, whether superstructure obeys some fundamental rules of reality

```shell
source env/bin/activate
python3 -mpytest tests
```


<a name="running"></a>
### Running
- you need a running `redis` instance, and then just run `main.py`

terminal 1
```shell
redis-server
```
terminal 2
```shell
source env/bin/activate
python3 main.py
```


<a name="style"></a>
### Style Guide
- development on superstructure should use `black` for formatting and `bandit` for linting
- development happens on `dev`, merging into `master` constitutes a version bump

<a name="further_reading"></a>
## Further Reading

<a name="documentation"></a>
### Documentation

[superstructure](https://github.com/MultifokalHirn/superstructure/blob/dev/superstructure/README.md) constitutes the logical backend

[metastructure](https://github.com/MultifokalHirn/superstructure/blob/dev/metastructure/README.md) constitutes the tooling for user interaction 

<a name="external_resources"></a>
### External Resources
coming soon

<a name="notes"></a>
### Development Notes
[development_notes.md](https://github.com/MultifokalHirn/superstructure/blob/dev/development_notes.md)

<a name="remember"></a>
### Things to Remember
[things_to_remember.md](https://github.com/MultifokalHirn/superstructure/blob/dev/things_to_remember.md)

<a name="license"></a>
### License

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FMultifokalHirn%2Fsuperstructure.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FMultifokalHirn%2Fsuperstructure?ref=badge_large)

[License File](https://github.com/MultifokalHirn/superstructure/blob/master/LICENSE)
