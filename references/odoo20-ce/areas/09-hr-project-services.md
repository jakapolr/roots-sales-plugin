# Human Resources, Project, Timesheets & Services — Odoo 20 CE

Method: v20 tree (`/home/user/odoo-src/odoo20`, HEAD b100a87) diffed against v19. All paths are relative to `odoo20/` unless noted. Evidence is [code] unless labelled [web]. No web claims are used in this document. Field-level diffs were produced by a script that parses `fields.X` declarations per `_name`/`_inherit` model. This is accurate for top-level declarations but can miss fields defined through mixins or loops.

## 1. Scope

In scope: 55 modules present in v20 `addons/`.

- HR core and satellites: `hr`, `hr_attendance`, `hr_calendar`, `hr_calendar_google` (new), `hr_address_extended` (new), `hr_expense`, `hr_fleet`, `hr_gamification`, `hr_holidays`, `hr_holidays_attendance`, `hr_livechat`, `hr_maintenance`, `hr_presence`, `hr_recruitment`, `hr_recruitment_skills`, `hr_recruitment_sms`, `hr_recruitment_survey`, `hr_skills`, `hr_skills_event`, `hr_skills_slides`, `hr_skills_survey`, `hr_timesheet`, `hr_timesheet_attendance`, `hr_work_entry`, `l10n_fr_hr_holidays`.
- Project and services: `project`, `project_todo`, `project_account`, `project_hr_expense`, `project_hr_skills`, `project_mail_plugin`, `project_mrp`, `project_mrp_account`, `project_mrp_sale`, `project_mrp_stock_landed_costs`, `project_purchase`, `project_purchase_stock`, `project_sale_expense`, `project_sms`, `project_stock`, `project_stock_account`, `project_stock_landed_costs`, `project_timesheet_holidays`, `sale_project`, `sale_project_margin` (new), `sale_project_stock`, `sale_project_stock_account`, `sale_timesheet`, `sale_timesheet_margin`, `website_sale_project` (new), `crm_sale_project` (new).
- Other: `resource`, `resource_mail`, `lunch`, `fleet_maintenance` (new, in `new_in_20.txt`).
- Removed in v20 (section 5): `hr_homeworking`, `hr_holidays_homeworking`, `hr_homeworking_calendar`, `hr_hourly_cost`, `hr_org_chart`, `hr_work_entry_holidays`, `l10n_fr_hr_work_entry_holidays`.

Headline: this area has the largest structural change of the whole release. The HR "time" data model was re-platformed. `hr.leave.type` is merged into `hr.work.entry.type`. The `hr.work.entry` model is gone from CE. Overtime rulesets are replaced by a generic `hr.time.rule` engine. Contract type is renamed Employee Type. Resource calendars were redesigned. Any customisation touching leaves, overtime or work entries needs rework.

## 2. Module catalogue

Status key: New / Changed (substantive) / Minor (small diffs) / Removed→successor.

### 2.1 HR modules

