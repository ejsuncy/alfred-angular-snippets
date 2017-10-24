# Alfred Angular Snippets
Code Snippets for Angular

This is based on the [Angular Snippets repository](https://github.com/johnpapa/vscode-angular-snippets) created by [John Papa](https://github.com/johnpapa) for [Visual Studio Code](https://code.visualstudio.com).

## Requirements
* [Alfred 3](https://www.alfredapp.com)
* [Alfred 3 Powerpack](https://www.alfredapp.com/powerpack/) (paid upgrade — it's worth it!)

## Installation
* Download the [latest release](https://github.com/ejsuncy/alfred-angular-snippets/releases/download/v0.1.0/alfred-angular-snippets-v0.1.0.alfredworkflow) and open it with Alfred

## Updates
* This workflow auto-updates to the latest release by checking the repository once daily.

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

## Release Notes
### `v0.1.2`
* Merge upstream changes: #1, #2, #3
* Increment version number: #4

### `v0.1.1`
* Increment version to test auto-updates

### `v0.1.0`
* Initial commit


[snippets]: https://github.com/ejsuncy/alfred-angular-snippets/blob/master/snippets.gif
