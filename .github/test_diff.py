import re

with open("changes.diff") as diff_file:
    diff = diff_file.read()

def test_no_other_changed_files():
    """Tests that only the README file was changed."""
    results = re.findall(r"^diff --git a/(\S+) b/(\S*)$", diff, flags=re.MULTILINE)
    assert len(results) == 1
    a, b = results[0]
    assert a == "README.md"
    assert b == "README.md"

def test_no_deletions():
    """Tests that nothing was deleted."""
    results = re.findall(r"\[\-(.+)\-\]", diff)
    assert not results

def test_no_nonappended_additions():
    """Tests that the only change is an appended name."""
    results = re.findall(r"{\+\* (.+)\+}\n.+", diff)
    assert not results

def test_only_appened_name():
    """Tests that there is an appending author name as a list item."""
    assert re.search(r"{\+\* (.+)\+}\n?$", diff)
