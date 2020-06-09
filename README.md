# superstructure
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![Pytest](https://github.com/MultifokalHirn/superstructure/workflows/pytest/badge.svg?style=flat)](#testing-)
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat)](#contributors-)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com) [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://github.com/MultifokalHirn/superstructure/blob/master/LICENSE)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

**a tool for Erkenntnis through dialectical notetaking**


- [overview](#overview)
    - [the idea](#idea)
    - [caveats](#caveats)
- [development](#development)
    - [setup](#setup)
    - [testing](#testing)
    - [running](#running)
    - [style guide](#style)
- [further reading](#further_reading)
    - [documentation](#documentation)
    - [development notes](#notes)
    - [license](#license)


<a name="overview"></a>
## overview

<a name="idea"></a>
### the idea
 - __tl;dr__: tools to help order your thoughts generally do not accomodate dialectical thinking in any meaningful way. superstructure is aiming to do so.

 - as any enlightened person will tell you, dialectical thinking is the only method for gain any actual [Erkenntnis](https://en.wiktionary.org/wiki/Erkenntnis)
 - dialectical thinking inevitably brings about highly complex and interwoven networks of [Begriffe](https://en.wikipedia.org/wiki/Notion_(philosophy))
 - keeping track of all the things that have already been considered during contemplation is difficult enough by itself, but to then also continuously integrate each one of your insights with the next to uncover all the relations between them, and to revise your understanding of them, is, for any sufficiently complex reflection, virtually impossible
 - people use note taking and thoughtful structuring of data as tools to aid them with all kinds of work that involves the mind
 - however, I could not find any tool that was well equipped to help with a dialectical approach to understanding things: each note taking tool was in some shape or form hierarchical - top-down or bottom-up - to accomodate _falsches Bewusstsein_
 - superstructure aims to do for the dialectic method, what mindmaps do for methods uninterested in any meaningful insight

<a name="caveats"></a>
### caveats
- a computer program, as a thing in itself, can neither fully replicate nor contain the absolute 
- designing the basic logical structure is difficult, because when talking about the Gegenstand of a _Begriff_, that _Gegenstand_ is not actually a Gegenstand, but itself just a _Begriff_, an object in computer land
- isomorphism to the (real) Whole is thus currently not part of the roadmap
- what we can do however, is to facilitate the _Erkenntnisprozess_ in your _Bewusstsein_
- any (future) claims of the opposite are either ironic, or should be ignored

<a name="development"></a>
## development
- superstructure is implemented in python3

<a name="setup"></a>
### setup
- superstructure requires python 3.7 or higher, as well as `redis`,because, as of now, it stores its data as pickled objects there
- 

```shell
python3 -mvenv env
source env/bin/activate
pip3 install -r requirements-dev.txt
```

<a name="testing"></a>
### testing
- testing is fairly simple: a _Bewusstsein_ gets created and it is prefilled with _Begriffe_, and then we will check, whether superstructure obeys some fundamental rules of reality

```shell
source env/bin/activate
python3 -mpytest tests
```


<a name="running"></a>
### running
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
### style guide
- development on superstructure should use `black` for formatting and `bandit` for linting
- development happens on `dev`, merging into `master` constitutes a version bump

<a name="further_reading"></a>
## further reading

<a name="documentation"></a>
### documentation
[superstructure](https://github.com/MultifokalHirn/superstructure/blob/dev/superstructure/README.md)

<a name="notes"></a>
### development notes
[development_notes.md](https://github.com/MultifokalHirn/superstructure/blob/dev/superstructure/development_notes.md)

<a name="license"></a>
### license
[MIT](https://github.com/MultifokalHirn/superstructure/blob/master/LICENSE)
