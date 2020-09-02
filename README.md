# Search-CSP
A Graphical Framework implementation of Search &amp; CSP section of Russel AI book



## Navigate

* [Enviroments](#envs)
* [Algorithms](#algorithms)
* [Credits](#credits)




# envs


Home

    Public

    Stack Overflow
    Tags
    Users
    Find a Job
    Jobs
    Companies

    Teams
    What’s this?

        Free 30 Day Trial

Github Markdown Same Page Link
Ask Question
Asked 5 years, 7 months ago
Active 3 months ago
Viewed 43k times
94

Let's say I have two points within the same git hub wiki page, which for this we'll call place 1 and place 2.

##Title

###Place 1

Hello, this is some text to fill in this, [here](place2), is a link to the second place.

###Place 2

Place one has the fun times of linking here, but I can also link back [here](place1).

An alternative is a ToC.

##Title
[ToC]
###Place 1
###Place 2

Is there any way to do this? Note - seen this so I'll assume it's on topic. Also, that deals with going between files, this one deals with going between the same file.
github hyperlink markdown anchor
share improve this question
edited May 20 at 10:21
Alberto S.
67099 silver badges2525 bronze badges
asked Jan 16 '15 at 9:52
Alexander Craggs
4,34833 gold badges1717 silver badges3737 bronze badges

    1
    possible duplicate of How do you create & link to a named anchor in Multimarkdown – flyx Jan 16 '15 at 9:58
    @flyx - Thanks, if this works I'll reply back =) – Alexander Craggs Jan 16 '15 at 9:59
    2
    this answer is probably the relevant one for you. – flyx Jan 16 '15 at 9:59
    @flyx Tiny bit late, but thanks! That did indeed help me out a bunch :) – Alexander Craggs Aug 30 '17 at 20:38

add a comment
3 Answers
Active
Oldest
Votes
123

This works on Github:

## Title

### Place 1

Hello, this is some text to fill in this, [here](#place-2), is a link to the second place.

### Place 2

Place one has the fun times of linking here, but I can also link back [here](#place-1).

### Place's 3: other example

Place one has the fun times of linking here, but I can also link back [here](#places-3-other-example).

Summary of the conversion rules:

    punctuation marks will be dropped
    leading white spaces will be dropped
    upper case will be converted to lower
    spaces between letters will be converted to -

A good example document with plenty of links and formatting is LivingSocial API Design Guide
share improve this answer
edited May 20 at 9:52
Alberto S.
67099 silver badges2525 bronze badges
answered Aug 4 '17 at 14:06
FelixEnescu
2,83411 gold badge2929 silver badges3131 bronze badges

    2
    Note that the ref link itself must be coded as lower case. Using the example above, if you link to [here](#Place-2), the link won't work. Note how in the example, the heading is called "Place 2" and the link to it is (properly) called [here](#place-2). – DaveL17 Nov 19 '17 at 15:27
    5
    If you have 2 or more headings with the same name Place the links will be named place, place-1, place-2, etc. Then if you also have an explicit header Place 2 its link will be place-2-1. – Kevin May 10 '18 at 13:29
    1
    The answer is still helpful as it works in Gitlab Wiki. The html method (using anchor tag in the gitlab wiki) doesn't work. I understand the question was about github though. – Nditah Oct 9 '19 at 12:20
    It does not seems to be supported in BitBucket. I use the anchor <a name="link"> instead. – рüффп Jul 9 at 10:38

add a comment
0

Unfortunately, it appears that GitHub wiki strips all of the "id=.." tags from custom HTML that you add to a wiki page, so the only working anchors within a page are the headings.
share improve this answer
answered Apr 6 at 17:36
cpurdy
1,05755 silver badges1212 bronze badges
add a comment
25


# algorithms



# credits
