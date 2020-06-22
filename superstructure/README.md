# superstructure
> [superstructure](https://github.com/MultifokalHirn/superstructure/blob/dev/superstructure) is everything

## Basics

.
|
├── metastructure
|   ├── grundbegriffe.py
|   ├── form.py
|   ├── geist.py
|   └── core.py
|
├── hyperstructure
|   └── vernunft.py
|
├── infrastructure
|   ├── storage
|   |   └── pickled.py
|   |
|   └── logo.py
|
└── cli.py

## Usage

### dormant state
* saved Begriffe for each Bewusstsein (account)

### interactive state
> whenever a BestimmteEinzelheit has a value for all qualities of a BestimmteAllgemeinheit, add it to the list of Seiende Begriffe
> adding: whenever a Begriff is mentioned that is not known, go through the adding loop there first

* add
    * `anUnbestimmterBegriff` (will be saved as a `UnbestimmterBegriff` with no `bestimmendeAllgemeinheiten` except for `UnbestimmterBegriff`)
        * ask for opposite
        * ask for "is a kind of" (bestimmendeAllgemeinheiten)
            * ask for properties based on these
        * ask for any other properties
    * `aBestimmteEinzelheit`
        * ask for "as a:"
            * selection must be a known `BestimmteAllgemeinheit`
    * `aBestimmteAllgemeinheit` - must be ALL CAPS
        * ask for opposite
        * ask for "is a kind of"
            * selection must be a known `BestimmteAllgemeinheit`
        * ask for defining qualities
* show
    * `anUnbestimmterBegriff` (by name)
    * `anUnbestimmterBegriff` as
        * `aBestimmteAllgemeinheit`
        * [`someBestimmteAllgemeinheit`, `someOtherBestimmteAllgemeinheit`, ...]
    * all Begriffe that are "bestimmable"
* update
    * properties of `anUnbestimmterBegriff` (very unstructured)
    * properties of `anUnbestimmterBegriff` as
        * `aBestimmteAllgemeinheit`
        * [`someBestimmteAllgemeinheit`, `someOtherBestimmteAllgemeinheit`, ...] (qualitatively the same, but in the long run easier for the user)
    * turn `anUnbestimmterBegriff` into a Allgemeinheit
        * by answering "is a kind of " ...
        * by adding `defining_qualities` as property
* contemplate
    * system asks questions that arise from the data
        * if `someUnbestimmterBegriff` has a set of `properties` that are all in the `defining_qualities` of  `someBestimmteAllgemeinheit`, but some parts from `defining_qualities` of `someBestimmteAllgemeinheit` are missing from the set of `properties` of `someUnbestimmterBegriff`, ask for an Urteil about that `quality` in `someUnbestimmterBegriff`
