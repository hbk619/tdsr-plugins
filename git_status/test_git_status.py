from git_status import parse_output

modified_staged = """On branch my-branchie
Changes to be committed:
(use "git restore --staged <file>..." to unstage)
modified:   ma/path/to/staged.md

Changes not staged for commit:
(use "git add <file>..." to update what will be committed)
(use "git restore <file>..." to discard changes in working directory)
modified:   a_modified_file
modified:   path/to/a_modified_file

Untracked files:
(use "git add <file>..." to include in what will be committed)
.hidden
some/folder/thing/untracked.md"""


def test_git_status_committed():
    expected = ["Staged", "modified:   ma/path/to/staged.md", "Not staged", "modified:   a_modified_file",
                "modified:   path/to/a_modified_file"]
    lines = modified_staged.split('\n')
    lines.reverse()
    results = parse_output(lines)
    assert results == expected


various_staged = """On branch my-branchie
Changes to be committed:
(use "git restore --staged <file>..." to unstage)
renamed:   ma/path/to/staged.md -> ma/path/to/staged-test.md
added: ma/new/file.py
removed: ma/deleted/file.py

Changes not staged for commit:
(use "git add <file>..." to update what will be committed)
(use "git restore <file>..." to discard changes in working directory)
removed:   a_modified_file
modified:   path/to/a_modified_file

Untracked files:
(use "git add <file>..." to include in what will be committed)
.hidden
some/folder/thing/untracked.md"""


def test_git_status_staged_renamed_added_removed():
    expected = ["Staged", "renamed:   ma/path/to/staged.md -> ma/path/to/staged-test.md", "added: ma/new/file.py",
                "removed: ma/deleted/file.py", "Not staged", "removed:   a_modified_file",
                "modified:   path/to/a_modified_file"]
    lines = various_staged.split('\n')
    lines.reverse()
    results = parse_output(lines)
    assert results == expected


no_staged_changes = """On branch my-branchie
Your branch is ahead of 'origin/master' by 2 commits.
  (use "git push" to publish your local commits)

Changes not staged for commit:
(use "git add <file>..." to update what will be committed)
(use "git restore <file>..." to discard changes in working directory)
modified:   a_modified_file
modified:   path/to/a_modified_file

Untracked files:
(use "git add <file>..." to include in what will be committed)
.hidden
some/folder/thing/untracked.md"""


def test_git_status_committed_no_staged_changes():
    expected = ["No staged files", "Not staged", "modified:   a_modified_file", "modified:   path/to/a_modified_file"]
    lines = no_staged_changes.split('\n')
    lines.reverse()
    results = parse_output(lines)
    assert results == expected


no_changes = """On branch my-branchie
Your branch is ahead of 'origin/master' by 2 commits.
  (use "git push" to publish your local commits)

Untracked files:
(use "git add <file>..." to include in what will be committed)
.hidden
some/folder/thing/untracked.md"""


def test_git_status_committed_no_changes():
    expected = ["No staged files", "No unstaged files"]
    lines = no_changes.split('\n')
    lines.reverse()
    results = parse_output(lines)
    assert results == expected
