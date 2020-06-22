# notes


## June 21
* rename core.py to core.py
* _erkenntnismöglichkeit_ instead of valueerror in _bewusstsein_: save incosistencies for later..?
* the question of the user experience: maybe as meditative knowledge construct that slowly builds and can remember things to ask you (inconsistencies are remembered as erkenntnismöglichkeit)
* how to save data? begriff should probably loose "vernunft" and so on, since this doesnt scale (shouldnt then "address" also be a field for begriff since some can have an address, if they refer to people? if not, where do we cut off?)
* bridge between dialectic and propositional logic?
    * -> maybe permit to write notes?
* maybe start with
* GraphViz: visualization of certain links as graphs (obv filtered in some way, _Begriffe in quotes_): "John" is a "Name" for a "Human" and has an "Adress" which is "Name" for a "Place".
    * apparently graphs are visual statements in propositional logic lol
* what is the opposite of Reiner Begriff?
* is Unknown() a good idea? whats a known unknown?
* By a Begriff existing for a Bewusstsein, it has (?) "Sein", and, while it is part of an inconsistency, it is a "Werden"
* rename Bewusstsein to Bewusstseinsinhalt?
* let every Begriff have a list of Bewusstseinsinhalte that it is part of? `aBegriff.context` ?
* grundbegriffe does not work as it does!!!!!! its completely wrong: "Einzelheit" should be an instance of the class Begriff!
* TDD 4 realz?

### Conceptualisations for Bestimmung

* every Begriff by itself is _unbestimmt_! only when its _bestimmt_ can we say something about it!
    * let every begriff have a `myBegriff.as(aBegriff)` function, which equals a _Bestimmung_ and returns a `BestimmterBegriff`?
    * Begriff (UnbestimmterBegriff)
        * has properties (== {quality: [values]})
        * a property should support multiple values, which are selected would be defined through the bestimmungsprozess
    * it needs a "first" `BestimmterBegriff` that is bestimmt by itself: `BestimmteAllgemeinheit` with the property `defining_qualities` == {`defining_qualities`: dict()}, after that, everything is easy
    * BestimmterBegriff + BestimmteAllgemeinheit:
        * every `BestimmterBegriff` has a set of `properties` that are defined by its `BestimmteAllgemeinheiten`
        * a property of a Allgemeinheit is a constant for all Einzelheiten
        * every `BestimmteAllgemeinheit` is a `BestimmterBegriff` that has certain `defining_qualities`, otherwise its implicitly assumed its a `BestimmteEinzelheit`:
            * `anUnbestimmterBegriff.as([bestimmteAllgemeinheit])` -> `aBestimmteAllgemeinheit`
            * for every other `aBestimmteAllgemeinheit`: `aUnbestimmterBegriff.as(aBestimmteAllgemeinheit)` -> `aBestimmteEinzelheit`
        * every `BestimmterBegriff`, that is a `Sein` has either exactly one negation, or None
        * every `BestimmterBegriff`, that is a `Werden` has a set of Negations, even if that set is empty

        * The largest subset of `defining_qualities` of a `BestimmteAllgemeinheit` are its `wesen`
    * Bestimmung
        * `anUnbestimmterBegriff.as([someBestimmterBegriff, someOtherBestimmterBegriff...]) -> aBestimmterBegriff`
            * `anUnbestimmterBegriff.as([someBestimmteAllgemeinheit, someOtherBestimmteAllgemeinheit...]) -> anotherBestimmterBegriff`
            * `anUnbestimmterBegriff.as(anUnbestimmterBegriff.as([BestimmteAllgemeinheit])) -> aBestimmterBegriff`
        * if `aBestimmteAllgemeinheit` is a `Werden`, a  `aBestimmterBegriff` that it has bestimmt can not be a `Sein` (?)
            * `Sein` and `Werden` are each a `BestimmteAllgemeinheit`
        * the properties (== {quality: value, ...}) that a `BestimmterBegriff` has are bestimmt and limited by the `defining_qualities` property of its `bestimmendeAllgemeinheiten`!
            * if some qualities have no value or contradictory (), the `BestimmterBegriff` is a `Werden`, since it can not be a `Sein` if it is this contradictory
        * ??? a BestimmterBegriff could have `bestimmendeAllgemeinheiten` (which make up his _Wesen_)
        * knowledge is manifested in a set of unbestimmteBegriffe and bestimmteBegriffe can be extrapolated from them!
    * Queries
        * `aBegriff.is_bestimmt == (len(aBegriff.is_a()) > 0)`
        * a `BestimmterBegriff` has all attributes that its `BestimmteAllgemeinheiten` have as well!
    * Examples
        * human as `BestimmteEinzelheit` john:
            * `john = humanUnbestimmt.as([animalUnbestimmt.as([bestimmteAllgemeinheit])])`
                * `john` will now be a human, but without any distinct properties
        * john (from above) as `animal`
            * `johnAnimal = john.as( [bestimmteAllgemeinheit, animalUnbestimmt.as([bestimmteAllgemeinheit])])`
        * human as `bestimmteAllgemeinheit`
            * `humanBestimmtAllgemein == humanUnbestimmt.as([bestimmteAllgemeinheit, animalUnbestimmt.as([bestimmteAllgemeinheit])])`
        * `johnBestimmt == john.as(human.as([bestimmteAllgemeinheit]))` -> `aBestimmteEinzelheit` with `human in johnBestimmt.bestimmende_allgemeinheiten` and with `johnBestimmt.properties.name == "john"` with `human.defining_qualities` being a subset of `johnBestimmt.properties.keys()`
        * john.
    * Comments
        * a `BestimmteAllgemeinheit` is a `BestimmterBegriff` that has the property `defining_qualities`
        * a `BestimmteEinzelheit` is a `BestimmterBegriff` with all `defining_qualities` as "keys" in its `properties`
        * _bestimmt_: `john.is_a() -> [human]`
        * _unbestimmt_: `john.is_a() -> [unbestimmterBegriff]`
    * Unclear:
        * maybe only BestimmteAllgemeinheiten can have negations?
        * how to save relationships between bestimmteBegriffe?
        * `johnsName = john.as([named.as(BestimmteAllgemeinheit)])`
        * name = Begriff(properties={"defining_qualities": ["namensträger"]})
        * when adding a quality, automatically add that quality as unbestimmtenBegriff?