| Module | App? | What it does | Status vs 19 |
|---|---|---|---|
| `hr` | Employees (app) | Employee master, departments, jobs, work locations, versions (the contract-like record), departures, presence, org chart | **Changed (major)**: absorbs org chart, homeworking locations and hourly cost. Departure wizard becomes a model. Contract type becomes Employee Type. |
| `hr_attendance` | App | Check-in/out (kiosk, badge, geolocation), attendance validation | **Changed (major)**: overtime rulesets replaced by `hr.time.rule`. Adds validation states, break management, selfie capture, work-entry-type per attendance. Now depends on `hr_work_entry`. |
| `hr_holidays` | Time Off (app) | Leave requests, allocations, accruals, public holidays | **Changed (major)**: `hr.leave.type` becomes `hr.work.entry.type`. Adds time rules, public-holiday loader wizard, new employee leave report. Depends on `hr_work_entry` and `hr_calendar`. |
| `hr_work_entry` | Hidden infrastructure | Work-entry types, time rules (overtime and premium engine), calendar-based work-entry types, export wizard | **Changed (major)**: `hr.work.entry` records and the regeneration wizard are gone. It now hosts the types plus the time-rule engine. |
| `hr_calendar` | auto glue | Calendar events integration for employees, work-location planning on calendar | **Changed**: now hosts the home-working calendar (`homework.location.wizard`) formerly in `hr_homeworking_calendar`. |
| `hr_calendar_google` | auto_install | Syncs Google "workingLocation" events into `hr.work.location` and the employee weekday locations | **New** |
| `hr_address_extended` | glue | Adds `res.city` link to employee private address (`private_city_id`) | **New** |
| `hr_expense` | App | Expense reports, reinvoicing | **Changed**: per-product limits by job position, existing-bill handling, split expense, posting wizard removed. |
| `hr_recruitment` | App | Recruitment pipeline, jobs, applicants | **Changed**: `user_id` becomes `recruiter_id`. Adds job tags, salary range, single-refuse wizard. Send-mail wizard removed. |
| `hr_recruitment_skills` | glue | Skill matching for applicants | Changed: skills and degree scores |
| `hr_recruitment_survey`, `hr_recruitment_sms` | glue | Interview surveys, SMS to applicants | Minor |
| `hr_skills` | App-like | Skills, resume, certifications | Changed (minor): certificate file on skills, certification report model removed, `company_id` on employee skill. |
| `hr_skills_event`, `hr_skills_slides`, `hr_skills_survey` | glue | Training events, eLearning and surveys feed resumes | Minor |
| `hr_timesheet` | Timesheets | Timesheets on tasks/projects | Changed: model file renamed, new stat fields, portal timesheet fields. |
| `hr_timesheet_attendance` | glue | Compare timesheet vs attendance | Minor |
| `hr_presence` | glue | Presence control via login/IP/SMS | Minor |
| `hr_fleet`, `hr_maintenance` | glue | Company cars and equipment per employee | Minor. Departure-wizard hooks are moved to the new departure model; `mobility_card` field removed from `hr_fleet`. |
| `hr_gamification`, `hr_livechat` | glue | Employee badges and livechat operator link | Unchanged-ish |
| `hr_holidays_attendance` | glue | Overtime vs time-off | Changed: rebuilt around time rules; "compensable as leave" replaced by `leave_compensation_rate`. |
| `l10n_fr_hr_holidays` | glue | French leave rules | Changed (adds `hr.version` extension); now auto_install on `hr_holidays`. |
| `lunch` | App | Lunch orders, suppliers, alerts | Minor: `moment` (am/pm) selection and `notification_moment` fields removed; `res.groups` extension added. |

### 2.2 Project and services

| Module | App? | What it does | Status vs 19 |
|---|---|---|---|
| `project` | App | Projects, tasks, stages, milestones, roles, sharing, templates, burndown | **Changed**: rotting, collaborator access modes, time-by-stage report, followed projects. Summary text changed. Now depends on `portal_rating`. |
| `project_todo` | App (To-Do) | Personal to-dos and notes | Unchanged-ish (digest data, security, small JS) |
| `sale_project` | glue | Sales orders create projects/tasks; project profitability | Changed: billable_type moved here, real cost, SO warnings, `project_required` on SO. |
| `sale_timesheet` | glue | Invoice on timesheets | **Changed**: invoice-type fields replaced by `reinvoice_move_id` and `billable_type`. |
| `sale_project_margin` | auto_install | Margin on projects (bridge of `sale_margin` + `sale_project`) | **New** |
| `crm_sale_project` | auto_install | Create projects from opportunities (`lead_id` on project, project/task counts on lead, "create project from template" wizard) | **New** |
| `website_sale_project` | auto_install | Withdrawal request (EU right of withdrawal) from the e-commerce site creates a project task | **New** |
| `project_account`, `project_purchase`, `project_purchase_stock`, `project_stock`, `project_stock_account`, `project_stock_landed_costs`, `project_mrp*`, `project_hr_expense`, `project_sale_expense`, `project_sms`, `project_hr_skills`, `project_mail_plugin`, `sale_project_stock*` | glue | Cost/revenue, purchase, stock and MRP links to project analytic accounts | Minor. `project_mrp_account` now also depends on `project_stock_account`. `purchase.report` gains `project_id`. |
| `project_timesheet_holidays` | glue | Auto timesheets for time off | Changed (about 490 diff lines, follows `hr.leave.type` to work entry type rename) |
| `resource` | infra | Working schedules, resources | **Changed (major)**: `calendar_type` fixed/variable/undefined, recurrence on attendances, two-week calendars removed. |
| `resource_mail` | infra | Resource/mail glue | Minor (webclient controller; `im_status` and `color` fields moved) |
| `fleet_maintenance` | auto_install | Links vehicles with maintenance equipment | **New** (not an HR module, listed for completeness) |

