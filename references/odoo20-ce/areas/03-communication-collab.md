# Communication, Collaboration & Contacts — Odoo 20 CE

All evidence is [code] from `/home/user/odoo-src/odoo20` (HEAD b100a87) diffed against `/home/user/odoo-src/odoo19`; paths are relative to `odoo20/`. No web sources were used. Confidence is marked where it is below High.

## 1. Scope

41 names were requested. 36 exist in both v19 and v20. 5 are new in v20 (`mail_tracking`, `mail_tracking_mass_mailing`, `mail_tracking_sms`, `portal_discuss`, `mysubscription`) and `hr_calendar_google` is a sixth new module listed alongside them. 2 are removed (`base_iban`, `base_vat`). Two names in the request, `im_livechat_mail_bot` and `mail_bot*` beyond `mail_bot_hr`, do not exist in either tree. Adjacent modules also read: `sms_twilio`, `hr_calendar`, `google_account`, `l10n_eu_account_vies`, `portal_rating`.

Cross-cutting change visible in almost every module: the `security/ir.model.access.csv` plus `*_security.xml` files are replaced by a single `security/ir.access.csv`. The new unified model `ir.access` (`odoo/addons/base/models/ir_access.py`) combines model access and record rules. A row with a group is a "permission" and a row without a group is a "restriction". Mail also adds `res_access_read/write/create/unlink` stored booleans on `mail.message` and `mail.activity` (`addons/mail/models/mail_message.py`, `mail_activity.py`), and `ir.access` itself is chatter-tracked (`addons/mail/models/ir_access.py`).

## 2. Module catalogue

| Module | App? | Summary | What it does | Status vs 19 |
|---|---|---|---|---|
| mail | no (Discuss) | Discussions, chatter, activities, mail gateway | Core messaging: chatter, followers, activities, templates, outgoing/incoming mail, Discuss channels/chats/RTC | Changed (large: ~1200 files differ) |
| mail_tracking | no | "Discuss Tracking": technical storage of tracked values | Owns `mail.tracking.value`, `tracking_value_ids`, and message origin (`source_template_id`, `source_view_id`) | **New** (split out of mail) |
| mail_tracking_mass_mailing | no, auto-install | Mass mailing tracking | Adds `mail.message.source_mailing_id` | **New** |
| mail_tracking_sms | no, auto-install | SMS message tracking | Adds `mail.message.source_sms_template_id` | **New** |
| mail_bot | no | OdooBot | Onboarding bot in Discuss | Changed (small refactor, new copy) |
| mail_bot_hr | no | Bridge hr/mail_bot | OdooBot state in HR user form | Unchanged-ish |
| mail_group | no | Mailing lists / forums by email | Group aliases, moderation, portal archive | Unchanged-ish (ir.access, `get_int`) |
| mail_plugin | no | Gmail/Outlook add-in backend | Partner lookup/create, log email as note | Changed (IAP enrichment removed, record search added) |
| im_livechat | app | Live Chat | Website chat widget, operators, chatbot scripts, reports | Changed (large) |
| website_livechat | no | Livechat + website | Visitor tracking, page-based rules | Changed |
| sms | no | SMS engine | Composer, templates, tracking, IAP/provider send | Changed |
| sms_twilio | no | Twilio provider | Alternative SMS provider (exists in 19 too) | Unchanged-ish |
| snailmail / snailmail_account | no | Letters via Pingen (IAP) | Send documents/invoices by post | Changed (webhook, no longer auto-install) |
| calendar | app | Calendar and meetings | Events, attendees, recurrence, alarms, availability | Changed (large: multi-calendar, sharing) |
| calendar_sms | no | SMS alarms | `sms` alarm type on events | Unchanged-ish |
| google_calendar | no | Google Calendar sync | Two-way event sync | Changed (multi-calendar sync) |
| microsoft_calendar | no | Outlook Calendar sync | Two-way event sync | Changed |
| hr_calendar_google | no, auto-install | Google working locations to employees | Imports Google "workingLocation" events into `hr.work.location` | **New** |
| google_gmail / microsoft_outlook | no | OAuth for incoming/outgoing mail servers | XOAUTH2 for Gmail and Outlook | Unchanged-ish (`get_str` refactor) |
| portal | no | Customer portal | `/my` home, chatter on portal | Changed (`portal.entry` cards, new chatter bundle) |
| portal_discuss | no, auto-install | Discuss for portal users | "Discuss" card and `/my/conversations` | **New** |
| phone_validation | no | Phone parsing, blacklist | Formatting, phone blacklist, `phone_formatted` | Changed (activity phone support) |
| contacts | app | Address book | Partner list/kanban/hierarchy | Changed (hierarchy view) |
| partner_autocomplete | no | Company autocomplete (IAP) | Autocomplete/enrich by name, VAT, DUNS | Changed |
| project_todo | app | To-Do | Personal memos/to-dos on `project.task` | Changed |
| social_media | no | Company social links | Facebook, Twitter etc. fields on company | Unchanged-ish |
| rating | no | Customer ratings | `rating.rating`, rating mixins | Changed |
| resource | no | Resources and working schedules | `resource.calendar`, leaves, attendances | Changed (major rewrite) |
| link_tracker / utm | no | Tracked links; UTM | Short URLs, clicks, UTM source/medium/campaign | Changed (`utm_reference`) |
| gamification | no | Goals, badges, karma ranks | Challenges, goals, badges | Unchanged-ish (static JS/SCSS dropped) |
| mysubscription | no, auto-install | "My Subscription" | Client-action dashboard with plan, database and IAP credits | **New** |
| base_iban / base_vat | no | IBAN and VAT validation | — | **Removed** |

