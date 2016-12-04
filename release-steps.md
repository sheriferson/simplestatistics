# Steps for PyPI release/update

See more details [here].

- Do you have a setup.py?
- Update changelog.txt
- Update version number in documentation
- Update version number in setup.py
- Convert README.md to README.rst
- Add tarball download url to setup.py
- If there are new files that should be included, edit MANIFEST.in
- Commit all those changes. Have a clean repo.
- Add/create a git tag
- Push git tag to remote
- Confirm that GitHub has generated the release file
- Release testing
    * `python setup.py register -r pypitest`
    * `python setup.py sdist upload -r pypitest`
    * `pip install -i https://testpypi.python.org/pypi simplestatistics`
- Release
    - `python setup.py register -r pypi`
    - `python setup.py sdist upload -r pypi`
    - `pip install simplestatistics`
- Add changelog notes to GitHub release page/tag

[here]: http://sherifsoliman.com/2016/09/30/Python-package-with-GitHub-PyPI/