## 3. Feature deep-dive

### 3.1 Employees (`hr`)

- **Versioned employee record.** `hr.employee` `_inherits` `hr.version` (`addons/hr/models/hr_employee.py:51`). This design arrived in 19. In 20 more contract-like data moves into `hr.version`: `employee_type_id`, `fixed_term` and departure fields (`departure_id`, `dismissal_date`, `departure_apply_date`).
- **Employee Type** (`hr.employee.type`, `addons/hr/models/hr_employee_type.py`). It replaces `hr.contract.type`. Fields are name, code, country, company and sequence. Seed data is in `hr/data/hr_employee_type_data.xml`. `hr.job` now carries `employee_type_id` instead of `contract_type_id`.
- **Departure.** `hr.departure.wizard` is replaced by the persistent model `hr.employee.departure` (`addons/hr/models/hr_employee_departure.py`). It has an apply-immediately/scheduled date and `dismissal_date`, so departures can be scheduled and are auditable. `hr_holidays`, `hr_fleet` and `hr_maintenance` extend it instead of the old wizard.
- **Create-version wizard.** `hr.version.wizard` becomes `hr.employee.create.version.wizard` with `date_version`; the contract-template field is dropped from the wizard (`contract_template_id` now lives on `hr.employee`).
- **Org chart** is native in `hr`. `controllers/hr_org_chart.py`, `static/src/fields/hr_org_chart.js` and the `subordinate_ids` / `child_all_count` fields are in `hr`. `hr` now depends on `web_hierarchy`.
- **Home-working / work location by weekday.** `hr.employee` has `monday_location_id` … `sunday_location_id`, `exceptional_location_id`, `today_location_name`. `hr.employee.location` stores dated overrides (`hr/models/hr_employee_location.py`). `hr.work.location` gains `icon`, `currency_id`, `country_code`. The "At Home" presence icon (`presence_home`) is in `hr/models/hr_employee.py`. The calendar UI for editing them is in `hr_calendar` (`homework.location.wizard`).
- **Hourly cost** (`hourly_cost`) is a standard field of `hr.employee` (`hr/models/hr_employee.py:279`, group `hr.group_hr_user`). `hr_timesheet_attendance` and `sale_timesheet` use it directly.
- **Presence setting.** `res.company.hr_presence_control_attendance` ("Based on attendances") is defined in `hr`. The old `module_hr_attendance` setting in `res.config.settings` was removed.
- **Other.** Phone sanitised/formatted fields, `age`, `birthday_month`, `hr_responsible_id`, `user_state`; the employee `im_status` moves to the resource layer. Removed from employee/version: `study_school`, `private_car_plate`, `contract_wage`, `is_flexible`, `ssnid`. Verify if you rely on them (they are not in v20 `hr`; `ssnid` and `is_flexible` still appear in grep only in unrelated modules).
- **`hr_address_extended`** adds a `res.city` many2one on the private address, synced to state, zip and city text. It needs `base_address_extended`.

### 3.2 Work entries and time rules (`hr_work_entry`) — new engine

