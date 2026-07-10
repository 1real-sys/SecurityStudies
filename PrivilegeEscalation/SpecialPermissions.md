# Special Permissions

The Set User ID upon Execution (`setuid`) permission can allow a user to execute a program with the effective permissions of the file owner (often `root`). On Linux, this special bit appears as `s` in the owner's execute position.

## Enumerating setuid binaries

```bash
JLMreal@htb[/htb]$ find / -user root -perm -4000 -exec ls -ldb {} \; 2>/dev/null
```

```text
-rwsr-xr-x 1 root root 16728 Sep  1 19:06 /home/htb-student/shared_obj_hijack/payroll
-rwsr-xr-x 1 root root 16728 Sep  1 22:05 /home/mrb3n/payroll
-rwSr--r-- 1 root root 0 Aug 31 02:51 /home/cliff.moore/netracer
-rwsr-xr-x 1 root root 40152 Nov 30  2017 /bin/mount
-rwsr-xr-x 1 root root 40128 May 17  2017 /bin/su
-rwsr-xr-x 1 root root 27608 Nov 30  2017 /bin/umount
...SNIP...
```

## Deep dive: setuid details that matter

1. **`s` vs `S`**  
   `-rwsr-xr-x` means setuid is set and executable by owner.  
   `-rwSr--r--` means setuid is set, but owner execute bit is missing (uppercase `S`), so it is usually not directly executable.
2. **Real UID vs Effective UID**  
   With setuid binaries, your real user stays the same, but the process effective UID becomes the file owner. Most privilege abuse depends on this effective UID behavior.
3. **Scripts vs binaries**  
   Modern Linux kernels generally ignore setuid on scripts for security reasons, but setuid on ELF binaries is still fully relevant.
4. **Risk indicators**  
   Non-standard/custom binaries in home folders, writable paths, unsafe library loading, shell escapes, or command execution features are strong escalation candidates.

It may be possible to reverse engineer a setuid program, identify unsafe behavior (for example, insecure `system()` usage, PATH trust, library loading, or command injection), and escalate privileges.

---

The Set Group ID (`setgid`) permission allows executing a binary with the effective group ID of the file group owner. It also has a directory behavior: files created inside a setgid directory inherit the directory group.

## Enumerating setgid binaries

```bash
JLMreal@htb[/htb]$ find / -user root -perm -6000 -exec ls -ldb {} \; 2>/dev/null
```

```text
-rwsr-sr-x 1 root root 85832 Nov 30  2017 /usr/lib/snapd/snap-confine
```

## Deep dive: setgid details that matter

1. **setgid on files** gives process group privileges that can unlock restricted files, sockets, or service-owned resources.
2. **setgid on directories** is often legitimate for collaboration, but dangerous when combined with weak write permissions and privileged automation.
3. **Attack paths** often involve group-owned scripts, log files, sockets, or IPC resources writable by unintended users.

---

## GTFOBins

The GTFOBins project is a curated list of Unix binaries that can be abused for:

- Privilege escalation
- Restricted shell escape
- File read/write
- Command execution
- Reverse/bind shell behavior (context dependent)

Each GTFOBins entry maps abuse techniques to specific contexts (for example: normal execution, `sudo`, SUID, or capabilities).  
This context is critical: a trick that works with `sudo` may not work without `sudo`.

### Practical GTFOBins triage workflow

1. Enumerate candidate binaries (`sudo -l`, SUID list, capabilities, PATH tools).
2. Cross-check each candidate on GTFOBins by exact binary name.
3. Match the right abuse context (`sudo`/SUID/capabilities).
4. Validate constraints (absolute path enforcement, noexec mounts, environment sanitization, version differences).
5. Use the minimum technique needed to gain stable elevated access.

For example, `apt-get` can be abused (in some contexts) to spawn a shell by adding a pre-invoke command:

```bash
JLMreal@htb[/htb]$ sudo apt-get update -o APT::Update::Pre-Invoke::=/bin/sh
```

```bash
# id
uid=0(root) gid=0(root) groups=0(root)
```

Familiarity with GTFOBins dramatically speeds up privilege escalation triage during assessments because it helps quickly separate low-value binaries from realistic escalation paths.