### Scenario

> system has not yet had any input from the user. BINARY and WORD are part of the (optional and later on mutable) standard set of Begriffe for a new Bewusstsein

* whenever the user is prompted (e.g. "is the opposite of:") and nothing comes after in the scenario, the user has written nothing and just pressed _enter_
* multiple values are inserted comma seperated

```
$ superstructure
> welcome to superstructure. logged in as "Alice".
$ add ANIMAL
>   ANIMAL is the opposite of:
>   ANIMAL is a kind of: LIVING_BEING
>     LIVING_BEING is the opposite of:
>     LIVING_BEING is a kind of:
>     Defining qualities or parts of a LIVING_BEING: is_alive
>       You mean 'is_alive' as a: BINARY
>       Is 'is_alive' as a BINARY always the same for a HUMAN? (y/n) n
>   Defining qualities or parts of an ANIMAL:
>
$ add HUMAN
>   HUMAN is the opposite of:
>   HUMAN is a kind of: ANIMAL
>   Defining qualities or parts of a HUMAN: first_name, last_name, body
>     You mean the HUMAN's 'first_name' as a: WORD
>       Is 'first_name' as a WORD always the same for a HUMAN? (y/n) n
>     You mean the HUMAN's 'last_name' as a: WORD
>       Is 'last_name' as a WORD always the same for a HUMAN? (y/n) n
>     You mean the HUMAN's 'body' as a:
>
$ add John
>   You mean John as a: HUMAN
>   John's 'first_name' as a WORD: John
>   John's 'last_name' as a WORD: Johnson
>   (Ignoring John's 'body' since I do not know what a 'body' as a quality or part of a HUMAN is.)
>   Does 'is_alive' apply to John as a HUMAN? (y/n) y
>
$ show John
>   John is a HUMAN, which is a kind of ANIMAL, which is a kind of LIVING_BEING.
>     first_name: John
>     last_name: Johnson
>     is_alive: True
>
$ contemplate
>   'first_name' as a WORD is a kind of: NAME
>     Is a NAME a kind of WORD? (y/n): y
>       NAME as ALLGEMEINHEIT is the negation/opposite of:
>       Is the 'string_value' of all NAMEs always the same? (y/n) n
>   'last_name' as a WORD is a kind of: NAME
>   Is 'is_alive' (as a BINARY) a quality of a NAME? (y/n): n
>   Next to HUMANs, a 'body' is a quality or part of a: ANIMAL
>     You mean the ANIMAL's 'body' as a:
>   Is 'is_alive' (as a BINARY) a quality of a NAME?
>   Is a LIVING_BEING a kind of NAME? (y/n): n
>     Good, that would would have complicated things!
>
$ exit
>   bye!
```

