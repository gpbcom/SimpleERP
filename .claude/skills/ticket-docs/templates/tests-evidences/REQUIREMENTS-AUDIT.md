# 🔬 <KEY> — Requirements audit on <stage>: develop vs this branch

> **Question:** <the question the audit answers, in the reader's words: are the ticket's requirements enforced on real data, and is what users see right? Quote the QA or review comment that prompted it, if any>
>
> **Date:** <DATE> · **Stage:** <🟦 dev / 🟪 qa> · **Data:** <the seeded data set used> · **Branch:** `<commit>` (<rebased on develop x.y.z>) · **Master:** `<commit>` (<x.y.z>) · **Front:** <xsa-web commit, or "not concerned: no screen shows this data">

**Legend:** 🟢 requirement met · 🟠 met but misleading or partial · 🔴 not met · 🟡 met by instruction only (prompt, convention) · ⚪ not live (cannot happen on real data; unit tests only) or no difference

---

## 🧭 Verdict at a glance

| Layer | Verdict | In one line |
|---|---|---|
| 🛠️ **Back end** (<stack>) | <🟢 / 🟠 / 🔴> **<verdict>** | <n / n sections, records or calls pass every rule of the ticket> |
| 🖥️ **Front end** (<app>) | <🟢 / 🟠 / 🔴 / ⚪ not concerned> **<verdict>** | <what users see, measured on the real bodies> |
| 🤖 **AI features** | <🟢 / 🟡 / 🔴 / ⚪ not concerned> **<verdict>** | <what the prompts read, and what guards them> |
| 🔌 **Contract** (exposed and called APIs) | <🟢 / 🔴> **<verdict>** | <statuses, fields, enums as EXPLAIN §3.1 states them> |
| 🔀 **Branch vs develop** | <⚪ identical / 🟢 fixed / 🔴 regressed> | <n / n differences, and which ones are the ticket's> |

### 🎯 Answer

- <The answer to the question above, in two or three bullets: which layer, why, and whether this ticket's own requirements are met.>

<Optional diagram of the verdict flow: a PNG in `diagrams/`, embedded as an image, with its SVG and Mermaid source linked under it.>

---

## 🧪 What was run

| # | Test | Scope | Where | Result |
|---|---|---|---|---|
| T1 | <🟦 collection / calls on the stage running **develop**> | <n records> | <stage, develop deployed when> | <🟢 n / n> |
| T2 | <🟦 deploy of the branch (Actions run #…)> | stack, unit, acceptance | <stage> | <🟢 / ⚠️ with the reason> |
| T3 | <🟦 the same collection / calls on the stage running **the branch**> | <n records> | <stage> | <🟢 n / n> |
| T4 | <🔎 rules per record (`scripts/analyze.py`)> | <n> | local, on T1 + T3 | <🟢 0 failure> |
| T5 | <🔀 develop vs branch, record by record> | <n pairs> | local | <⚪ 0 difference / list> |
| T<n> | <📡 the upstream system's own answer (the truth the ticket's rules are checked against)> | <n> | <API, stage> | <🟢 used as reference> |
| T<n> | <🖥️ the front rendered with the real bodies / driven in a browser> | <n cards or screens> | <app commit> | <🟢 / 🔴> |
| T<n> | <🤖 the prompts: what they read> | <n features> | code | <🟢 / 🟡> |
| T<n> | <💻 unit suite on the final commit> | <n tests> | local | <🟢 n / 0> |

---

## 🛠️ 1. Requirements — every rule of the ticket on real data

Every topic (T…) and acceptance criterion (AC…) of [TICKET.md](../../TICKET.md) has a row, out-of-scope ones included (🚫, with their Dn).

| Requirement (TICKET.md) | Check | <🟦 develop> | <🟦 branch> | Evidence |
|---|---|---|---|---|
| **<AC1 / T1>** <the rule, in one line> | <how it is checked on real data> | <🟢 n / n> | <🟢 n / n> | <file or folder> |
| **<ACn>** <a rule that cannot happen on the stage> | <why not live> | ⚪ | ⚪ | <unit test IDs> |
| **Contract** <statuses, enums, shapes> | <check> | <🟢> | <🟢> | <file> |

### 🔢 Branches on real data (TEST-3)

<One row per branch of every matching, lookup, fallback or rule the ticket adds, with its live count. A branch at 0 is named "not live" here, in the PR description and in EXPLAIN §6. Write "No matching, lookup or fallback in this ticket" when there is none.>

| Branch | <dimension 1> | <dimension 2> | Note |
|---|---:|---:|---|
| <🟢 normal case> | <n> | <n> | <note> |
| <🟠 fallback> | <n> | <n> | <note> |
| <⚪ branch added by this ticket> | <0> | <0> | <never sent by the upstream on this stage → proven by unit tests …> |

### 🕰️ Before / after on the same data

| <stage> snapshot or call | <measure> | <measure> |
|---|---|---|
| <🔴 before (date, code)> | <value> | <value> |
| <🟢 after (date, code)> | <value> | <value> |

---

## 🖥️ 2. Front end — what users see

<The real GET bodies of T1 and T3 rendered with the front's own components (vitest), or the deployed front driven in a browser. One row per kind of display. Write "Not concerned: <reason>" when no screen shows the ticket's data.>

| What the screen shows | <count> | <design ticket> | <this ticket's goal> |
|---|---:|:---:|:---:|
| <display> | <n> | <🟢> | <🟢 / 🔴> |

---

## 🤖 3. AI features

<What each AI feature touched by the data reads, and what guards it: data (the field is not sent) or instruction (the prompt says to ignore it). Write "Not concerned: <reason>" when no prompt reads the ticket's data.>

| Feature | Reads the ticket's data? | Verdict |
|---|---|---|
| <feature> | <✅ / ❌ where (`file:line`)> | <🟢 / 🟡 / 🔴> |

---

## 🚩 4. Findings

Every 🔴 and 🟠 finding is fixed before the hand-over, or named in the pull request description and in EXPLAIN §6 with its owner.

| # | Sev. | Layer | Finding | Owner / next step |
|---|---|---|---|---|
| **A1** | <🔴 / 🟠 / 🟡 / ⚪> | <🛠️ back / 🖥️ front / 🤖 AI / 📚 docs / 🧰 env> | <the finding, with its count on real data> | <fixed in `<commit>` / ticket to open / product decision (who) / EXPLAIN §6 Rn> |

---

## 🧱 Limits of this audit

- <What could not be checked and why: QA account access, a front not driven in a browser, rules that never fire on real data (unit tests only).>
- 🧹 **Side effects:** <data rewritten or calls billed on the stage, and what the stage runs now.>

## 📁 Evidence

[README.md](README.md) (commands, files) · <links to every sub-folder: develop/, branch/, scripts/, front/, ai/, diagrams/…>
