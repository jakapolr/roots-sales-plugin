# Product → Target Bucket Mapping (verified)

แปลงผลจาก `read_group` (group by product) เป็น target bucket — verify กับ Sheet แล้วตรงทุกบาท (Jan 2026)

## แมปตาม Product Category (`product_id.categ_id`)

| Odoo category (`complete_name`) | categ id | → Target bucket |
|---|---|---|
| All / Saleable / Implementation Services | 7 | Implementation + Gov |
| All / Saleable / Maintenance Agreement | 10 | Maintenance Agreement |
| All / Saleable / Cloud Services | 9 | Cloud |
| All / Saleable / Software Licenses | 11 | *(แยกระดับ product — ดูด้านล่าง)* |
| All / Saleable / Training | 16 | Training |
| All / Saleable / Hardwares | 8 | Hardware *(adjustment — ไม่มี target)* |
| All / Saleable / Special Discount | 14 | Special Discount *(adjustment — ติดลบ)* |
| All / Saleable / Affiliate | 15 | *(ไม่มี target)* |
| All / Saleable / BEECY | 13 | **ตัดออก** (ระบบอื่น) |
| All / Saleable / Others | 12 | review case-by-case |

## กฎพิเศษ — Software Licenses แยก 2 bucket

category "Software Licenses" รวม แต่ target แยก Odoo vs Other:

| Product | → Bucket |
|---|---|
| Odoo Enterprise License | Odoo License |
| Google Workspace License + อื่น ๆ | Other License |

## Products ที่ verify แล้ว (จากข้อมูลจริง YTD 2026)

| product (id) | category | bucket | YTD price_subtotal |
|---|---|---|---|
| Odoo Implementation Services (1) | Implementation Services | Implementation + Gov | 7,405,544.86 |
| Non-ERP Implementation Services (38) | Implementation Services | Implementation + Gov | 19,800.00 |
| Data Migration Services (48) | Implementation Services | Implementation + Gov | 10,000.00 |
| [MA] Maintenance Agreement (40) | Maintenance Agreement | Maintenance Agreement | 2,789,216.96 |
| [Cloud] Cloud Managed Service (5) | Cloud Services | Cloud | 961,950.25 |
| Odoo Enterprise License (2) | Software Licenses | Odoo License | 160,822.55 |
| Google Workspace License (37) | Software Licenses | Other License | 60,782.40 |
| [DEFAULT48] Hardware (52) | Hardwares | Hardware (adj) | 29,001.00 |
| Special Discount (67) | Special Discount | Special Discount (adj) | −41,399.96 |

## วิธีดึง category ของ product (ถ้าเจอ product ใหม่)

`read_group` คืน `product_id` — ถ้าไม่แน่ใจ bucket ให้เช็ค category:
```bash
odoo search read product.product --domain '[["id","=",<product_id>]]' --fields name,categ_id
```
แล้วแมปตามตารางบนสุด หากเจอ product ใหม่ที่ยังไม่อยู่ในตาราง ให้แจ้ง user เพื่อเพิ่มลง map