## 3. Feature deep-dive

### 3.1 Discuss (module `mail`)

**Channels, chats, groups.** `discuss.channel.channel_type` has three values: `chat` (1-to-1, unique via `member_indices`), `group` (private, invitation) and `channel` (open or restricted) (`addons/mail/models/discuss/discuss_channel.py:107`). There is no `livechat` type in the base selection; livechat adds its own. Sub-threads exist through `parent_channel_id`.

New in 20 on the channel:
- `is_readonly`: only admins may post. Allowed on `channel` only (constraint at `discuss_channel.py:193`).
- Roles on membership: `discuss.channel.member.channel_role` is `owner` or `admin`. Owners manage admins, owner and admins edit the channel and members. Only for `group` and `channel`.
- `discuss.category` (new model, `models/discuss/discuss_category.py`) groups channels in the sidebar. `discuss_category_id` on the channel, kanban admin view at `static/src/views/web/discuss_category`.
- Per-member `is_favorite`, `is_unread`, `invitation_sent_dt`, `can_join`/`can_leave`/`can_unlink` computed access flags.
- `custom_channel_name` and `fetched_message_id` removed from members.
- `discuss.channel.last.interest.update` is an append-only queue for `last_interest_dt`, a write-contention optimisation.
- `bus.sync.mixin` and `bus.listener.mixin` give models real-time field sync over the bus.

**Threads and messages.**
- Polls (new): `mail.poll`, `mail.poll.option`, `mail.poll.vote` with question, options with emoji and label, multiple-choice flag, end datetime, and a winning-option compute. Votes by user or guest. Controller `controllers/poll.py` (`/mail/poll/create|end|delete|vote|remove_vote`). `mail.message` has `started_poll_ids`, `ended_poll_ids`, `has_poll`.
- Bookmarks replace stars: `starred_partner_ids`/`starred` become `bookmarked_partner_ids`/`is_bookmarked`. Pinned messages remain via `pinned_at`. `pinned_message_ids` removed from the channel, with a new `pinned_messages_panel.js`. Custom code or SQL using `starred` will break.
- Message translation: `mail.message.translation` stores translations, with Google Translate controller `controllers/google_translate.py` and an im_livechat CORS variant.
- Link previews (`mail.link.preview`, `mail.message.link.preview`), reactions, GIF picker (Tenor, `discuss.gif.favorite`), canned responses, scheduled messages (`mail.scheduled.message`, also for SMS via `sms/models/mail_scheduled_message.py`) all persist.
- CC recipients: `mail.message.partner_cc_ids`, `mail.mail.recipient_cc_ids`, `mail.template.partner_cc`, `mail.scheduled.message.partner_cc_ids`. Replaces the v19 `mail.thread.cc` mixin (`mail_thread_cc.py` deleted; `crm`, `project`, `hr_recruitment`, `maintenance` used it in 19). Gateway parsing of `partner_cc_ids` is in `mail_thread.py:1398`. `partner_ids` is relabelled "Recipients (To)".
- `mail.thread.subject.suggested` (new mixin) provides `suggestedSubject` and `showSubjectInSmallComposer` in the composer.
- A `html_composer_message_field` and `html_editor` assets suggest a richer HTML composer. Medium confidence on end-user behaviour, since only file names were seen.

