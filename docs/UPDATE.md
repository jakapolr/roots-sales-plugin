# คู่มืออัปเดต Roots Sales Plugin (สำหรับทีมขาย)

> **เวอร์ชันปัจจุบัน: v3.0.0** — เพิ่มระบบ TOR Response Factory
> Marketplace: `roots-sales-plugin` · Plugin: `sales` · Repo: `jakapolr/roots-sales-plugin`

---

## สำหรับคนที่ติดตั้งปลั๊กอินอยู่แล้ว (อัปเดต)

รันใน Terminal ตามลำดับ:

```bash
# 1. ดึงข้อมูล marketplace ล่าสุดจาก GitHub
claude plugin marketplace update roots-sales-plugin

# 2. อัปเดตปลั๊กอินเป็นเวอร์ชันล่าสุด
claude plugin update sales@roots-sales-plugin

# 3. ปิดแล้วเปิด Claude Code ใหม่ (จำเป็น — ต้อง restart ถึงจะมีผล)
```

หรือทำผ่านเมนูใน Claude Code: พิมพ์ **`/plugin`** → เลือก marketplace `roots-sales-plugin` → Update

---

## สำหรับคนที่ยังไม่เคยติดตั้ง (ติดตั้งใหม่)

```bash
# 1. เพิ่ม marketplace
claude plugin marketplace add jakapolr/roots-sales-plugin

# 2. ติดตั้งปลั๊กอิน
claude plugin install sales@roots-sales-plugin

# 3. restart Claude Code
```

---

## ตรวจสอบเวอร์ชัน

```bash
claude plugin list
# ควรเห็น: sales  3.0.0  (enabled)
```

ดูรายละเอียดส่วนประกอบ (skills / agents):

```bash
claude plugin details sales
```

---

## สิ่งที่ต้องทำเพิ่มเพื่อใช้ฟีเจอร์ TOR Factory

1. **เชื่อม Google Drive** — ครั้งแรกที่เรียกใช้ skill ที่ต้องใช้ Drive ระบบจะให้ authenticate (แต่ละคนทำของตัวเอง)
2. **โฟลเดอร์กลางตั้งค่าไว้แล้ว** — `8. Sales and Marketing/TOR Factory/` พร้อมทะเบียน 10 ไฟล์ และโฟลเดอร์ `_Masters/` — ไม่ต้องสร้างเอง แค่ต้องมีสิทธิ์เข้าถึง
3. **คู่มือการใช้งาน** — เปิดไฟล์ `docs/user-manual.html` (ดับเบิลคลิกเปิดในเบราว์เซอร์)

---

## เริ่มใช้งานเร็ว

| สถานการณ์ | พิมพ์ |
|---|---|
| ไม่รู้จะเริ่มยังไง | `"ช่วยแนะนำหน่อย"` |
| มี TOR ใหม่เข้ามา | `"intake TOR [ชื่อโครงการ]"` |
| เดินงาน TOR ครบวงจร | `"orchestrate TOR [tor_id]"` |
| วิเคราะห์ว่าควรประมูลไหม | `"analyze this TOR [วาง/แนบไฟล์]"` |
| เตรียมก่อนพบลูกค้า | `"research [ชื่อบริษัท]"` |
| ทำ MOM หลังประชุม | `"ทำ MOM [วาง transcript]"` |

---

## มีปัญหา?

- คำสั่ง `claude` ไม่เจอ → ติดตั้ง Claude Code ก่อน แล้ว login (`claude` แล้วทำตามขั้นตอน)
- อัปเดตแล้วยังเห็นเวอร์ชันเก่า → ตรวจว่า restart Claude Code แล้ว และรัน `claude plugin marketplace update roots-sales-plugin` อีกครั้ง
- ติดต่อ: Petch (AI Ops Coordinator)