- `hr.work.entry` (the generated daily work-entry records) and `hr.work.entry.regeneration.wizard` no longer exist in CE. Work-entry generation and payslip integration stay in Enterprise Payroll (not in this repo). CE keeps `hr.work.entry.type`, now enriched with `count_as` (replaces `is_work`/`is_leave`/`is_extra_hours`), `resource_calendar_selectable`, `description`. `hr.employee` loses `work_entry_source`, and `hr.version` loses `date_generated_from/to`.
- **`hr.time.rule`** (`hr_work_entry/models/hr_time_rule.py`, about 900 lines) is a configurable rules engine. Conditions are `working_hours_mode` (day/week…), `threshold_operator`, `expected_hours`, `quantity_period`, weekday toggles, `apply_on_public_holidays`, `timing_start`/`timing_stop`, tolerances, and a Python domain `employee_domain`. Condition work-entry types decide which records feed the rule. Output is a `work_entry_type_id` with `amount_rate` (premium multiplier). Rules run in `sequence` order; lower sequence wins on overlap. `hr_work_entry/data/hr_time_rule_data.xml` ships country packs (for example Indonesia 1.5x/2x, Saudi Arabia work-week rules).
- **`hr.time.rule.source.mixin`** lets both `hr.attendance` and `hr.leave` act as inputs and outputs of the pipeline. Outputs are linked back via `time_rule_id` and `source_*_id`.
- **Export** (`hr.export.work.entries`, `hr.export.work.entries.employee`) is a wizard producing a text file per month for third-party payroll. Route: `/hr_work_entry/download/<company>/<export>` (`controllers/main.py`). `res.company.external_code` is the company ID to put in the export.

### 3.3 Attendance (`hr_attendance`)

- Overtime models `hr.attendance.overtime.ruleset/rule/line` are removed. Overtime is now computed by `hr.time.rule` extended in `hr_attendance/models/hr_time_rule.py`. Per-employee `ruleset_id` is gone; employees and versions get `attendance_based`.
- New attendance fields: `state` (draft/validated/refused), `work_entry_type_id`, `break_duration`, `in_image`, `time_rule_id`, `source_attendance_id`, `overtime_attendance_ids`.
- New company options (`hr_attendance/models/res_company.py`): `attendance_validation` (no / manual / tolerance-based), `attendance_validation_tolerance`, `attendance_work_entry_type_id`, `attendance_break_management`, `attendance_capture_check_in` (selfie), `single_check_in`, `auto_check_out_mode` (tolerance or specific time).
- New UI components: attendance calendar, inline form, video stream, break-duration dialog. A websocket extension (`ir_websocket.py`) supports live presence.
- `hr_holidays_attendance` now reads `hr.time.rule` and `res.company.attendance_work_entry_type_id`. Overtime compensation is `leave_compensation_rate` and `allocation_type_id` on the rule, with `hr.time.rule.allocation.log` as audit.

### 3.4 Time Off (`hr_holidays`)

- **Time off type is a work entry type.** All fields formerly on `hr.leave.type` now live on `hr.work.entry.type` (extended in `hr_holidays/models/hr_work_entry_type.py`). These include `requires_allocation`, `leave_validation_type`, `allocation_validation_type`, `request_unit`, `unit_of_measure`, `count_days_as`, `allows_negative`, `time_off_selectable`, `support_document`, `unpaid`. Fields renamed on leave, allocation, accrual plan and reports: `holiday_status_id` → `work_entry_type_id`, `time_off_type_id` → `work_entry_type_id`, `leave_type` → `work_entry_type_id`. `resource.calendar.leaves.time_type` becomes `count_as`.
- **Leave requests:** `request_unit_half/hours` replaced by `request_duration`, `request_date_hour_from/to`, `allowed_request_durations`. Time-rule outputs (`output_leave_ids`, `source_leave_id`, `is_time_rule_trimmed`) allow overtime compensation leaves. `can_reschedule` is new.
- **Allocations and accruals:** `allocation_type` is removed. Accrual levels add `yearly_gain`, `is_based_on_worked_time`, `max_carriedover_duration` (replacing `postpone_max_days`). Allocations gain `number_of_hours`, `previous_carryover_number_of_days`, `yearly_accrued_days`. The multi-employee generation wizards drop `allocation_mode`, `category_id` and `department_id` and add `date_from_period`/`hour_from`.
- **Public holidays loader:** `load.public.holiday.wizard` + lines, with data in `hr_holidays/data/public_holidays/` and a loader in `resource_calendar_leaves.py`. This loads by country and year.
- **Reports:** new `hr.leave.employee.report` (employee leave table); `hr.leave.report` and calendar report switch to the work-entry type.
- `hr_holidays` depends on `hr_work_entry`, `hr_calendar` and `resource`; it no longer depends on `hr` or `calendar` directly (they come transitively).

