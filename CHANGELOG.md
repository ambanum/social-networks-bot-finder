Changelog
=========


v1.2.0 (2021-07-13)
-------------------

New
~~~
- Feat: support json files with several users to batch process data.
  [Martin Ratinaud]

Other
~~~~~
- Docs: add contributing guide. [Martin Ratinaud]


v1.1.1 (2021-07-12)
-------------------

New
~~~
- Feat: add automatic generation of changelog when releasing new
  version. [Martin Ratinaud]


v1.1.0 (2021-07-12)
-------------------

New
~~~
- Feat: add support for passing a json array of users with rawjson.
  [Martin Ratinaud]

Changes
~~~~~~~
- Chore: fix release to always take into account the new version.
  [Martin Ratinaud]


v1.0.1 (2021-07-12)
-------------------

Fix
~~~
- Remove datetime as it results in a not valid JSON. [Martin Ratinaud]


v1.0.0 (2021-07-12)
-------------------

New
~~~
- Feat : updated the model. [Antoine-Barre]
- Feat : added contributing file. [Antoine-Barre]

Changes
~~~~~~~
- Chore: remove unwanted files from git. [Martin Ratinaud]
- Chore: add troubleshooting informations. [Clément Biron]

Fix
~~~
- Changed difficult explanations. [Antoine-Barre]

Other
~~~~~
- Merge pull request #3 from ambanum/doc/install_on_M1. [Clément Biron]

  ops: install on M1
- Doc: fix pip install in README. [Vincent Viers]
- Ops: working docker for ARM/M1 (using conda image) [Vincent Viers]
- Merge pull request #4 from ambanum/refacto/vviers. [Antoine-Barre]

  Refacto/vviers
- Clean: minor formatting. [Vincent Viers]
- Clean: remove useless length function. [Vincent Viers]
- Refacto: change import order to respect pep8 convention. [Vincent
  Viers]
- Refacto: add config file. [Vincent Viers]
- Ops: add docker image + doc. [Vincent Viers]
- Ops: install on M1. [Vincent Viers]
- Update CONTRIBUTING.md. [Antoine-Barre]


v0.1.0 (2021-06-29)
-------------------

New
~~~
- Feat: add easy setup for bumping versions when releasing. [Martin
  Ratinaud]


v0.0.4 (2021-06-29)
-------------------

New
~~~
- Feat: display version of package with --version. [Martin Ratinaud]
- Feat: refactor to be able to install command line easily on local.
  [Martin Ratinaud]
- Feat : added an explanation. [Antoine-Barre]
- Feat: add ability to pass directly a JSON string extracted from
  snscrape to prevent an unecesary call to snscrape. [Martin Ratinaud]
- Feat : test adding a feature to read jsonRaw from file. [Antoine-
  Barre]
- Feat: add bash command for easier use. [Martin Ratinaud]
- Feat: make script return a full json to make it processable by other
  tools. [Martin Ratinaud]
- Feat: add explanation md file. [Clément Biron]

Changes
~~~~~~~
- Chore: replace call to os by directly calling click help method.
  [Martin Ratinaud]
- Chore: freeze package versions to prevent problems of version
  mismatch. [Martin Ratinaud]
- Chore: clean. [Martin Ratinaud]
- Chore: prevent syncing of unwanted files. [Martin Ratinaud]

Fix
~~~
- Use absolute paths for files to not break when installed on other
  machines. [Martin Ratinaud]
- Include joblib file in package. [Martin Ratinaud]
- Distinguish local requirements from release one as it is a good
  practice. [Martin Ratinaud]
- Better files structure for dataset. [Clément Biron]
- Use more global solution to access files even if launched from another
  folder. [Martin Ratinaud]

Other
~~~~~
- Docs: add explanation on how to release a new version. [Martin
  Ratinaud]
- Update explanation.md. [Clément Biron]

  Add french translation
- Added an example. [Antoine-Barre]
- Corrected some mistakes. [Antoine-Barre]
- Add files via upload. [Antoine-Barre]
- Updated with consolidated dataset. [Antoine-Barre]
- Docs: update docs with every command. [Martin Ratinaud]
- Wip. [Martin Ratinaud]
- Add files via upload. [Antoine-Barre]
- Update README.md. [Antoine-Barre]
- Docs: add link to methodology. [Martin Ratinaud]
- Docs: add return type of function. [Martin Ratinaud]
- Docs: add install instructions. [Martin Ratinaud]
- Add files via upload. [Antoine-Barre]
- Add files via upload. [Antoine-Barre]
- Update explanation.md. [Clément Biron]

  feat: improve temp text
- Update BotClassifier.py. [Antoine-Barre]
- Update requirements.txt. [Antoine-Barre]
- Update README.md. [Antoine-Barre]
- Update README.md. [Antoine-Barre]
- Create requirements.txt. [Antoine-Barre]
- Simplified the script. [Antoine-Barre]
- Create README.md. [Antoine-Barre]
- Init. [Antoine-Barre]
- Add files via upload. [Antoine-Barre]


