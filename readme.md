# Simpsons Parser #

## Introduction ##
In this directory, you'll find a file named 'homer.json' containing data about Homer Simpson. Whilst the data is in JSON format, it contains nested data in a range of different formats. Your job is to implement a parser that makes the tests pass, as described in the feature file. You can decide whether you'd like to implement the parser in Python or C#, you don't need to do both.

## Build & Test ##

### dotnet ###

dotnet restore dotnet/Simpsons.sln  
dotnet build dotnet/Simpsons.sln  
dotnet test dotnet/Simpsons.sln

### Python ###

## Tips ##
Study the nested data, and aim to determine what the formats are before implementing the parser. Feel free to use any libraries you see fit, the only rule is you're not allowed to change the JSON file, or the test implementations!

```
dotnet restore dotnet/Simpsons.sln
dotnet build dotnet/Simpsons.sln
dotnet test dotnet/Simpsons.sln
```

### python ###
You'll need:
* Python 3.6 or higher
* Make
* Pipenv

```
pipenv install
make python_tests
```

or, if you're on windows, or cannot use make:
```
pipenv run behave
```

if you end up running the tests in a different way, please note this along with your submission.

## Tips ##
Study the nested data, and aim to determine what the formats are before implementing the parser. Feel free to use any libraries you see fit, the only rule is you're not allowed to change the JSON file, or the test implementations!