**Calls / RTC.**
- Models: `discuss.channel.rtc.session`, `discuss.call.history`, `mail.ice.server` (STUN/TURN). SFU support is through `mail/static/lib/odoo_sfu`. Routes in `controllers/discuss/rtc.py`: join/leave call, notify members, upgrade connection, cancel invitation.
- Meetings: `default_display_mode='video_full_screen'` makes a channel a meeting. `meeting_start_dt`/`meeting_stop_dt` are computed on the channel. The UI has meeting, stage layouts (`call/common/stage`), "ready banner", PiP, push-to-talk extension, blur background, permission dialogs, presentation (screen share) bar.
- Recording and debrief (new): `mail.call.artifact` is one record per media artifact (offset `start_ms`/`end_ms`, non-overlapping per call, `recording_started_by_id`, `recording_upload_pending`). `discuss.call.history` gains `artifact_ids` and `has_recording/has_audio/has_video`. A "call debrief" field widget (`views/fields/call_debrief`) gives timeline and media controls.
  - The upload route `/mail/rtc/recording/<id>/routing` calls `_get_recording_destination()`, which in CE just raises `NotFound` (`controllers/discuss/rtc.py:216-225`). So CE ships the data model, UI and SFU claims, but not a working storage backend or transcription. The comment block "Recording / Transcription" and the `voip.call` mention imply Enterprise or another module supplies it. Confidence: High that CE has no backend, Medium on what supplies it.

**Voice messages.** `discuss.voice.metadata` stores metadata on voice attachments. The browser recorder (`static/src/discuss/voice_message/common/voice_recorder.js`) uses an AudioWorklet served at `/discuss/voice/worklet_processor` and lamejs for MP3 encoding. Duration is limited by a config value in minutes. No transcription found in code.

**Presence.** `mail.presence` is now a model for user and guest presence (`status`, `last_poll`, `last_presence`). `res.users.im_status` becomes a Selection and `offline_since` is added. Presence and `res.users.settings` moved to the discuss sub-package.

**AI / bots.**
- OdooBot (`mail_bot`): scripted onboarding (emoji, mention, attachment, command) plus `/help`. In v20 `mail.bot._apply_logic` takes the saved `mail.message` instead of a values dict (`addons/mail_bot/models/mail_bot.py`). `_message_post_after_hook(self, message)` lost its `msg_vals` parameter. Overrides in custom modules must be updated. Copy was rewritten and the icons moved to Material Symbols.
- AI hooks only: the CE code contains references to an Enterprise `ai` module (`messaging_menu_ui_state_model.js` mentions `"ai.agent_scope"`, `im_livechat_channel.py:409` mentions an `ai_agent` operator model). No AI model, agent or LLM call exists in CE. Treat any "Discuss AI" as Enterprise.
- Livechat chatbot scripts (`chatbot.script`, steps `text`, `question_selection`, `question_email`, `question_phone`, `forward_operator`, free input) are rule-based, not AI.

**Activities.** `res.role` (roles, users many2many) lets activities and plan templates be assigned to a role (`role_id`, `activity_type.default_role_id`, `responsible_type='role'`). Unassigned role activities have an index. Activity types drop `chaining_type`/`triggered_next_type_id`/`recommended_activity_type_id` and have a single `suggested_next_type_id`. Activities gain `phone` and `activity_plan_id`. Activity type icons use Material Symbols. `kpi.provider` integration exposes activity counts, with visibility per type (`kpi_provider_visibility`).

**Other.** `mail.template` has `email_layout_force_header/footer`, `partner_cc` and `reply_to` relabelled. `res.users` gets `tracking=` on name/email/phone/login and `user_writeable=True` flags on out-of-office fields. `mail.gateway.allowed` whitelists senders from gateway quota.

### 3.2 Email tracking (new modules) — in depth

Two different "tracking" concepts exist in Odoo. The v20 split is about field-change tracking and message origin audit, not open/click tracking (that stays in `mass_mailing`/`link_tracker`).

