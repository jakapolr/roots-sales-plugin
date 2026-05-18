# Skill Template

โฟลเดอร์นี้เป็น **template สำหรับสร้าง custom skill ใหม่** — ไม่ใช่ skill ที่ใช้งานได้

วางไว้ใน `docs/` โดยตั้งใจ เพื่อไม่ให้ Claude Code scan เป็น skill จริง
(Claude Code โหลด skill จาก `skills/` และเฉพาะไฟล์ชื่อ `SKILL.md` เท่านั้น)

## วิธีสร้าง skill ใหม่

1. คัดลอกโฟลเดอร์นี้ไป `skills/[ชื่อ-skill-ใหม่]/`
2. เปลี่ยนชื่อ `TEMPLATE.md` เป็น `SKILL.md`
3. แก้ frontmatter — `name` ต้องตรงกับชื่อโฟลเดอร์
4. ลบ comment block ด้านบน (บรรทัดที่ขึ้นต้นด้วย `#`) ออกเมื่อแก้เสร็จ
5. commit + push — ทีมรัน `claude plugin update` ก็ได้ skill ใหม่

ดูตัวอย่าง skill ที่ Roots สร้างเอง: `skills/odoo-gap-analysis/`, `skills/roots-tor-analyzer/`
