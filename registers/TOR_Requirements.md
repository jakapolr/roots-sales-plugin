# Register — TOR_Requirements (Compliance Matrix)

> **Location:** Google Drive → `8. Sales and Marketing/TOR Factory/registers/TOR_Requirements.md`
> **Maintained by:** `roots-compliance-matrix`
> **Purpose:** The compliance matrix — every TOR requirement as a row with owner,
> evidence, and response status. **This is the G2 control: no proposal drafting until
> every mandatory/pass-fail row has a response and the matrix is frozen.**

## How to Use

- One section of the file per `tor_id` (or filter the table by `tor_id`).
- `roots-compliance-matrix` decomposes the TOR and appends rows.
- `roots-evidence-matcher` fills `evidence_link`; owners update `response_status`.
- `tor-qa-reviewer` reads this to verify 100% coverage before G4.

---

## Registry

| req_id | tor_id | section | requirement | type | mandatory | weight | owner | evidence_link | response_status | risk |
|---|---|---|---|---|---|---|---|---|---|---|
| REQ-001 | TOR-2026-001 | คุณสมบัติผู้ยื่น | จดทะเบียนนิติบุคคล ≥ 5 ปี | legal | yes | — | Admin | Company_Documents#affidavit | ready | 🟢 |
| REQ-002 | TOR-2026-001 | เทคนิค | ระบบรองรับ IFRS | scored | no | 10 | SE | Needs human review | open | 🟡 |

---

## Field Reference

| Field | Description | Example |
|---|---|---|
| `req_id` | Sequential per TOR, `REQ-NNN` | REQ-001 |
| `tor_id` | Parent TOR | TOR-2026-001 |
| `section` | TOR section the requirement came from | คุณสมบัติผู้ยื่น |
| `requirement` | Original requirement text (verbatim, do not paraphrase away meaning) | จดทะเบียนนิติบุคคล ≥ 5 ปี |
| `type` | mandatory-passfail / scored / commercial / legal / presentation / delivery | scored |
| `mandatory` | yes / no (pass-fail disqualifier?) | yes |
| `weight` | Scoring weight if `type=scored`, else `—` | 10 |
| `owner` | Roots person responsible for the response | SE |
| `evidence_link` | Pointer to evidence (register#anchor or Drive link), or `Needs human review` | Company_Documents#affidavit |
| `response_status` | open / drafting / ready / waived | ready |
| `risk` | 🟢 OK / 🟡 WARN / 🔴 RISK (disqualifier or gap) | 🟡 |

---

## Statistics

> Auto-updated by `roots-compliance-matrix` on each write.

- Requirements logged: 2
- By type: legal 1, scored 1
- Coverage (ready / total): 1 / 2
- Open 🔴 risks: 0
- Last updated: 2026-05-29