**What was split.** In v19 `mail.tracking.value`, `mail.message.tracking_value_ids` and the tracking views lived in `mail`. In v20:
1. `mail` keeps the logic that detects changes. A new abstract `mail.track.mixin` (`addons/mail/models/mail_track_mixin.py`, inherited by `mail.thread`) holds `_track_prepare`, `_track_finalize`, `_mail_track`, `_track_get_fields`, `fields_get` tracking info, `_track_disabled` (`tracking_disable`/`mail_notrack` context). It is documented as enabling tracking "what to do with values is left to child model".
2. `mail.thread._track_log` still posts a `message_type='tracking'` message with `tracking_values`. The core renders the change summary directly into the message body using `mail.mail_tracking_template` (`old → new (field label)`, `mail_thread.py:3144`, `data/mail_templates_chatter.xml:80`). So chatter shows tracking even without the new module.
3. `mail_tracking` (`depends: ['mail']`, not auto-install) persists structured values. It adds:
   - `mail.tracking.value` (system-only crud via `security/ir.access.csv`) with `field_id`, `field_info` (JSON snapshot if the field is later removed), `old/new_value_{integer,float,char,text,datetime}`, `mail_message_id` (cascade).
   - `mail.message.tracking_value_ids` (groups `base.group_system`). `_create_tracking_data` creates them after the message as sudo. Messages with tracking values refuse content edit and copy with a changed message type.
   - `ir.model.fields._unlink_tracking`: when a tracked field is deleted, values are kept with their metadata in `field_info`.
   - Generation-source audit: `mail.message.source_template_id` and `source_view_id` (view must be `technical_usage='mail_post_source'`), propagated from the composer (`mail.compose.message.source_view_id`, `_prepare_mail_values_static`). Filters and group-bys by Template/View in the message search view.
   - Menu Settings > Technical > Discuss > "Tracking Values" (`views/mail_menus.xml`), and a Tracking tab on `mail.message` form.
4. `mail_tracking_mass_mailing` (auto-install with `mass_mailing`) adds `source_mailing_id` ("Generated by (mailing)") and propagates it from the composer.
5. `mail_tracking_sms` (auto-install with `sms`) adds `source_sms_template_id`, set by `sms.composer` for single and mass-log posts.

**Why it matters.** The doc string says it is for "auditing, debugging, and analysis", "accounting or business process audits". Concretely, a consultant can answer "which template or mailing generated this message?" and query old/new values in SQL or list views instead of parsing HTML bodies. `mail_tracking` is not auto-installed and is required by tests only (`test_mail` depends on it). Without it, `mail.message` has no `tracking_value_ids` field (the field is declared only in `mail_tracking`). Verify on a clean database what installs it; no manifest in `addons/` besides test modules depends on it. Confidence on "tracking history may be body-only in a database without `mail_tracking`": Medium. Consequence for upgrades: v19 databases already have the `mail_tracking_value` table, so the 20 upgrade must install the module or the data become orphaned and invisible in structured form.

**Not covered here.** Mass-mail open/click statistics (`mailing.trace`, `link.tracker.click`) are in `mass_mailing` and `link_tracker`. See `link_tracker` below for the `utm_reference` change that makes tracked links per-record.

### 3.3 Live Chat (`im_livechat`, `website_livechat`)

- Depends changed to `digest, mail, phone_validation, utm` (v19 `rating` dropped). Ratings are no longer `rating.rating` records: `discuss.channel.livechat_rating` is a Selection `1/3/5` (Unhappy/Neutral/Happy) with `livechat_rating_percentage` aggregated as `avg` (`models/discuss_channel.py:184-199`). The `rating.mixin`/`rating.parent.mixin` inheritance of `im_livechat.channel` is gone and `im_livechat.channel` fields `rating_count/percentage/percentage_satisfaction` are plain computes. `models/rating_rating.py` was deleted. Any report or automation reading `rating.rating` for livechat will lose data.
- `im_livechat.conversation.tag` (v19) removed with its views and widgets. `conversation_tag_ids` is gone from `discuss.channel`. No successor found.
- `livechat_operator_id`, `is_forward_operator` fields removed. Operators are tracked through `im_livechat.channel.member.history` (existing in 19). Medium confidence on exact replacement.
- New: `livechat_looking_for_help_since_dt` (replaces the old "looking for help" JS controllers), `available_operator_ids_count`, `script_external_text` on chatbot steps, `utm.mixin` on the chatbot (UTM source "Chatbot", `data/utm_data.xml`), `ir.http` override, leave dialog, rating notification service, messaging-menu items for livechat (the old sidebar category patches are removed).
- `website_livechat`: adds `discuss_channel_member.py`, a website controller, and reorganised static (`core/` replaces `common/`, `frontend/`, `web/`).

