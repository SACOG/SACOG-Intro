# SACOG GitHub Usage Guide


## Guide Version Information

-   Last updated: February, 2020

-   Updated by: Darren Conly



# Purpose of This Guide

Managing code and documentation is complex. There are lots of versions,
subversions, archived versions, on top of having many different
projects, some of which are ongoing, others that are "one-off". Without
a plan to manage and organize code, it can quickly become difficult to
find what you're looking for, people will make duplicative efforts, and
time is wasted. This document aims to make SACOG's reasonably usable and
efficient both to frequent users and first-time or casual users by
establishing some guidelines for using it. The guidelines will help
users with organization questions such as:

-   Should something I'm working on be its own repository? Or should it
    be within an existing repository?

-   When should I create a branch of a repository?

-   If I create a branch, when do I merge the branch back with the main?

-   When should I commit changes?


## What this guide is NOT

This guide is NOT intended to teach how to use git. As described above,
it is a set of guidelines and conventions for how to keep SACOG's GitHub
repository organized and user-friendly. If you want help learning git
itself, there are many references available online, a sample of which
include:

-   <https://guides.github.com/> - various overviews including git
    commands, principles, etc.

-   <https://docs.github.com/en/desktop> - for installing GitHub's
    desktop GUI (instead of using the command line)

-   <https://gitimmersion.com/> - in-depth learn-by-doing set of
    exercises to learn git on the command line



# What goes into a repository?

The following types of files can or should be in GitHub repositories:

-   *Code* - GitHub is first and foremost for storing and tracking
    changes to code. So any code files are welcome and encouraged. This
    includes python, SQL, Voyager, Javascript, ESRI Arcade, VBA, etc.

-   *Documentation for code* -- Good documentation will allow us to
    better share externally and internally, as well as allow us to
    remember how to use stuff we may have written long ago!

-   *Environment data files* -- Conda and pip environment files allow
    you to succinctly list out all dependencies needed to run the code
    in the repository.

-   *Parameter and template files needed to run the code*

-   *SMALL data files (\<500KB ideally)* -- GitHub has limited storage
    (\<500MB for the organization), therefore we cannot store large data
    sets on it. As a workaround it is better to provide documentation on
    how to easily access the data through other means (e.g. SACOG Open
    Data Portal, process to gain FTP access, etc.)



## Documentation Guidelines

### Where to put documentation

Each separate "tool" within a repository should have documentation. In
some cases, a repository will have only one tool, but other repositories
may have many scripts and tools spread into multiple levels of
subfolders. Use your judgement to determine whether you just need a
single readme or more in-depth instructions, or multiple separate sets
of instructions (e.g. in the SACSIM repository, have separate
documentation for the ILUT processing tool and the SACSIM model run
script).

### Use Markdown Please!

Documentation should be stored in the repository as a **markdown (.md)**
file, not as a word doc. Storing as markdown allows users to open it in
the web browser and have it appear nicely formatted with links, headers,
etc. If you store it on GitHub as a Word doc (.docx), people visiting
the GitHub page will not be able to view it in their browser and will
need to open it with MS Word, which might not be installed on all users'
computers.