The result (leaving out the standard library stuff). defining qualities need not be specific:
```
LIVING_BEING:
    as_a:
        BESTIMMTEALLGEMEINHEIT:
            properties:
                defining_qualities: [is_alive]
                non_applicable_qualities: []
                negation:
            generalizations: []

ANIMAL:
    as_a:
        BESTIMMTEALLGEMEINHEIT:
            properties:
                defining_qualities: [is_alive, body]
                non_applicable_qualities: []
                negation:
            generalizations: [LIVING_BEING]

HUMAN:
    as_a:
        BESTIMMTEALLGEMEINHEIT:
            properties:
                defining_qualities: [first_name, last_name, body, is_alive]
                non_applicable_qualities: []
                negation:
            generalizations: [ANIMAL]

NAME:
    as_a:
        BESTIMMTEALLGEMEINHEIT:
            properties:
                negation:
                defining_qualities: [string_value]
                non_applicable_qualities: [is_alive]
            generalizations: [WORD]

John:
    as_a:
        HUMAN:
            properties:
                first_name:
                    NAME:
                        John
                last_name:
                    NAME:
                        Johnson
                is_alive:
                    BINARY:
                        True
    as_a:
        NAME:
            properties:
                string_value:
                    "John"

Johnson:
    as_a:
        NAME:
            properties:
                string_value:
                    "Johnson"

is_alive:
    as_a:
        BINARY:
            properties: [is_true, is_false]

body:
    as_a:


```

## June 12
* should probably throw out ids and shrink it down to name - whats the difference anyways?

## June 9
* renamed superstructure to metastructure and metastructure to infrastructure to not confuse a module with the project. this naming makes way more sense anyway
* started to get really unsure about the whole logical form thing. if the a.allgemeinheit == b and b.einzelheit == a and a.aufhebung == ... scratch that, it does make sense
* Allgemeinheit and Einzelheit as classes however appear questionable; maybe even use even more abstract language? negative?
* just realized from AbstrakteAllgemeinheit: it should actually be the class Allgemeinheit..


## June 6
* defining abstract concepts that fold into themselves and are interconnected is pretty hard to do when restricted by a language that is interpreted bottom up, not top down
* I have extreme issues even desciding on a set of core "structures". I am not even sure whether the most basic whatchamacallit should outline a thing or a relation. but the good news is, that on this level, I dont even see a difference between the two. I guess I should have read that book on category theory...
* deciding on using German terms is still not final for me. right now it helps me think, but object.is_bestimmt() just feels really wrong
* it is quite unclear to me, why there has to be a set of necessary Begriffe next to the basic structure for it to survive.. Hegel says they are necessary consequences of the basic structure but.. I mean it would be cool if my structure could at some point just generate them itself on startup (without the particular names.. -> this reminds me, Begriffe/Things shouldnt be identifiable through their names, but by their particular structure! no 2 Begriffe can share the same predicates in relation to themselves and others)
* thus, if we have the basic structures thing and relation defined (through themselves), we have a basic set of certain necessary combinations.
* end of day: this looks and feels extremely wrong, but also I dont have a better idea as of know
