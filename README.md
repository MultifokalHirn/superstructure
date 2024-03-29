<!-- IMAGE-->
<p align="center">
  <img width="60%" src="https://raw.github.com/MultifokalHirn/superstructure/dev/assets/images/logo_window.png" />
</p>

# superstructure
> a tool for Erkenntnis through dialectical notetaking

[![Pytest](https://github.com/MultifokalHirn/superstructure/workflows/pytest/badge.svg?style=flat)](https://github.com/MultifokalHirn/superstructure/actions)
[![Coverage Status](https://coveralls.io/repos/github/MultifokalHirn/superstructure/badge.svg)](https://coveralls.io/github/MultifokalHirn/superstructure)
[![Dependabot Status](https://badgen.net/dependabot/thepracticaldev/dev.to?icon=dependabot&color=brightgreen)](https://dependabot.com)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com) [![Contributors][contributors-shield]][contributors-url]
[![Code Style](https://badgen.net/badge/Code%20Style/black?color=000000)](https://github.com/psf/black)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://github.com/MultifokalHirn/superstructure/blob/master/LICENSE)



<!-- CONTENTS -->
<a name="contents"></a>
## Contents

* [Overview](#overview)
    * [Idea](#idea)
    * [Caveats](#caveats)
* [Usage](#usage)
    * [Setup](#setup)
    * [Running](#running)
* [Contributing](#contributing)
    * [General Remarks](#remarks)
    * [Setup for Development](#setup_dev)
    * [Testing](#testing)
    * [Style Guide](#style)
    * [Discussion](#discussion)
* [Further Reading](#further_reading)
    * [Documentation](#documentation)
    * [Books, Papers, and other External Resources](#external_resources)
    * [Development Notes](#notes)
* [Licensing](#licensing)
* [Acknowledgements](#acknowledgements)

<!-- OVERVIEW -->
<a name="overview"></a>
## Overview

> __tl;dr__: tools to help order your thoughts generally do not accommodate dialectical thinking in any meaningful way. `superstructure` is aiming to do so.

<!-- IDEA -->
<a name="idea"></a>
### Idea

* as any enlightened person will tell you, dialectical thinking is the only method for gaining any actual [_Erkenntnis_](https://en.wiktionary.org/wiki/Erkenntnis)
* dialectical thought inevitably brings about highly complex and interwoven networks of [_Begriffe_](https://en.wikipedia.org/wiki/Notion_(philosophy))
    * keeping track of all the things that have already been considered during contemplation is difficult enough by itself, but to then also continuously integrate each one of your insights with the next to uncover all the relations between them, and to revise your understanding of them, is, for any sufficiently complex reflection, virtually impossible
* hence, people use note taking and thoughtful structuring of data as tools to aid them with all kinds of work that involves the mind
    * however, I could not find any tool that was well equipped to help with a dialectical approach to understanding things: each note taking tool was in some shape or form hierarchical - top-down or bottom-up - to accommodate _falsches Bewusstsein_
* `superstructure` aims to do for the dialectic method, what mindmaps do for methods uninterested in any meaningful insight

<!-- CAVEATS -->
<a name="caveats"></a>
### Caveats

* a computer program by its nature can neither fully replicate nor contain the _Absolute_
* designing the basic logical structure is difficult, because when talking about the _Gegenstand_ of a _Begriff_, that _Gegenstand_ is not actually a _Gegenstand_, but itself just a _Begriff_, an object in computer land
* isomorphism to the (real) _Whole_ is thus currently not part of the roadmap
* what we can do however, is to facilitate the _Erkenntnisprozess_ in your _Bewusstsein_
* any (future) claims of the opposite are either ironic, or should be ignored


<!-- USAGE -->
<a name="usage"></a>
## Usage

> `superstructure` requires python3.7 or higher

<!-- SETUP -->
<a name="setup"></a>
### Setup

```sh
$ python3 -m venv env
$ source env/bin/activate
$ python3 -m pip install -r requirements.txt
$ python3 -m pip install --editable .
```

<!-- RUNNING -->
<a name="running"></a>
### Running

* start `superstructure` in CLI mode
```sh
$ source env/bin/activate
$ python3 superstructure/cli.py
```


<!-- CONTRIBUTING -->
<a name="contributing"></a>
## Contributing

 <p>
    <a href="https://github.com/MultifokalHirn/superstructure/issues">Report Bug</a>
    ·
    <a href="https://github.com/MultifokalHirn/superstructure/issues">Request Feature</a>
</p>

<!-- GENERAL REMARKS -->
<a name="remarks"></a>
### General Remarks

Any contributions to `superstructure`, be they in the form of comments or code, are **greatly appreciated**. If you want to contribute some code, please do so by following this common procedure:

1. fork the project
2. create your feature branch (`git checkout -b feature/new_stuff`)
3. commit your changes (`git commit -m 'Add some new stuff'`)
4. push to the branch (`git push origin feature/new_stuff`)
5. open a pull request to `dev`


<!-- SETUP -->
<a name="setup_dev"></a>
### Setup for Development

```sh
$ python3 -m venv env
$ source env/bin/activate
$ python3 -m pip install -r requirements-dev.txt
$ export BETTER_EXCEPTIONS=1
$ pre-commit install && pre-commit install -t pre-push
$ pre-commit run --all-files
$ python3 -m pip install --editable .  # build project according to setup.py
$ python setup.py bdist_wheel  # create wheel
$ twine upload --repository testpypi dist/*  # upload wheel to testpypi (requires ~/.pypirc)
$ twine upload dist/*  # CAUTION: upload wheel to pypi (requires ~/.pypirc)
```


<!-- TESTING -->
<a name="testing"></a>
### Testing
* testing is fairly simple: a _Bewusstsein_ gets created and it is prefilled with _Begriffe_, and then we will check, whether `superstructure` obeys some fundamental rules of reality

```sh
$ source env/bin/activate
$ export BETTER_EXCEPTIONS=1
$ python3 -mpytest --cov=superstructure --cov-report term-missing tests
$ python3 main.py
```
or simply

```sh
$ ./run_tests
```

<!-- STYLE GUIDE -->
<a name="style"></a>
### Style Guide
* development on `superstructure` should use `black` for formatting and `bandit` + `flake8` for linting
* development happens on `dev`, merging into `master` constitutes a version bump


<!-- DISCUSSION -->
<a name="discussion"></a>
### Discussion
* [General Discussion](https://github.com/MultifokalHirn/superstructure/issues/1)
* [General Questions](https://github.com/MultifokalHirn/superstructure/issues/3)
* [wiki](https://github.com/MultifokalHirn/superstructure/wiki)


<!-- FURTHER READING -->
<a name="further_reading"></a>
## Further Reading

<!-- DOCUMENTATION -->
<a name="documentation"></a>
### Documentation

```
.
├── superstructure
|   |
|   ├── metastructure
|   |   ├── grundbegriffe.py
|   |   ├── form.py
|   |   ├── geist.py
|   |   └── core.py
|   |
|   ├── hyperstructure
|   |   └── vernunft.py
|   |
|   ├── infrastructure
|   |   ├── storage
|   |   |   └── pickled.py
|   |   |
|   |   └── logo.py
|   |
|   └── cli.py
|
└── tests
|       ├── test_geist.py
|       └── test_core.py
|
└── main.py
```

* [_metastructure_](https://github.com/MultifokalHirn/superstructure/blob/dev/superstructure/metastructure): constitutes the set of structures underlying the superstructure
* [_hyperstructure_](https://github.com/MultifokalHirn/superstructure/blob/dev/superstructure/hyperstructure): constitutes the tooling for analyzing structures found in `metastructure`
* [_infrastructure_](https://github.com/MultifokalHirn/superstructure/blob/dev/superstructure/infrastructure): constitutes the tooling for user interaction
* [_tests_](https://github.com/MultifokalHirn/superstructure/blob/dev/tests): constitutes tests

<!-- Notes -->
<a name="notes"></a>
### Notes on Phenomenology of Spirit
#### Summary
Phenomenology of Spirit by G.W.F. Hegel is a philosophical work that explores the concept of Spirit and its relationship to the individual. The book is divided into three sections: the Phenomenology of Spirit, the Science of Logic, and the Philosophy of Right. In the Phenomenology of Spirit, Hegel examines the development of Spirit from its most basic form, the immediate consciousness, to its highest form, the absolute Spirit. He argues that Spirit is a process of self-realization, in which the individual must overcome the limitations of their immediate consciousness in order to reach a higher level of understanding. In the Science of Logic, Hegel examines the nature of logic and its role in the development of Spirit. He argues that logic is the foundation of all knowledge and that it is essential for the development of Spirit. Finally, in the Philosophy of Right, Hegel examines the concept of right and its relationship to the individual. He argues that right is the basis of all ethical behavior and that it is essential for the development of Spirit. The overall message of the book is that Spirit is a process of self-realization, in which the individual must overcome the limitations of their immediate consciousness in order to reach a higher level of understanding.

#### Important ideas
* The true form of philosophy is intuition, or immediate knowledge of the Absolute.
* The individual's share in the total work of Spirit is very small.
* Language is the more truthful form of expression, as it expresses the true content of sense-certainty.
* The power of the negative is essential to Spirit's progress.
* The ethical order exists as something given, and the customs and laws are a specific ethical substance.
* War is the form in which the essential moment of the ethical substance, the absolute freedom of the ethical self from every existential form, is present in its actual and authentic existence.
* The supreme reality and the reality which stands in the greatest antithesis to universal freedom is the freedom and individuality of actual self-consciousness itself.
* The shapes of the totality of Spirit display themselves in a temporal succession, for only the whole has true actuality and therefore the form of pure freedom in face of an other.
* The divine Being descends from its universality, through the mediation of the Cult, into individuality, and thus unites itself with reality.


<!-- EXTERNAL RESOURCES -->
<a name="external_resources"></a>
### Books, Papers, and other External Resources

* G. W. F. Hegel: [_Die Wissenschaft der Logik_](http://hegel.logik.1.abcphil.de)
* Thomas Sören Hoffmann: [_Georg Wilhelm Friedrich Hegel - Eine Propädeutik_](https://www.verlagshaus-roemerweg.de/Marix_Verlag/Thomas_Soeren_Hoffmann-Georg_Wilhelm_Friedrich_Hegel-EAN:9783865392909.html)
* Yaozhi Jiang: [_Mathematical Foundation for Dialectical Logic - An Introduction for Making Dialectical Logic Mathematically_](https://www.researchgate.net/publication/333679776_Mathematical_Foundation_for_Dialectical_Logic_-An_Introduction_for_Making_Dialectical_Logic_Mathematically)
* Huacan He, Yanquan Zhou, and Zhicheng Chen: [_Research on Mathematical Dialectical Logic for Intelligent Information Processing_](www.mdpi.com%2F2504-3900%2F1%2F3%2F149%2Fpdf&usg=AOvVaw1CQNOH4PHOZT5htUXa5oFk)
* nLab: [Formalization of _Hegel's Science of Logic_ in Categorical logic / in Modal homotopy type theory](https://ncatlab.org/nlab/show/Science+of+Logic#FormalizationText)
* Hrgb. Andreas Arndt, Christian Iber and Günter Kruck: [_Hegels Lehre vom Begriff, Urteil und Schluss_](https://www.degruyter.com/view/title/311014)
* Sven Jürgensen: [_Freiheit in den Systemen Hegels und Schellings_](https://books.google.ae/books?id=sL_fb9p-q5YC&dq=hegel+bestimmt+unbestimmt&hl=en)
* [hegel.net](https://hegel.net/en/e0.htm)
* [github.com/m-strasser/hegelizer](https://github.com/m-strasser/hegelizer)
* https://labs.kagi.com/ai/sum?url=https://archive.org/stream/phenomenology-of-spirit-g-w-f-hegel/Phenomenology%2520of%2520Spirit%2520-%2520G%2520W%2520F%2520Hegel_djvu.txt&expand=1

<!-- DEVELOPMENT NOTES -->
<a name="notes"></a>
### Development Notes

[CHANGES.md](https://github.com/MultifokalHirn/superstructure/blob/dev/CHANGES.md)

[things_to_remember.md](https://github.com/MultifokalHirn/superstructure/blob/dev/things_to_remember.md)


<!-- LICENSING -->
<a name="licensing"></a>
## Licensing

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FMultifokalHirn%2Fsuperstructure.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FMultifokalHirn%2Fsuperstructure?ref=badge_large)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/badge/all_contributors-1-red.svg?style=flat
[contributors-url]: https://github.com/MultifokalHirn/superstructure/graphs/contributors


<!-- ACKNOWLEDGEMENTS -->
<a name="acknowledgements"></a>
## Acknowledgements

* thanks Hegel