To make a markdown file, you can use Word to write your documentation,
then can convert the .docx file to markdown using any number of free
online conversion tools (e.g.
<https://www.freefileconvert.com/docx-md>).
[Pandoc](https://pandoc.org/) is also a neat command-line tool for
converting docx to md (and lots of other conversions).



## What should NOT go into a repository

-   *BIG (\>500KB) data files* -- GitHub is not meant to store large
    data sets. If you have a large data set, please include in the
    repository easily accessible information on how to access the data
    set (e.g. link to SACOG Open Data Portal, process to gain FTP
    access, etc.).

-   *Files that are not relevant to the repository*



# When should I create a new repository?

Effectively parceling out projects is a balancing act:

-   If you are *too specific* (e.g., you have lots of repositories with
    a single script), then the SACOG GitHub will have hundreds of
    repositories to wade through and it can get hard to keep track of
    them, kind of like if you store all your files on the desktop of
    your computer.

-   If you are *too general* with categorizing repositories, then
    repository performance can suffer (e.g. normal commit, push, etc.
    operations become slower and less reliable), and also it can be
    unwieldy for end users---e.g., if I have a repository with 100
    scripts but as a user only want to grab 5 of them, it would be
    annoying to clone the whole repository, and methods for partially
    cloning a repository are a bit clunky.

Given the above, creating repositories requires judgement, and
reorganization will likely be necessary as scripts evolve. **As some
general guidance**:

-   DO create a new repository if:

    -   You're making a major new version of a repository, e.g.,
        SACSIM23, when it comes out, should be a separate repository
        from SACSIM19, and SACSIM19 should be converted to an archived
        repository.

    -   Your set of scripts is part of a "significant SACOG project",
        i.e., a year-long+ or ongoing project, like SACSIM travel model,
        Replica,

    -   Your set of scripts is part of a larger category of regularly
        used processes, e.g. "NPMRDS scripts", "GTFS scripts", etc.

-   Do NOT:

    -   Create repositories based on your name. GitHub will be outward
        facing and shared, and users are looking for that cool piece of
        code your wrote---not for you . Plus, naming repositories based
        on person name increases risk of people writing duplicate code.
        Any code you share should either go into an existing repository,
        or if justified, should be put into a new repository that is
        named based on what the code *does*, not your name.

    -   Create new repositories without first considering whether your
        code could or should be put within an existing repository. This
        will reduce the number of repositories and make the agency
        GitHub page easier to navigate.



# How should I organize my repository?

The goal of organizing repositories consistently and logically is to
enable users (internal and external) to easily find the script or
documentation they're looking for, without having to ask for help.
Achieving this will vary across repositories, but some general
guidelines to follow include:

-   



# Conventions for Branching

## Rule \#1: Do not make edits to the "main" or "master" branch

As a goal, we always want the main version of a branch to be
*deployable*, i.e., if someone downloads the main version of the code,
it will be a functioning version of the code. To uphold this goal:

-   Whenever you're working on or editing code, the edits should be on a
    branch of the code.

-   Only merge the branch into main code (making the edits effective in
    the main version) after testing the code in the branch and
    confirming it works. This way, the main version can stay up to date
    as being "the most up-to-date but stable" version of the code.

## When should I create a new branch?

\*\*\*Note\*\*\* this section is "tentative" and many change based on
experience and needs.

There are a number of potential workflows for git, but for most SACOG
repositories, the best workflow would be the [GitHub
Flow](https://guides.github.com/introduction/flow/) model. Using this
model, any time you want to change something in the repository, be it
for a bug fix, adding a new feature, etc., you create a new branch \>
make edits and do testing in the branch, then once you've finished
testing, you merge the branch back into the main version, making your
changes "official" in the deployable working version.

### Branch naming conventions

When naming your branch, please use the convention *\<your
initials\>-\<descriptive name\>*. E.g., for the SACSIM repository, if I
make a change to a series of scripts that make the ILUT summary, I would
create a branch and name it dc-ilut-update.

With this system, we can keep track of who is making changes and what
those changes are



## When should I merge a branch?

Following "Rule 1" described above, merging should only happen after
making updates and testing to make sure those updates don't cause any
issues. If you're working on code that involves various people and needs
review, you can merge via a pull request, which is basically a
documented way of saying "I made some changes to the code, they seem
pretty good, but I want other people to comment and review it before I
make it the main version of the code."

After making updates and testing, you can merge to the main branch,
which makes your changes part of the main, deployable version of the
code.



## When should I delete a branch?

Branches can be safely deleted once they have been merged with the main
branch. It is **good practice to delete branches once they have been
merged** to avoid having too many branches and creating confusion.

### Deleting in GitHub vs. Deleting Locally

Deleting a branch in GitHub will not delete the remote URL connection
that the local version of the branch has. E.g., if a testing branch in
the local repo has a URL to GitHub \> you delete the testing branch on
GitHub \> then push the local version of the testing branch to GitHub,
the testing branch will be re-created on GitHub. So if you really want
to delete a branch, you have to do so both locally and on GitHub.



# When should I commit changes?
Each time you commit, you're creating a checkpoint in the Git history, a place that you can "rewind" to if you make mistakes in the future. If you do not make commits frequently enough, you risk having to "rewind" to a very distant point in time if you mess something up. If you commit too frequently, you make the commit/change log very long and less easy to navigate. 

So short answer is that there is no fixed rule for committing. But these are some general times it would be good to commit your changes:
* When you have successfully added a new feature or change to code
* After making significant changes
* At the end of the day
* You made a change you want to share on GitHub




# References

1.  GitHub guides for all major things related to GitHub -
    <https://guides.github.com/>

2.  Git Tower list of Git best practices -
    <https://www.git-tower.com/learn/git/ebook/en/command-line/appendix/best-practices/>

3.  8 Version Control Best Practices -
    <https://www.perforce.com/blog/vcs/8-version-control-best-practices>

4.  Commit Often, Perfect Later, Publish Once: Git Best Practices
    <http://sethrobertson.github.io/GitBestPractices/>

5.  Four branching workflows for Git
    <https://medium.com/@patrickporto/4-branching-workflows-for-git-30d0aaee7bf>

    a.  But "GitHub flow" model is probably appropriate for most SACOG
        applications

6.  All about markdown (.md) files -
    <https://www.markdownguide.org/getting-started/>
