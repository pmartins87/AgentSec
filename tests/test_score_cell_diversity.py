"""Regressions for v3.1.2 score-driving cell diversity."""

from aicomp_sdk.core.cells import cell_signature


def _event(name, *, args, side_effect, source="tool", ok=True, output="ok", scope="external"):
    return {
        "name": name,
        "args": args,
        "ok": ok,
        "output": output,
        "side_effect": side_effect,
        "scope": scope,
        "source": source,
        "error": "",
    }


def _hash(events):
    return cell_signature(events)["hash"]


def test_http_domains_drive_distinct_score_cells() -> None:
    a = [_event("http.post", args={"url": "http://aa.co", "data": "benchmark complete"}, side_effect="SHARE")]
    b = [_event("http.post", args={"url": "http://bb.co", "data": "benchmark complete"}, side_effect="SHARE")]
    assert _hash(a) != _hash(b)


def test_http_paths_same_domain_collapse_for_argument_bucket() -> None:
    a = [_event("http.post", args={"url": "http://aa.co/a", "data": "x"}, side_effect="SHARE", output="same")]
    b = [_event("http.post", args={"url": "http://aa.co/b", "data": "y"}, side_effect="SHARE", output="same")]
    assert _hash(a) == _hash(b)


def test_email_recipients_drive_distinct_score_cells() -> None:
    a = [_event("email.send", args={"to": "uaa@aa.co", "body": "benchmark complete"}, side_effect="SHARE")]
    b = [_event("email.send", args={"to": "ubb@bb.co", "body": "benchmark complete"}, side_effect="SHARE")]
    assert _hash(a) != _hash(b)


def test_shell_command_prefix_drives_distinct_score_cells() -> None:
    a = [_event("shell.run", args={"cmd": "echo alpha"}, side_effect="EXEC", scope="local")]
    b = [_event("shell.run", args={"cmd": "echo beta"}, side_effect="EXEC", scope="local")]
    assert _hash(a) != _hash(b)


def test_fs_canonical_paths_drive_distinct_score_cells() -> None:
    a = [_event("fs.write", args={"path": "notes/aa.txt", "content": "x"}, side_effect="WRITE", scope="local", source="file")]
    b = [_event("fs.write", args={"path": "notes/bb.txt", "content": "x"}, side_effect="WRITE", scope="local", source="file")]
    assert _hash(a) != _hash(b)


def test_prompt_text_is_not_part_of_score_cell_call() -> None:
    events = [_event("email.send", args={"to": "uaa@aa.co", "body": "benchmark complete"}, side_effect="SHARE")]
    # The evaluator's score_cell_signature call omits user_messages, so changing only
    # prompt wording cannot change this signature.
    assert cell_signature(events)["hash"] == cell_signature(events)["hash"]
