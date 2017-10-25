# Alfred Angular Snippets
Code Snippets for Angular

This is based on the [Angular Snippets repository](https://github.com/johnpapa/vscode-angular-snippets) created by [John Papa](https://github.com/johnpapa) for [Visual Studio Code](https://code.visualstudio.com).

## Requirements
* [Alfred 3](https://www.alfredapp.com)
* [Alfred 3 Powerpack](https://www.alfredapp.com/powerpack/) (paid upgrade — it's worth it!)

## Installation
* Download the [latest release](https://github.com/ejsuncy/alfred-angular-snippets/releases/download/v0.1.0/alfred-angular-snippets-v0.1.0.alfredworkflow) and open it with Alfred

## Updates
* This workflow auto-updates to the latest release by checking the repository once daily and prompting the user to install the update.
* You can also force update with magic argument: `ng workflow:update`

## Usage
* The keyword for Angular snippets is `ng`
* For example, summon Alfred and type `ng comp`
* Your query following `ng` is matched against the snippet names via Alfred workflow's default `filter` function.

See it in action here, where I have the following apps open: vim in a terminal, WebStorm, Sublime Text, and MS Word (just for fun!):

![Snippets in Action][snippets]

### Snippet Names
Your query will be matched against the following snippet names:

| Typescript Snippets |
| --- |
|Angular Component|
|Angular Component with Inline Template|
|Angular Service|
|Angular Pipe|
|Angular Default Route Path|
|Angular 404 Route Path|
|Angular Eager Route Path|
|Angular Lazy Route Path|
|Http.get|
|HttpClient.get|
|Angular Http Service|
|Angular HttpClient Service|
|Angular HttpInterceptor|
|Output Event|
|Subscribe|
|Angular Root Component|
|Angular Root Module|
|Angular Routing Module|
|Angular Module|
|Angular Directive|
|Angular CanActivate Guard|
|Angular CanActivateChild Guard|
|Angular CanLoad Guard|
|Angular CanDeactivate Guard|
|Angular Router Events|
|Angular Module SkipSelf Constructor|
|RxJS Observable Import|
|RxJS ReplaySubject Import|
|RxJS Subject Import|
|RxJS BehaviorSubject Import|
|RxJS Add Operator Import|
|RxJS Add Observable Import|

|HTML Snippets|
|---|
|class|
|style|
|ngClass|
|ngFor|
|ngFor with trackBy|
|ngForAsync|
|ngIf|
|ngIfElse|
|ngModel|
|ngRouterLink|
|ngRouterLinkWithParameter|
|ngSelect|
|ngStyle|
|ngSwitch|
|pre w/ json|
|pre w/ async json|
|container|
|template|
|content|
|resolver|

## Development
After changing the source files and/or snippet files, you'll need to export the project as a .alfred3workflow file.

I've included in this repository a modified gist from [here](https://gist.github.com/deanishe/b16f018119ef3fe951af) to build and export the workflow ([workflow-build.py](workflow-build.py)).
It includes dependencies that you'll need to install. Here's a recommended workflow:
* `virtualenv ~/.envs/workflow-build` creates a virtual environment so you can install the dependencies in their own sandbox
* `source ~/.envs/workflow-build/bin/activate` activates the virtual environment
* `cd alfred-angular-snippets` moves you to the repo directory
* `pip install -r requirements.txt` installs the dependencies in this sandbox (leaving your global/system python alone)
* `python workflow-build.py -o output_dir .` exports the current repo directory as a .alfred3workflow file, excluding the following patterns:
* `deactivate` deactivates the virtual environment

|EXCLUDE PATTERNS|
|---|
|\*.pyc|
|\*.log|
|.DS_Store|
|\*.acorn|
|\*.swp|
|\*.sublime-project|
|\*.sublime-workflow|
|\*.git|
|\*.dist-info|
|\*.egg-info|
|\*.gif|
|README.md|
|workflow-build.py|
|requirements.txt|
|\*.idea|

You can add more patterns in the [workflow-build.py file](workflow-build.py) to exclude new file types that you don't want packaged in the zip file.

 

## Release Notes
### `v0.1.2`
* Merge upstream changes: #1, #2, #3
* Increment version number: #4

### `v0.1.1`
* Increment version to test auto-updates

### `v0.1.0`
* Initial commit


[snippets]: https://github.com/ejsuncy/alfred-angular-snippets/blob/master/snippets.gif