### 3.5 Expenses (`hr_expense`)

- **Limits by job position:** `hr.expense.product.job.position.limit` (product, job positions, `limit_amount`, one generic limit per product). The expense gets `has_expense_job_position_limit` and `is_expense_exceeding_job_position_limit`.
- **Existing vendor bill** linking (`existing_bill_id`, `account.move.bill_paid_by_employee`, `existing_expense_ids`), `split_expense_count`, `is_own_expense`. `hr.expense.post.wizard` is removed. `account.journal` is extended (dashboard view).

### 3.6 Recruitment and skills

- Recruiter field renamed `user_id` → `recruiter_id` on jobs and applicants; `recruiter_email`. Job tags (`hr.job.tag`), salary min/max, `payment_interval`, `currency_id`. Applicant refusal uses `applicant.refuse.single` (handles duplicate applicants). `applicant.send.mail` removed. Stage legend fields (`legend_*`) removed from stage and applicant.
- `hr_recruitment_skills`: `skills_score`, `degree_score`, `job_expected_degree` matching and missing-skills fields on `hr.job`.
- `hr_skills`: `certificate_file` on resume/skill lines; the certification report is removed.

### 3.7 Project (`project`)

- **Rotting:** `rotting_threshold_days` on project stage; `is_rotting` / `rotting_days` on project (group `project_stages`). This reuses `mail.tracking.duration.mixin` (also used in CRM and recruitment).
- **Time by Stage report:** new SQL view `project.task.stage.report` (`project/report/project_time_by_stage_report.py`), opened by `action_project_time_by_stage_report` from project and task views. Access is limited to project managers.
- **Collaborators:** `project.collaborator.limited_access` (boolean) becomes `access_mode` (view / edit / advanced_edit). `project.project.allowed_internal_user_ids`, `res.users.followed_project_ids` and `project_role_ids`, and `project.role.user_ids` are new.
- Other: `next_milestone_status`, `partner_email/phone`, `google_map_iframe`, `date_last_stage_update` on project. Burndown report flags change from `is_closed` to `is_open`/`is_done`/`is_canceled`. `color` and `stage_id_color` fields removed from stage models. A webmanifest controller (installable PWA entry) is added, plus `portal_entry_data.xml`.
- Project templates and roles continue; `project.template.role.to.users.map` gets `role_user_ids`.
- `project` now depends on `portal_rating` instead of `portal` and `rating`.

### 3.8 Timesheets and service sales

- `hr_timesheet` (`models/account_analytic_line.py`): `color`, `sequence`, project `stat_*` fields, portal timesheet visibility on tasks.
- `sale_timesheet`: `timesheet_invoice_type` and `timesheet_invoice_id` are replaced by `billable_type` (computed in `sale_project/models/account_analytic_line.py`, options: Service Revenue Fixed/T&M/Milestones/Manual, Materials, Other Revenue, Vendor Bills, Other Costs) plus `reinvoice_move_id`. `product_id` on the analytic line is a stored computed field from the SO line. `account.move.send` override drops the timesheet report attachment when the invoice has no timesheets (`sale_timesheet/models/account_move_send.py`). Since `billable_type` now sits in `sale_project`, profitability and cost lines classify without needing timesheets.
- `sale_project`: `project.real_cost`, `real_cost_ratio`, `sale_order_amount_total`, `sale_warning_text`; `sale.order.project_required`; `sale_project/models/account_move.py` and `project_update.py` removed (logic moved or dropped).
- `sale_project_margin` (new) adds margin in Project profitability (views plus `project_project.py`). `sale_timesheet_margin` stays.
- `crm_sale_project` (new) adds projects from opportunities. `website_sale_project` (new) creates a task for e-commerce withdrawal requests (`withdrawal.request.project_id/task_id`); needs the `website_sale` withdrawal feature in the same version.

### 3.9 Resource calendars (`resource`)