### 3.4 SMS and phone
- `sms`: `sms.composer` gains `sms_type` (marketing/alert), `scheduled_date`, `mail_scheduled_message_id`, `template_name`; it uses `_phone_get_recipients_info` (moved to `phone_validation`) instead of `_sms_get_recipients_info`. Scheduled SMS through `mail.scheduled.message.send_method`. Character counter widget and template selector are new (`sms_char_counter.js`, `sms_composer_template_selector.js`). Manifest adds `iap_paid_service`.
- `phone_validation`: `mail.activity.phone`, `_get_phone_number_from_record`, and an activity-schedule wizard extension so call-type activities get a phone number.
- `calendar_sms`: alarm view for `sms_template_id`; selection label shortened.
- `sms_twilio` exists in both versions and is unchanged in structure.

### 3.5 Calendar
**Multi-calendar (biggest functional change).** `calendar.calendar` ("User Calendar") and `calendar.user` (membership with `access_role` owner/writer, colour, filter flags, `is_primary`) are new (`addons/calendar/models/calendar_calendar.py`, `calendar_user.py`). Events and recurrences get `calendar_id` (cascade). Each user has `calendar_ids`, `owned_calendar_ids`, `writable_calendar_ids`, `primary_calendar_id`; the primary calendar cannot be deleted; `share_user_ids` shares a calendar with colleagues. `calendar_default_privacy` moved from user to calendar and has a new value `members_only` (Shared Calendar Members Only). The v19 `res.partner.partner_checked` filter field was removed.
- UI: attendee calendar side panel, filter sections, quick create, archive-or-unlink wizards (single and multi) replace the popover delete wizard. `calendar_provider_config` wizard removed. A setting `calendar_show_activities` shows activities in the calendar and a "schedule meeting" bridge exists on activities. Meeting activity link is `meeting_activity_ids` on events.
- Discuss meetings: `calendar.event.videocall_channel_id` backs an event with a Discuss meeting channel. `calendar/models/discuss_channel.py` computes `meeting_start_dt/stop_dt` from events. Portal users are invited to `/my/conversations/<id>` (`portal_discuss`).
- `google_calendar`: `google.calendar.sync` is replaced by `google.sync` plus `google.event.sync`. Per-calendar `google_sync_token`, `google_sync_enabled`, `is_import_pending`, `access_role` extended with `reader` and `freeBusyReader`, `google_account_email`. Hooks `enable_primary_calendar_sync` (post-init) and `remove_unimported_calendars` (uninstall). New route in `controllers/google_auth.py`. `microsoft_calendar` gets `microsoft_account_email`, `microsoft_sync_active`, `test_multicalendar`. The pre-20 `google_calendar_cal_id` field is dropped, so re-sync should be tested.
- `hr_calendar_google` (new, auto-install with `hr_calendar` + `google_calendar`): extends `google.event.sync` to treat Google `workingLocation` events as employee work locations. Creates `hr.work.location` and writes `<weekday>_location_id` on the employee. Skips those events as calendar events. A cron `cron_sync_working_locations` fetches the current week for users with a Google token (`models/res_users.py`). Note the removal of `hr_homeworking*` modules elsewhere in 20; `hr_calendar` provides the display.

