# Benchmark Utility Task: MkDocs Documentation Update

Complete a documentation maintenance task.

1. Validate the repository.
2. Add a new section to `docs/runbooks/troubleshooting.md` describing how to check broken navigation references.
3. Ensure `mkdocs.yml` still references existing files.
4. Build the site if dependencies are installed.

Success criteria:

- `make validate` succeeds.
- The troubleshooting page contains the new section.
- No unrelated files are modified.