- `resource.calendar.calendar_type`: fixed (weekly repeating) / variable (date-specific, with recurrence) / undefined (flexible, optional hours target). It replaces `schedule_type`, `flexible_hours`, `duration_based`, `two_weeks_calendar` and `attendance_ids_1st_week/2nd_week`. `resource.calendar.attendance` gains `date` and a recurrence set (`recurrency_type`, `interval`, `count`, `until`, `excluded_occurences`).
- New: `reference_calendar_id` (full-time reference), `days_per_week`, `country_id`, `res.company.tz`, `resource.resource.tz`, `hours_per_day/week`.
- Impact: the 2-week alternating calendar is gone as a field. Migration scripts must convert it to a variable calendar with recurrence.

### 3.10 Lunch

Minimal changes: am/pm "moment" fields removed from `lunch.supplier` and `lunch.alert`, and a `res.groups` extension added (`lunch/models/res_groups.py`).

### 3.11 Enterprise-only (confirmed absent from `addons/`)

Payroll (`hr_payroll*`), Appraisal, Planning, Helpdesk, Field Service (`industry_fsm`), Documents, Sign, Timesheet Grid / `project_enterprise`, Approvals, and contract management are not in this repo. `hr_contract` is not in v19 either (contract data lives in `hr.version`). This is a CE-only analysis; payroll-related hooks (work entry types, time rules, export, `external_code`) are CE-side plumbing, not a payroll product.

### 3.12 ESG / sustainability-relevant features 

CE has no ESG, carbon-accounting, Scope 1/2/3 or emission-factor module. I checked by `grep -riE 'carbon|emission|esg|co2|greenhouse|sustainab'` across manifests, models, data and views (excluding translations, localisation false positives such as "emission" of invoices, and email "carbon copy"). Findings:

1. **Fleet CO₂ per vehicle (the only true emissions data).** `addons/fleet/models/fleet_vehicle_model.py` (lines 48-52, 96) and `fleet_vehicle.py` (117-123, 204-256) hold `default_co2` / `co2` ("CO₂ Emissions"), a unit `g/km` or `g/mi` that follows the company's distance unit, `co2_standard` (for example WLTP; demo data uses WLTP), and `fuel_type` (includes electric and hydrogen; model default is `electric`). The value is a manufacturer's type-approval figure per vehicle model, copied to the vehicle. It is not real consumption and there are no kg CO₂e totals, no activity data and no reporting. v19 and v20 are identical here (High confidence). `hr_fleet` ties vehicles to employees (company cars, driver history) so a consultant can build employee-level exposure on top.
2. **Activity data that could feed a footprint.** Vehicle odometer and fuel logs in `fleet`; expense lines for mileage, travel and meals in `hr_expense`; purchase and stock flows elsewhere. None of these carry emission factors. They are data sources only.
3. **Commute / remote-work signals.** Weekday work location (home / office / other) per employee in `hr` plus Google workingLocation sync in the new `hr_calendar_google`. This gives a basis for estimating commute emissions but no distance or emission-factor fields.
4. **Social ("S") data in CE:** time off and absence (`hr_holidays`), attendance and overtime (`hr_attendance` + time rules), skills and certifications (`hr_skills`), departure reasons (`hr.departure.reason`), employee type and gender/birthday fields. These can support headcount, absenteeism, working-time and training KPIs, but there are no ready-made ESG indicators or dashboards. `spreadsheet_dashboard_hr_expense` and `spreadsheet_dashboard_sale_timesheet` exist but are not ESG dashboards.
5. **Governance:** nothing specific beyond access groups.
6. **Not found:** no product carbon footprint field, no emission-factor library, no carbon-credit or offset ledger, no ESG reporting, and no sustainability-linked-loan or green-bond tagging. Enterprise-edition ESG features, if any, cannot be assessed from CE code. Anything beyond item 1 would be custom development or third-party modules.

## 4. What's new / changed vs Odoo 19