### 3.6 Resource calendars (calendar side)
`resource.calendar` was redesigned (`addons/resource/models/resource_calendar.py:78`):
- `calendar_type` = `fixed` (weekly repeating), `variable` (dated attendances, multi-week rotations), `undefined` (flexible hours, optional hours target). It replaces `schedule_type`/`flexible_hours`/`two_weeks_calendar`/`duration_based`/`duration_days`.
- `attendance_ids_1st_week`/`_2nd_week`, `two_weeks_calendar`, `week_type` and the section display types are removed; instead attendances have `date` and recurrence (`recurrency_type`, `recurrency_interval`, `recurrency_end_type`, `recurrency_count/until`, `recurrency_excluded_occurences`), `count_as`, `hours_per_week`, `days_per_week`, `hours_per_day`, `reference_calendar_id` (for FTE), `color`, `country_id`.
- Monthly cron "Clean up calendar attendances" (`data/ir_cron.xml`). New attendance calendar view and components.
- Upgrade risk: modules (HR, planning, work entries) and customisations reading two-week calendars must migrate to `variable`. Data migration is outside this repo.

### 3.7 Portal
- `portal.entry` (new, `addons/portal/models/portal_entry.py`): the `/my` home cards (name, URL, image, `placeholder_count` counter name, `category`, `is_config_card`, `show_in_portal`) are now data records, extended via `_filter_visible_portal_cards`. Modules that register entries: account, payment, sale, purchase, project, hr_timesheet, event, website_slides, mass_mailing, mrp_subcontracting, `portal_discuss`, `auth_passkey_portal`, `website_crm_partner_assign`, `account_payment`.
- Portal chatter was reorganised into `static/src/chatter/portal`, `portal_project` and `core`; `portal_chatter.js`, `portal_chatter_service.js`, and the old frontend patches are removed and `controllers/portal_thread.py` is deleted from both `portal` and `rating`. The mail chatter code is reused. Any custom portal chatter JS must be ported.
- `portal` now depends on `base_address_extended`, `portal.res_country` model, new `portal_profile_editor` interaction replaces `portal_details`.
- `portal_discuss` (new, auto-install with mail+portal): the Discuss card (`/my/conversations`), counter `discuss_count` (unread memberships), visible only if the partner is a member of a channel, and the invite URL for portal users. Public Discuss assets under `mail.assets_public`.

### 3.8 Contacts, autocomplete, plugin
- `contacts` depends on `base_address_extended`, `mail`, `web_hierarchy`, adding a hierarchy view (default view mode `list,kanban,form,hierarchy,activity`). Settings are small.
- `partner_autocomplete` depends on `iap_mail` only (not `base_vat`). New autocomplete by DUNS and by field (`autocomplete_by_field`), `enrich_by_vat`, an "Enrich" server action, `additional_identifiers_list_partner_autocomplete` widget. The UNSPSC tag helper was removed. `iap_paid_service` is flagged. VAT now uses `vat` only, no `company_registry` fallback.
- `mail_plugin` (`depends digest, web, contacts`): IAP-based enrichment (`enrich_and_create_company`, `res.partner.iap`, `res_partner_iap_views`) is removed. New `search_records/<model>` and `redirect_to_record/<model>`. Controller now extends the portal `MailController`. Digest tips added. Plugin API clients (Gmail/Outlook add-in) built for v19 must be checked: the old `/mail_client_extension/modules/get` and `.../partner/get|create` aliases are gone.

### 3.9 Smaller modules
- `link_tracker`: `utm_reference` (Reference to the originating record) is part of the uniqueness key, so a short URL is now per source record. QR code download action. `utm.campaign` gets `utm_reference`; `utm.mixin` creates required UTM records on demand (`_utm_ref`, `SELF_REQUIRED_UTM_REF`); `utm` version 1.2.
- `project_todo`: digest tip with `Alt+Shift+T` shortcut, share-target (PWA) web client, `todo_template`, activity wizard. Auto-install with `project`.
- `rating`: `parent_res_id` becomes `Many2oneReference`; messaging-menu items replace the old patches; `portal_thread` controller removed.
- `gamification`: assets (`static/src/scss/gamification.scss`) removed; version tag dropped; SQL refactor to `SQL()`.
- `social_media`: the company group is no longer `base.group_no_one`-only, so the fields are visible to all with company access.
- `snailmail`: Pingen delivery webhook (`/webhook/snailmail/1/<delivered|undeliverable>`, HMAC with `snailmail.webhook_signing_key`), new state `process`, new layouts (`center`, `dual`, `lines`), `letter_uid`, `attachment_raw` instead of `attachment_datas`. No longer `auto_install`; `iap_paid_service`.
- `google_gmail`/`microsoft_outlook`: code-level refactor to typed config getters only.
- `mail_group`: new ir.access, trivial code change.

