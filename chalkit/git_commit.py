import subprocess


def git_commit(commit_message, path):
    try:
        subprocess.Popen(
            f'git add -A && git commit -m "{commit_message}"', shell=True, cwd=path
        )
    except Exception as e:
        return e