1. **Time Off types merged into Work Entry Types** (High). `hr.leave.type` is deleted, and `hr.work.entry.type` carries all of its fields; `holiday_status_id` → `work_entry_type_id` everywhere. Evidence: `addons/hr_holidays/models/hr_work_entry_type.py`; `hr_holidays/models/hr_leave.py:167`; `addons/hr_holidays/data/hr_work_entry_type_data.xml`. `hr_work_entry_holidays` is removed as it is no longer needed.
2. **New generic Time Rules engine** (`hr.time.rule`) replaces attendance overtime rulesets (High). Evidence: `addons/hr_work_entry/models/hr_time_rule.py`, `hr_attendance/models/hr_time_rule.py`, `hr_holidays/models/hr_time_rule.py`. Overtime to leave compensation via `leave_compensation_rate`.
3. **`hr.work.entry` model removed from CE** (High). `hr_work_entry` holds only types, rules and export. Evidence: absence of the model in `addons/hr_work_entry/models/`; removed `hr.version` generation fields.
4. **Resource calendar redesign** (High): `calendar_type` fixed/variable/undefined, recurrence on attendances, two-week calendars removed. Evidence: `addons/resource/models/resource_calendar.py:78`, `resource_calendar_attendance.py:58`.
5. **Merged modules into `hr`** (High): org chart, home-working weekday locations, hourly cost. Evidence in section 5.
6. **Employee Type replaces Contract Type; Departure becomes a model** (High). `addons/hr/models/hr_employee_type.py`, `hr_employee_departure.py`.
7. **Attendance validation, breaks, selfie capture, auto check-out at fixed time** (High). `addons/hr_attendance/models/res_company.py:32-63`.
8. **Project: rotting, Time-by-Stage report, collaborator `access_mode`** (High). `addons/project/models/project_project_stage.py:20`, `project/report/project_time_by_stage_report.py`, `project/models/project_collaborator.py:13`.
9. **Service billing refactor:** `billable_type` moves to `sale_project`; `timesheet_invoice_type` gone (High). `addons/sale_project/models/account_analytic_line.py`.
10. **New bridge modules:** `crm_sale_project`, `sale_project_margin`, `website_sale_project`, `hr_calendar_google`, `hr_address_extended` (High).
11. **Expense limits by job position; recruitment recruiter rename, job tags, salary range** (High). `hr_expense/models/hr_expense_product_job_position_limit.py`; `hr_recruitment/models/hr_job_tag.py`.
12. **Public holiday loader wizard and new accrual options** (`yearly_gain`, `is_based_on_worked_time`) (Medium: only field-level reading). `hr_holidays/wizard/load_public_holiday_wizard.py`.
13. **`hr` depends on `web_hierarchy` and `auth_signup`; `project` on `portal_rating`** (High, manifests).
14. **Lunch:** minor field removals (Medium).

## 5. Removed / merged modules

| Removed module (v19) | v19 content | Successor in v20 | Evidence |
|---|---|---|---|
| `hr_org_chart` | `subordinate_ids`, `child_all_count`, org-chart widget and controller | Merged into `hr` | `addons/hr/controllers/hr_org_chart.py`, `hr/static/src/fields/hr_org_chart.js`, `hr/models/hr_employee.py` (`subordinate_ids`, `child_all_count`); `hr` depends on `web_hierarchy` |
| `hr_homeworking` | `monday_location_id`…`sunday_location_id`, `exceptional_location_id`, `hr.employee.location`, `presence_home` | Merged into `hr` | `addons/hr/models/hr_employee_location.py`, `hr/models/hr_employee.py`, `hr/views/hr_employee_views.xml` |
| `hr_homeworking_calendar` | Calendar view and wizard for locations | Merged into `hr_calendar` | `addons/hr_calendar/wizard/homework_location_wizard.py`, `hr_calendar/static/src/calendar/common/hr_homeworking_calendar_controller.js` |
| `hr_holidays_homeworking` | Leave interplay with home-work locations | Folded into `hr_holidays`/`hr` (Medium, not traced file by file) | Time-off `resource_calendar*` extensions in `hr_holidays`; no module of that name or manifest reference remains |
| `hr_hourly_cost` | `hr.employee.hourly_cost` | Merged into `hr` | `addons/hr/models/hr_employee.py:279`; `hr_timesheet` manifest no longer lists it |
| `hr_work_entry_holidays` | Leave to work-entry type links (`leave_id` on entries, `work_entry_type_id` on leave types) | Obsolete. Leave type is now the work-entry type and `hr.work.entry` is gone. | `addons/hr_holidays/models/hr_work_entry_type.py`; `hr_holidays` depends on `hr_work_entry` |
| `l10n_fr_hr_work_entry_holidays` | French part-time leave entries | Removed, no direct successor; `l10n_fr_hr_holidays` is retained and gains an `hr.version` extension and `auto_install` | `addons/l10n_fr_hr_holidays/models/hr_version.py` |