### 3.10 `mysubscription` — what is it?
A backend "My Subscription" client action (`mysubscription.dashboard`, fullscreen target) that depends only on `base`+`web` and is `auto_install`. Server: abstract `mysubscription.mysubscription` with `get_dashboard_data` (base URL, enterprise code visible to admins only, subscription considered active only if `database.enterprise_code` and a future `database.expiration_date` are set) and `get_iap_data` (lists `iap.account` balances/credit URLs for admins when `iap` is installed). Client: plan section, database section, IAP section, user-menu entry. It is a UI shell around the Odoo.com subscription data and, on a CE database without those parameters, will show "no subscription". It does not manage subscriptions (that is the separate `sale_subscription`, Enterprise). Confidence in intent: Medium; the code is clear but the Odoo-side product framing was not verified (no web check).

## 4. What's new / changed vs Odoo 19 (most impactful first)

1. Field-change tracking storage moved out of `mail` into optional `mail_tracking` (+ two bridges for mailing/SMS origin). High. `addons/mail_tracking/`, `addons/mail/models/mail_track_mixin.py`.
2. Unified `ir.access` replaces `ir.model.access` and `ir.rule` in module data; `res_access_*` stored flags on message/activity. High. `odoo/addons/base/models/ir_access.py`.
3. Calendar multi-calendar and sharing (`calendar.calendar`, `calendar.user`, access roles, privacy `members_only`), Google/Microsoft sync reworked per calendar. High. `addons/calendar/models/calendar_calendar.py`, `addons/google_calendar/models/google_event_sync.py`.
4. Discuss: polls, bookmarks (replace stars), read-only channels, channel owner/admin roles, categories, favorites, call artifacts and debrief UI. High. `addons/mail/models/mail_poll.py`, `mail_call_artifact.py`, `models/discuss/*`.
5. Call recording UI with no CE storage backend (hook raises NotFound). High that backend is absent. `addons/mail/controllers/discuss/rtc.py:216`.
6. Resource calendar redesign: fixed/variable/undefined, dated and recurrent attendances. High. `addons/resource/models/resource_calendar.py`.
7. Livechat ratings become a selection on the channel, conversation tags removed, `rating` dependency dropped, UTM chatbot source. High. `addons/im_livechat/models/discuss_channel.py:184`.
8. CC support in core (`partner_cc_ids`); `mail.thread.cc` deleted. High. `addons/mail/models/mail_message.py`, v19 `mail_thread_cc.py`.
9. Portal home cards as `portal.entry` data; new `portal_discuss`; portal chatter rebuilt. High. `addons/portal/models/portal_entry.py`.
10. VAT/IBAN validation merged into base/tools; VIES to `l10n_eu_account_vies`. High (see section 5).
11. `mail.bot._apply_logic` and `_message_post_after_hook` signatures changed. High. `addons/mail_bot/models/`.
12. `mail_plugin` IAP enrichment removed. High. `addons/mail_plugin/controllers/mail_plugin.py`.
13. Activity roles (`res.role`), single suggested next activity type, phone on activities. High. `addons/mail/models/res_role.py`, `mail_activity_type.py`.
14. `link_tracker.utm_reference` per-record short URLs and QR download; SMS scheduled messages and counters; snailmail webhook; `hr_calendar_google` working-location sync; `mysubscription`. High.
15. Persistent `mail.presence`, `im_status` selection. Medium (seen via field diff only).

## 5. Removed / merged modules

| Module | Where it went | Evidence |
|---|---|---|
| base_vat | Merged into `base`: `res.partner._check_vat`, `_run_vat_checks`, `_check_vat_number`, `_validate_identifier`; `res.country.vat_label`; identifier catalogue in `odoo/tools/partner_identifiers.py` (stdnum-based, 1042 lines) with `res.partner.additional_identifiers` (JSON) and `additional_identifiers_list` widget. The online VIES check moved to `l10n_eu_account_vies` (new, depends `account`, adds `vies_valid` and a cron, with the same "VAT VIES Check" description). | `odoo/addons/base/models/res_partner.py:1395-1560`; `addons/l10n_eu_account_vies/__manifest__.py`; `addons/partner_autocomplete/models/res_partner.py` no longer tests for `base_vat` |
| base_iban | IBAN tooling moved to `odoo/tools/bank_account_number.py` (`validate_iban`, `normalize_account_number`, `get_bban_from_iban`, `get_iban_part`). The `iban` account type is added in `account` (`selection_add=[('iban','IBAN'),('clabe','CLABE')]`) and validation is wired there; also used by `hr` and `l10n_ch`. `base.res.partner.bank` itself documents IBAN. | `addons/account/models/res_partner_bank.py:7,26,48`; `addons/hr/models/res_partner_bank.py` |

I could not find a successor for `im_livechat.conversation.tag`. `mysubscription` and the three `mail_tracking*` are new rather than merged from removed modules. Other removals in the list (`hr_homeworking*`, `hr_org_chart`, etc.) are outside this area.

## 6. Implementation notes, risks and migration gotchas (19 to 20)

- **Install `mail_tracking`** on upgraded databases if you need structured tracking history (`mail.tracking.value`) or message origin. Otherwise the table's users (e.g. reports or SQL based on `mail_tracking_value`) break. Custom modules referencing `mail.tracking.value` or `tracking_value_ids` must add `mail_tracking` to `depends`. Medium to High risk.
- **Security data**: any custom module shipping `ir.model.access.csv` or `ir.rule` XML must be ported to `ir.access` (`ir.access.csv` columns `id,name,model_id,group_id/id,operation,domain`; `operation` is a crud subset). High.
- **Starred messages**: `starred`/`starred_partner_ids` renamed to bookmark fields. Update domains, favourites, mail templates or SQL.
- **Livechat**: backup `rating.rating` rows and conversation tags before upgrade; reports based on them will be empty. Validate the Happy/Neutral/Unhappy mapping. Chatbot phone steps now rely on `phone_validation`.
- **OdooBot overrides** and any code calling `_message_post_after_hook(message, msg_vals)` need the new signature (`message` only).
- **Calendar**: each user is expected to get a primary calendar (`primary_calendar_id`; migration script not verified); Google sync must be re-authorised or re-tested (new `google_sync_token`, per-calendar sync, `google_calendar_cal_id` dropped). Check privacy defaults (now calendar-level, `calendar.default_privacy` ICP) and add shared members deliberately.
- **Resource calendars**: audit two-week calendars, flexible hours and `duration_based` configs in HR, payroll or planning customisations. Run the attendance clean-up cron expectations. High.
- **Portal customisations**: custom `/my` home templates, counters and portal chatter JS (`portal_chatter*.js`) need rework; use `portal.entry` records and `_filter_visible_portal_cards`.
- **mail_plugin** add-in clients: only `/mail_plugin/*` routes remain; enrichment is gone.
- **Snailmail** is not auto-installed anymore and needs the Pingen webhook reachable from IAP (signing key stored in `snailmail.webhook_signing_key`). Template or code using `attachment_datas` must use `attachment_raw`.
- **Tests**: `get_param` refactoring (`get_str/get_int/get_bool`) is pervasive; custom code that relied on string results may behave differently.
- **VAT/IBAN**: remove `base_vat`/`base_iban` from custom `depends`; for VIES install `l10n_eu_account_vies`. The `base_vat`-only fields `vies_valid`/`perform_vies_validation` are now in that module.
- **Auto-installs to expect**: `portal_discuss`, `mysubscription`, `hr_calendar_google`, `mail_tracking_mass_mailing`, `mail_tracking_sms` install automatically when their dependencies are present.
- **Call recording**: do not promise recording or transcription on CE.

## 7. Open questions / not verifiable from CE code

- What installs `mail_tracking` in a stock CE database (only test modules depend on it) and whether structured tracking is intentionally optional. Need an install run or Odoo release notes.
- The Enterprise side of call recording/transcription and any "Discuss AI" or AI agents (`ai` module; only hooks in CE).
- The Odoo.com semantics behind `mysubscription` (`database.enterprise_code`, `database.expiration_date` set by Enterprise or IAP processes).
- Migration scripts (no `migrations/` directories assessed; no git history) for renamed fields: starred to bookmarked, livechat rating, calendar to multi-calendar, resource calendars. Only the target schema was checked.
- Whether `livechat_operator_id` has an exact replacement.
- `mail.presence` and `im_status` behavioural change (seen only in field definitions).
- Exact end-user scope of the HTML composer assets (`html_composer_message_field`).