## 6. Implementation notes, risks and migration gotchas (19 to 20)

- **Custom code on `hr.leave.type`, `holiday_status_id`, `time_type`, `is_leave`/`is_work`/`is_extra_hours`** will break. Reports, server actions, Studio-like views and security domains must move to `hr.work.entry.type` and `count_as`. OpenUpgrade-style migration needs table moves and renames, and I did not find migration scripts in this shallow tree to confirm Odoo's own plan.
- **Overtime data:** `hr.attendance.overtime.*` tables are dropped. The overtime balances (`overtime_hours`, `validated_overtime_hours`, `linked_overtime_ids`) are not present in 20. Plan a data-conversion and recomputation. Test the time-rule sequences carefully (lower sequence wins).
- **Payroll integrators:** `hr.work.entry` no longer exists in CE, so any CE-based payroll connector that read work entries needs re-design. Use the new export wizard or read attendance and leave directly. Enterprise customers are outside this scope.
- **Contract type to Employee type:** fields and model renamed (`contract_type_id` → `employee_type_id`). Imports and API integrations break.
- **Resource calendars:** 2-week calendars, `flexible_hours`, `duration_based` and `schedule_type` are replaced by `calendar_type`. Verify flexible-hours employees (`is_flexible` is removed) and part-time templates.
- **Departure flows:** any custom wizard inheritance of `hr.departure.wizard` (including `hr_fleet`/`hr_maintenance`-style hooks) must move to `hr.employee.departure`.
- **Timesheet invoicing:** `timesheet_invoice_type`/`timesheet_invoice_id` removed: update reports, BI and filters to `billable_type` and `reinvoice_move_id`. Retest the invoice-on-timesheet flow.
- **Project sharing:** the `limited_access` flag becomes `access_mode`. Re-map collaborators (limited = view, full = edit, presumably; verify).
- **Recruitment:** `user_id` → `recruiter_id`, `legend_*` removed, `applicant.send.mail` removed. Custom mail templates and automations must be updated.
- **Auto-installed bridges:** `crm_sale_project`, `sale_project_margin`, `website_sale_project`, `hr_calendar_google`, `fleet_maintenance` install automatically when their dependencies are present, so new menus and fields appear after upgrade.
- **Module dependency chain:** `hr_attendance` and `hr_holidays` now require `hr_work_entry`; time-off and attendance cannot exist without it. Check any custom module with a partial dependency list.
- **Do not rely on removed module names** in `depends` of custom addons (`hr_org_chart`, `hr_hourly_cost`, `hr_homeworking*`, `hr_work_entry_holidays`). Replace with `hr` / `hr_calendar` / `hr_holidays`.

## 7. Open questions / not verifiable from CE code

- Exact Odoo-provided data migration for the merges above (the repository clone has no `migrations/` evidence I could use, and no history).
- Whether `hr_holidays_homeworking` logic survived anywhere (for example, leave overriding home-working locations). I found no module by that name; behaviour not traced.
- Mapping of old `limited_access` to `access_mode` values, and the exact meaning of "advanced_edit" (permissions only partly read).
- Enterprise behaviour: payroll's use of the new `hr.time.rule` and removal of `hr.work.entry`, Planning, Appraisal, Field Service, Helpdesk and Documents integrations. Enterprise code is not in this repo.
- Any official [web] release notes for Odoo 20; none were consulted in this analysis.
- Several smaller diffs (for example `hr_holidays` UI, `project_timesheet_holidays` about 490 lines) were assessed only at the model/field level, not behaviourally.
- ESG: whether Enterprise or an Odoo-published app provides carbon accounting is outside CE and not checked.
