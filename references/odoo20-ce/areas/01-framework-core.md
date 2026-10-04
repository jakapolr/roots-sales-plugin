# Framework & Platform Core — Odoo 20 CE

Evidence convention: [code] = verified by reading/diffing /home/user/odoo-src/odoo20 vs odoo19; paths are relative to `odoo20/`. [web] = none used. Confidence is High unless stated.

## 1. Scope
- `odoo/` Python package: `orm/`, `models/`, `fields/`, `api/`, `http/` (now a package), `tools/`, `cli/`, `service/`, `modules/`, `upgrade_code/`, `release.py`, `_monkeypatches/`, `tests/`.
- Core addons in `odoo/addons/`: `base` plus 15 test modules (down from 23 in 19, see 2.2).
- New top-level `skills/` directory (AI coding-agent skills).
- `requirements.txt`, `setup.py`.
- New addons: `populate`, `test_populate`, `test_translation_mode`, `test_utm` (all in `addons/`).
- Also checked for the coordinator's priority questions: `ir.access`, offline mode, MCP / JSON-2 API.

## 2. Catalogue

### 2.1 Platform facts
| Item | v19 | v20 | Evidence |
|---|---|---|---|
| Version | 19.0 | `version_info = (20, 0, 0, FINAL, 0, '')` | `odoo/release.py` |
| Python | min 3.10 | **min 3.12, max 3.14** | `odoo/release.py` (`MIN_PY_VERSION=(3,12)`, `MAX_PY_VERSION=(3,14)`); code uses PEP 695 syntax (`def f[T]()`, `class X[T]`, `type X = ...`) |
| `requirements.txt` | many `python_version < '3.11'/'3.12'` pins (Jammy-era) | all pre-3.12 pins dropped; added `h11==0.16.0`, `tzdata` (win32 only); removed `xlrd`, `xlwt`, `pytz`, `asn1crypto`, `chardet` | `requirements.txt` diff |
| PDF lib | `PyPDF2` | `setup.py` now requires `pypdf` (requirements still pins `PyPDF2==2.12.1 <3.13` as legacy fallback); `tools/pdf/_pypdf2_1.py` removed | `setup.py`, `odoo/tools/pdf/` |
| Excel | xlrd/xlwt monkeypatches | `_monkeypatches/xlrd.py`, `xlwt.py`, `pytz.py`, `requests.py` deleted; new `zoneinfo.py` (maps tz names removed in Ubuntu 24.04 to canonical ones) and `logging.py` (RUNBOT level) | `odoo/_monkeypatches/` |
| Default HTTP bind | `0.0.0.0` (warning "will change to 127.0.0.1 in 20.0") | **`127.0.0.1`** | `odoo/tools/config.py` |

### 2.2 Core addons (`odoo/addons/`)
| Module | Status | Notes |
|---|---|---|
| `base` | Changed (heavily) | `ir.access` replaces `ir.model.access`+`ir.rule`; `res.bank` removed; new `clearing.label`, `website` stub model, `ir.profile.query`, `res.session`; `populate/` folder (blueprint sample `common.xml`) |
| `test_base` | **New** (consolidation) | Absorbs most former test_* modules as `tests/test_core`, `test_modules`, `test_orm` (46 files), `test_tools`. Depends only on `base`. |
| `test_tests` | New (consolidation) | Test-framework tests (`test_form.py`, `test_cases.py`, `test_freeze_time.py`, `test_logging.py`...) — replaces `test_testing_utilities` |
| `test_translation` | New | Translation tests (export wizard, load manifest translations, term count, UI); replaces `test_translation_import` |
| `test_web` | New | Search-panel, `web_read_group`, `formatted_read_group`, grouping sets, `web_save`, `web_read`, properties/onchange tests (replaces `test_read_group`, `test_search_panel`) |
| `test_l10n` | New | `install_all_l10n.py`, `test_country.py` |
| `test_http`, `test_inherit`, `test_lint`, `test_main_flows`, `test_uninstall`, `test_assetsbundle`, `test_data_module(_install)`, `test_inherit(s)_depends` | Changed | Switch to `ir.access.csv`; `test_http` gains `test_bearer_scope`, `test_auth_custom` (absorbs 19's `test_auth_custom`), `test_rpc_path`, `test_error_http/rpc` |
| Removed test modules (13) | Removed → test_base / test_web / test_tests / test_translation / test_http | `test_access_rights, test_action_bindings, test_auth_custom, test_convert, test_converter, test_inherits, test_mimetypes, test_orm, test_read_group, test_rpc, test_search_panel, test_testing_utilities, test_translation_import` (13 modules). Successor mapping is by file names (e.g. `test_base/tests/test_orm/test_action_bindings.py`, `test_inherits.py`, `test_tools/test_mimetypes.py`, `test_tools/test_convert.py`); Medium confidence on `test_converter`/`test_rpc`. |

### 2.3 New addons
| Module | App? | Summary |
|---|---|---|
| `populate` (cat. Hidden/Tools, depends `base`) | No | Synthetic data generator driven by XML/JSON **Blueprints** (`populate.blueprint`, `populate.session`, `populate.job`, `populate.model.data`). Registers the `odoo-bin populate` CLI command. Replaces v19's `odoo-bin populate` + `tools/populate.py` + per-model `_populate_factories`. |
| `test_populate` | No | Test suite + sample blueprints (`populate/sample_blueprints.xml`) for the populate module (generators: scalar, textual, temporal, relation, choice, binary, fake, reference, properties, misc). |
| `test_translation_mode` (depends `web`) | No | In-context interactive translation mode (command palette → side panel) that tags translated strings with invisible metadata (siphash) and redirects to Weblate (default Odoo official project, configurable in settings). Explicit warning: do not use on production. Files: `static/src/translation_mode_service.js`, `models/ir_http.py`, `tools/translate.py`. |
| `test_utm` (depends `utm`) | No | Test-only models (`test_utm_sale_order`, `test_utm_mailing`) for `utm.mixin` tests, split from functional modules. |

## 3. Deep dives

### 3.1 `ir.access`: unified ACL + record rules (PRIORITY)
**What changed [code].** `ir.model.access` (CSV `ir.model.access.csv`) and `ir.rule` (`base_security.xml`, `models/ir_rule.py`) no longer exist as models. `grep "_name = 'ir.rule'|'ir.model.access'"` in odoo20 returns nothing. They are replaced by one model, `ir.access` (`odoo/addons/base/models/ir_access.py`, 540 lines; `_allow_sudo_commands = False`). Files removed: `security/ir.model.access.csv`, `security/base_security.xml`, `models/ir_rule.py`, `views/ir_rule_views.xml`; added: `security/ir.access.csv` (142 rows), `views/ir_access_views.xml`.

**Fields of `ir.access`:**
- `name` (required), `active`, `model_id` (M2O `ir.model`, cascade, indexed), `group_id` (M2O `res.groups`, optional), `domain` (Char, Python-evaluated domain string), `note` (Html).
- `operation` (Selection, required): any subset of `crud` letters in fixed order (`c`, `r`, `u`, `d`, `cr`, `ru`, `crud`, ... 15 values). It replaces the four `perm_*` booleans.
- Computed/searchable helpers: `kind` (`permission` if `group_id` set, else `restriction`), `is_standard` (defined by a module vs `__export__`/`__custom__`/`studio_customization`), and `for_read/for_write/for_create/for_unlink` booleans (inverse writes `operation`). These use the new field attribute `compute_sql` so they are searchable/groupable.

**Semantics [code: `orm/models.py::_access_domain`; confirmed by `skills/odoo-guidelines/guidelines/security.md`].**
- Rows **with a group** = *permissions*; their domains are **OR-ed** across all groups of the user (a group's implied groups count).
- Rows **without a group** = *restrictions* (the old global rules, plus ACL-less constraints); **AND-ed** on every user and never grant anything.
- Resulting domain = `OR(permissions) & AND(restrictions)`. No permission at all gives `Domain.FALSE` -> model-level AccessError ("default deny"). A permission row with empty domain = whole model.
- `_inherits` parents: each parent model's access domain is AND-ed in as `(parent_field any <parent domain>)` (`_check_inherits_access`).
- Replaces the old two-stage check (ACL boolean, then ir.rule domain). Public ORM API stays: `check_access(op)`, `has_access(op)`, `_filtered_access(op)`, plus new `Model._access_domain(operation)` (ormcache keyed by `env._access_context`, i.e. allowed companies) and `_make_access_error_message`.
- Eval context for domains: `user`, `time`, `company_ids`, `company_id` (same as old ir.rule).
- **New domain operator `'access'`** (`orm/domains.py::_operator_access_rule_domain`): `[('partner_id', 'access', 'read')]` means "records whose many2one target the user can access for that operation"; also works on `id`. Value must be read/write/create/unlink. Used inside access domains to chain permissions across models; the access-error builder (`_get_groups_with_access`) walks these to tell users which groups would allow the operation.
- Validation: `_check_domain` (domain must validate against the model, `access` conditions skipped), no domain on `ir.access` itself.
- Caching: `_get_all_access()` is an `ormcache(cache='stable')` map of `AccessInfo(id, group_id, operation, domain)`; `_clear_caches()` invalidates env + access cache + `stable` ormcache on create/write/unlink.
- `customize()` method: for module-defined accesses, deactivates the standard row and returns a copy for editing (UI "customize" button).
- Error messages are rewritten (`ACCESS_ERROR_MESSAGE`; model-level message now lists the groups that would grant the operation; record-level message keeps the jokey text; debug users see "Blame the following accesses").

**Interaction with `res.groups` / privileges [code: `models/res_groups.py`, `res_groups_privilege.py`].**
- `res.groups.model_access` (O2M `ir.model.access`) and `rule_groups` (M2M `ir.rule`) are replaced by `access_ids` (O2M `ir.access`, `copy=True`) + `access_count`; new `implied_count`, `implied_by_count`.
- Group changes now use `transaction.invalidate_ormcache('groups')` and `ir.access._clear_caches()`; `_check_user_disjoint_groups` rewritten (per-group check of exclusive user-type groups, error "User %s cannot be at the same time in exclusive groups"); new check "This makes a group imply two disjoint groups".
- `res.groups.privilege`: `description`, `placeholder` now `translate=True`; placeholder relabelled "No group label"; `res.groups.privilege_id` string renamed "Scope". The `(privilege_id, name)` unique constraint on `res.groups` was removed.
- `res.groups.share` help text changed; `res.groups` `_clear_cache_name='groups'`, `_clear_cache_on_fields={'implied_ids','implied_by_ids'}`.
- `ir.model.access_ids` now points to `ir.access`; `rule_ids` is gone from `ir.model`.
- `ir.actions.server.group_ids` is used (the new `base/data/ir_action_data.xml` defines "Change Password" action).

**CSV / XML format.**
- `ir.access.csv` header: `id,name,model_id,group_id/id,operation,domain` (see `odoo/addons/base/security/ir.access.csv`, `test_base/security/ir.access.csv`).
- Old: `id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink`. New: single `operation` string + optional `domain`.
- Examples [code]: `ir_attachment_public_rule,read public attachments,ir.attachment,base.group_user,r,"[('public', '=', True)]"`.
- Rows without a group (global restriction) leave `group_id/id` empty. To grant to everyone including public use `base.group_everyone`.
- Records defined in XML (`<record model="ir.access">`) are possible; the migration script handles both.
- The file must be listed in manifest `data` and the lint test `test_lint/tests/test_security_files.py` (new) checks security files.

**Upgrade script `odoo/upgrade_code/19.4-00-ir-access.py`** (run via `odoo-bin upgrade_code`): reads `ir.model.access.csv` and `ir.rule` records from a module's CSV/XML (`security`/`access` files), builds equivalent `ir.access` rows honouring group implication and disjointness (`SetDefinitions`), subsumes redundant rows, creates `security/ir.access.csv`, edits `__manifest__.py` `data` list, removes the old file, and prints warnings for misconfigurations (an ACL without rule combined with another group's rules: "giving access to ALL records ... may interact with rules ... giving access to LESS records"). Records not defined in the module's own namespace are skipped with a warning. This is the migration path for custom modules; manual review of its warnings is mandatory because the semantics of rules changed (global rule -> restriction, group rules -> per-group permission domains).

**Migration impact for custom modules.**
1. Run `odoo-bin upgrade_code --from 19.0 ...` (see 3.5) on every custom addon; review warnings.
2. Any Python using `self.env['ir.model.access']` / `self.env['ir.rule']` / `ir.rule._compute_domain` / `check_access_rights` / `check_access_rule` must be rewritten (removed: see 4).
3. `res.groups.model_access`, `rule_groups`, `ir.model.rule_ids` references in views/XML need updating.
4. Rules previously "global + no group" must become restrictions; any restriction that does not cover all operations leaves other operations permitted (`skills/odoo-security/SKILL.md`: "write checks write access only, never read").
5. Tests using `ir.rule` records/`_compute_domain` should use `ir.access` and `Model._access_domain`.
6. Data XML that referenced `base.model_ir_model_access`/rule XML ids will break.

### 3.2 ORM API (developer-facing)
- **Removed `read_group` dict API**: in 19, `read_group()` was deprecated (`@api.deprecated`) in favour of `_read_group` and `formatted_read_group`. In 20 the old `read_group` + `_read_group_fill_results/_fill_temporal/_format_result` are **deleted**. A new `Model.read_group(domain, groupby, aggregates, having, offset, limit, order)` exists (`@api.model`, `@typing.final`, `orm/models.py:1932`) and returns a list of tuples like `_read_group` but with records converted to ids (groupby value -> id, `recordset` aggregate -> list of ids). `_read_group` is the overridable one. `formatted_read_group`, `formatted_read_grouping_sets`, `web_read_group` stay in `addons/web/models/models.py`. Raises `ValueError("Need groupby or aggregates.")` when both empty. `_read_group` no longer calls `check_access('read')` at the top (access is now applied through the query/`_access_domain`) — Medium confidence. Hooks changed signature: `_read_group_select(table, spec)`, `_read_group_groupby(table, spec)`, `_read_group_having(table, domain)`, `_read_group_orderby(table, order, groupby_terms)` (query/alias params replaced by `TableSQL`).
- **SQL-building API refactor (breaks any override)**: `Query` moved from `odoo.tools.query` to `odoo/orm/query.py` with new `TableSQL`/`FieldSQL`; `tools/query.py` removed, `from odoo.tools import Query` removed from `tools/__init__`. Signatures: `Field.to_sql(table)`, `Field.condition_to_sql(table, field_expr, operator, value)`, `Field.property_to_sql(field_sql, property_name)`, `Field.join(table, kind)`, `Domain._to_sql(table)`, `_order_to_sql(table, order, reverse)`, `_order_field_to_sql(...)`. Old `(model, alias, query)` signatures are gone. `Query.where/join/select` with non-SQL args emit "Since 20.0, use only SQL..." DeprecationWarnings (`orm/query.py`).
- **New field attribute `compute_sql`** (`orm/fields.py`): `compute_sql='_compute_sql_x'` or lambda `(model, table) -> SQL` makes a computed, non-stored field searchable/sortable/groupable in SQL; requires explicit `compute_sudo`. Related fields get `_compute_sql_related`. Example: `ir.access.kind`, `res.currency._current_rate_sql`, `company_default_for(...)` (`res_company.py`).
- **Field attribute changes**: `copy` may be a callable `(record) -> value` (e.g. `copy=mark_as_copy('name')`, `tools/translate.py::mark_as_copy`), which replaces many `copy_data` overrides (`res.groups.copy_data` removed). New `init_storage` param (initialises column values; replaces `Model._init_column`, now `@deprecated("Since 20.0 ... Field.init_storage")`). `Char.size` removed. `_table_has_rows` deprecated. `convert_to_cache(value, records, validate)` (param renamed from `record`). `ir.model.fields.index` is now a Selection (btree / btree_not_null / trigram) instead of Boolean (`allowed_index_types`). New custom field parameter mechanism `user_writeable=True` on `res.users` fields replaces `SELF_READABLE_FIELDS`/`SELF_WRITEABLE_FIELDS`/`_self_accessible_fields` (`res_users.py` `_valid_field_parameter`) — Medium (removal of the old properties verified by diff of definitions).
- **Binary fields**: values are `BinaryValue`/`BinaryBytes` objects (`odoo/tools/binary.py`, `EMPTY_BINARY`), lazily loaded; `ir.attachment._file_read()` returns `BinaryValue`; `_file_write(fname, io)`, `_file_fname(sha)`; the `bin_size` context dependency was removed; Binary fields are not sortable/groupable. Custom code touching `attachment.datas`, `_file_read(fname, size)`, `_get_path` must be reviewed.
- **Access API**: `has_field_access`/`check_field_access` are public (were `_has_field_access`, `_check_field_access`; the latter kept as `@deprecated`); `check_field_access_rights`, `check_access_rights`, `check_access_rule`, `_filter_access_rules(_python)`, `_check_recursion`, `_check_m2m_recursion`, `toggle_active` were deprecated in 18/19 and are **removed** (use `check_access`, `has_access`, `_filtered_access`, `_has_cycle`, `action_archive/unarchive`).
- **Recordsets**: `concat(it=(), /, *args)` / `union(it=(), /, *args)` accept an iterable (varargs-only and empty forms warn "Since 20.0, use concat() with only one iterable"). `name_create` return type no longer allows `False`. `Model._inherit` internal refactor. `get_public_method(model, name)` exported from `odoo.models` (replaces `check_method_name`; used by the `/json/2` controller).
- **Cached models**: new `models.CachedModel` (`orm/models_cached.py`): `_cached_data_domain`, `_cached_data_fields`, `_clear_cache_name`; caches whole small tables (e.g. `res.company`, `res.currency`, `website` now inherit it). Uses the `stable` ormcache.
- **Domains**: lowercase operators enforced, `'<>'` and `'=='` operators (deprecated in 19) now rejected; comparing booleans with non-booleans warns ("Since 20.0, compare booleans only with booleans"); `Domain.is_condition(field_expr, operator, value)` helper; `optimize_dynamic`/`optimize_full(model, search_domain)`; `osv/expression.py` (`odoo.osv.expression`) **removed** — use `odoo.fields.Domain`. `any!`/`not any!` on AccessError now re-raise.
- **Decorators**: `@api.deprecated` removed; use `from odoo.tools.func import deprecated` (a `warnings.deprecated` backport; `typing`-style generics PEP 695). `api.ormcache` is now defined in `odoo/orm/cache.py` and exported from `odoo.api`; `from odoo.tools import ormcache`/`tools.cache` emit "Since 20.0 import ormcache from odoo.api". `Environment`/Registry: `registry.clear_cache(...)` removed -> `self.env.transaction.invalidate_ormcache('name')`; `registry.clear_access_cache` -> `transaction.invalidate_access_cache`; `env.cache` / `_field_access_memo` deprecated ("use transaction.clear or transaction.reset"). `Registry.signal_changes/check_signaling/registry_invalidated` replaced by `will_change_registry`/`_signal_changes`.
- **Exceptions**: `UserError.suppress_traceback()` removed; replaced by class attribute `conceal_debug_traceback = True` (`exceptions.py`).
- **`ir.config_parameter`**: typed API `get_bool/get_int/get_float/get_str` and `set_bool/set_int/set_float/set_str` (415 `get_str/set_str` call sites in addons vs 2 `get_param`). `get_param`/`set_param` are gone from the model. Value field help: "Supported types: str, bool, int, float".
- **ir.cron**: `_trigger(at, *, coalesce=0)`, `_rollback_progress()`, `CompletionStatus(enum.StrEnum)`; v19's `@api.deprecated` helper removed.
- **Other models**: `ir.actions.act_window.views` and `params` become Json instead of Binary; `ir.model`/`ir.ui.view` gain `explanation`/`notes`; `ir.actions.server` can update a property (`update_property`, `property_selection`); `ir.ui.view` gets `technical_usage`, card/filter/kanban postprocess, `_get_access_groups`; `ir.module.module` gets `test_data`, `iap_paid_service` (replaces `has_iap`); `ir.mail.server.max_email_size` removed; `res.partner` gets `has_vat`, `additional_identifiers` (Json) driven by `odoo/tools/partner_identifiers.py` + `partner_identifier_validation.py` (stdnum-based), `company_registry*` computed fields removed from base, `partner_latitude/longitude` removed from base (Medium), `res.partner.vat` index `btree_not_null`; `res.device` becomes `res.device.log`/`res.device`/`res.session` (`res_users.session_ids`); `res.currency._get_rates` returns `(rate, date)` tuples; `res.lang` data classes are `Mapping` not `ReadonlyDict`; `ReadonlyDict` is now a function returning `MappingProxyType`.
- **Bank data**: `res.bank` removed from base (`models/res_bank.py` deleted, `data/res_bank*.xml` deleted); `res.partner.bank` now in `models/res_partner_bank.py` and stores `bank_name`, address fields, `bank_bic`, `clearing_number` and `clearing_label_id` (new `clearing.label`) directly. `tools/bank_account_number.py` added. Migration: `l10n_fr_account/migrations/2.2` is the only remaining `res.bank` reference. Anything depending on `res.partner.bank.bank_id` must be rewritten (Medium: no successor model for banks found in CE).
- **`website` model in base** (`models/website.py`): a minimal `CachedModel` so `ir.http` can look up the website before `website` is installed (`env.website`); `data/website.xml`.
- **Profiling**: `ir.profile.query` model, `profile_query_ids`, `traces_sync` removed.
- **Translation**: `tools/translate.py` adds `StoredTranslations` (dict subclass with fallback languages), `ParsedTranslation`, `adapt_translated_field_value`, `get_translations_for_references`, `get_iso_codes` moved (from `tools.misc`), `is_meaningful_term`; `Char/Html.get_trans_terms/get_text_content/get_translation_dictionary/get_translation_fallback_langs` removed from field classes. Lint tests: `test_override_translated_fields.py`, `test_i18n.py`.
- **tools**: `tools.safe_eval` is now a package (`evaluation.py`, `expression.py`, `runtime.py`) with config `--unsafe-policy {disable,log,raise,terminate}`; `tools.cache` and `tools/populate.py`, `tools/pycompat.py`, `tools/test_reports.py` removed (`tests/reports.py` added); new `tools/duplicate.py`, `business_data.py`, `binary.py`; `tools.misc`: `flatten, discardattr, scan_languages, mod10r, street_split, get_flag, format_frame, ...` removed, `find_circular_dependency`, `diff_zip`, `LazyDict` added; `tools.sql`: `SQL` metaclass, `LiteralSQL`, `escape_like_value` (replaces `escape_psql`, "Since 20.0, use escape_like_value"), `quoted_identifier`, `format_query`, `pg_varchar`, `create_unique_index` removed; several marked "Removed after 20.0". `tools.convert.convert_csv_import/convert_sql_import/convert_xml_import` no longer re-exported. `tools.image`: `image_process`-style helpers warn "use directly binary_to_image / image_apply_opt". `GeoIP` dict API deprecated ("Since 20.0, dictionnary GeoIP API is deprecated").
- **Tests framework**: `tests.common` adds `MockHTTPClient`, `CrossModule`, `QueryLike`, `Response`, `flushing_cursor`, `DummyRLock`; `SingleTransactionCase` removed; runbot parallel testing config `tests/runbot/parallel_testing.json`; `--test-tags` doc now says `post_install` is default tag with `standard`. `tests/loader.py`, `tag_selector.py` changed (Low detail).

### 3.3 HTTP / controllers
- `odoo/http.py` (2,897 lines) is now the package `odoo/http/` (`__init__`, `_facade`, `dispatcher`, `geoip`, `requestlib`, `response`, `retrying`, `router`, `routing_map`, `server`, `server_log`, `session`, `stream`). Public API (`http.route`, `http.request`, `http.Controller`, `http.Response`, `http.Stream`) is re-exported from `odoo/http/__init__.py`; internals import paths changed (`odoo.http.requestlib.Request`, `odoo.http.session`). `odoo/tools/_vendor/sessions.py` removed.
- `@route`: `type` is only `'jsonrpc'` or `'http'` (the `'json'` alias is long gone; 18.1 upgrade script `18.1-02-route-jsonrpc.py` handles it). `auth='bearer'` requires `bearer_scope` (and it must not be set for other auth methods). New route options documented: `captcha`, `save_session`, `handle_params_access_error`, `readonly` may be callable. `ir.http._auth_method_bearer(cls, routing)` now takes the routing dict.
- Default bind 127.0.0.1; new `--gevent-workers`, `--db-system` (`PGDATABASE_SYSTEM`; DB used for shared system operations such as bus), `ODOO_MAX_HTTP_THREADS` env.
- **JSON-2 API** (`/json/2/<model>/<method>`) already existed in 19 and still lives in `addons/rpc/controllers/json2.py` (+ `addons/api_doc`); in 20 it uses `get_public_method`. `addons/web/controllers/json.py` still has `/json/<path>` and `/json/1/...` (`auth='bearer'`, `bearer_scope='rpc'`).
- Errors: `UserError.conceal_debug_traceback`; test split `test_error_http.py` / `test_error_rpc.py`.
- Logging: coloured log output controlled by `[colors]` config section and `ODOO_PY_COLORS`, `NO_COLOR`, `FORCE_COLOR`; `--syslog` marked deprecated.

### 3.4 CLI (`odoo-bin` subcommands)
v20 commands (`odoo/cli/`): `cloc, db, deploy, duplicate (new), help, i18n, module, neutralize, obfuscate, scaffold, server, shell, start, upgrade_code`, plus `populate` which is now provided by the `populate` addon (`addons/populate/cli/populate.py`; the core `cli/populate.py` is gone). Details:
- `duplicate` (new, `odoo/cli/duplicate.py`, `tools/duplicate.py`): "Populate database via duplication of existing data" — options `--factors`, `--models` (default `res.partner,product.template,account.move,sale.order,crm.lead,stock.picking,project.task`), `--sep`. This takes over the role of v19's `populate` command (duplication-based; was `tools/populate.py`).
- `populate` (addon): `odoo-bin populate -d DB -b BLUEPRINT [--seed --scale -j N|auto --resume [id] --profile]`; requires the `populate` module installed and `-u populate` after installing modules that ship blueprints (README).
- `module`: new `list` subcommand, `-n/--dry-run` for install/uninstall/upgrade.
- `db`: uses `odoo.modules.db` (functions moved from `odoo/service/db.py`, now removed; `service/security.py` also removed): `db.create`, `db.restore`, `db.dump`, `db.duplicate`, `db.drop`, `db.rename`, `db.exist`, `db.list_dbs`; `create` kwarg `login` -> `user_login`.
- `scaffold`: `l10n_payroll` template removed.
- `upgrade_code`: new `FileManager.get_modules()`, `get_file(module, name)`, `FileAccessor._save` (deletion support), shared helpers `tools_etree.py`, `tools_js_expressions.py`.
- `start` / `server` / `shell`: `-s` short option for `--save` removed (use `--save`); `--stop` alias for `--stop-after-init`; unambiguous long-option prefixes accepted; default config file lookup now prefers `appdirs` user config dir `odoo.conf`.
- `--stop-after-init`, `--unsafe-policy`, `--db-system`, `--gevent-workers`: new config options (`tools/config.py`).
- Deprecated and removed: `config.rcfile`, `config.load()` (19 deprecations).

### 3.5 `odoo/upgrade_code` scripts — the change log
Run via `odoo-bin upgrade_code`. Scripts new in 20 vs 19 (version number = "saas-xx" series; `19.1`..`19.5` are 19.x minor series that were not run in 19.0 GA, `20.0` is GA):

| Script | Transformation | Meaning |
|---|---|---|
| `19.1-00-t-call.py` | QWeb: move `t-set` before `t-call`, auto-close empty `<t>`, fix xpaths targeting `t-call`/`t-snippet-call` | `t-call` bodies no longer used for variable passing / QWeb `t-call` semantics changed (qweb now takes `root_values, process` params) |
| `19.3-00-account-groups.py` | Generates `account.group` data for 23 CoAs (`ar_base, bd, bh, co, do, ec, il, iq, jo_standard, kh, kw, lb, mx, mz, om, pk, qa, sk, ua_psbo, us, zm`) | Chart of accounts groups rebuilt from account code ranges (accounting) |
| `19.3-00-account-report-foldable.py` | `account.report` data: shorthand formula engines (`domain_formula` -> `domain`, `aggregation_formula`, `account_codes_formula`, `external_formula`, `tax_tags_formula`), foldable flag | Report line definitions format |
| `19.3-00-base64-in-xml.py` | `<field type="base64" file=...>` -> `type="bytes"` | Matches `tools/convert.py` warning "Since 20.0, use type=bytes instead of type=base64" |
| `19.4-00-ir-access.py` | `ir.model.access` + `ir.rule` -> `ir.access.csv` | See 3.1 |
| `19.4-00-ormcache-on-transaction.py` | `registry.clear_cache` -> `transaction.invalidate_ormcache` | See 3.2 |
| `19.5-00-tuple-rec_names_search.py` | `_rec_names_search = [...]` -> tuple `('name',)` | Model attribute must be tuple |
| `20.0-00-search-date-filters.py` | Removes `start_month/end_month/start_year/end_year` from `<filter date="...">` in search views | Not parsed anymore, rejected by RNG |
| `owl3-migration.py` | Converts Owl 2 templates/JS to Owl 3 (`t-esc`/expression rewriting, excluded-template list incl. `point_of_sale.Navbar`, `Appointment.*`, `ai.*`) | Owl 3 migration of the web client (e.g. `@odoo/owl` `Plugin`, `usePlugin`, `signal`, `computed` used in `offline_plugin.js`); `web/static/src/owl2` kept for legacy |
| existing since 19: `17.5-01-tree-to-list`, `18.1-00-sql-constraint`, `18.1-02-route-jsonrpc`, `18.2-00-l10n-translate` (changed), `18.3-00-l10n-fiscal-position-taxes`, `18.5-00-deprecated-properties`, `18.5-00-domain-dynamic-dates`, `18.5-00-no-tax-tag-invert` | | unchanged except `18.2-00-l10n-translate` (changed) |

### 3.6 Skills directory (`skills/`)
**What it is [code: `skills/README.md`]:** "a set of useful Skills for agentic development with Odoo" — structured documentation for AI coding agents (format agentskills.io; same `SKILL.md` + frontmatter convention as Claude Code skills). Installation = copy the directory into `.agents/skills/` or `.claude/skills/` (or global) of the harness; all four skills must be installed together because they cross-reference.
- `odoo-guidelines` (`SKILL.md` + `guidelines/`: comments, controllers, fields, manifest, module_structure, orm, performance, python, reports, security, stable, tests, xml; `AUTHORING.md`): house rules for any file outside `static/`.
- `odoo-web-guidelines` (`guidelines/`: assets, javascript, scss; `AUTHORING.md`): JS, Owl templates, SCSS, Hoot tests under `static/`.
- `odoo-security`: security audit checklist (access control, field groups, default-to-private methods, SQL, domain injection, sudo, routes/CSRF, XSS, `file_open`, `eval`, pickle, timing attacks, mutable defaults).
- `odoo-review`: two-pass code review process dispatching changed files to the three sibling skills.
- They state conventions of "master" (= v20): e.g. `ir.access.csv` is the only access format, `stable.md` lists API stability rules. Useful to implementers as a free, authoritative statement of what Odoo S.A. considers correct v20 code.

### 3.7 Offline mode and MCP claims (coordinator request)
- **"Offline mode to create/edit/archive/delete records": VERIFIED (web client, CE).** `addons/web/static/src/core/offline/offline_plugin.js` (Owl 3 `Plugin`) stores data in IndexedDB (`"offline"` DB, encrypted with `session.browser_cache_secret` via `core/crypto`; disabled in non-secure contexts, `FakeIndexedDB`). `scheduleORM(model, method, args, kwargs, options)` queues ORM calls when a `ConnectionLostError` happens and syncs them when back online (`syncingORM`, `_ormToSync`, table `orm-to-sync`). Relational model uses it for `web_save` (create/edit: `record.js::_offlineSave`) and `web_unlink` (delete: `record.js`, `dynamic_list.js`); archive goes through the same list/record paths (Medium for archive specifically: `web_save`/unlink calls verified, an explicit "archive" scheduleORM call not separately located). Only previously *visited* UI (list/kanban/form views and many2x searches, `VISITED_UI_TABLE_NAME`) is available offline; UI buttons without `data-available-offline` are disabled while offline (`SELECTORS_TO_DISABLE`); fields have `availableOffline` flags (binary = false); components: `offline_systray`, `OfflineActionHelper`, `OfflineSearchBar`, `offline.scss`. Not tested for conflict resolution here.
- **"AI agents connect over MCP": NOT FOUND in CE.** `grep -w "MCP|mcp|Model Context Protocol"` over `odoo/` and `addons/` (py/js/md) finds nothing; there is no `ai*` addon in the CE tree (`ls addons | grep ^ai` empty). The only AI-adjacent items are JS templates (`ai.VoiceTranscriptionBlueprint`, `ai_website_livechat...`) listed in `owl3-migration.py` exclusions, which belong to Enterprise/other repos. What does exist in CE is the **JSON-2 external API** (`addons/rpc/controllers/json2.py`, documented by `addons/api_doc`) with bearer API keys (`auth='bearer'`, `bearer_scope='rpc'`) — an HTTP interface an MCP server could wrap, but no MCP code ships. Any MCP/AI-agent feature would be Enterprise or external (cannot be verified from CE).

## 4. What's new / changed vs Odoo 19 (most impactful first)
1. `ir.model.access` + `ir.rule` replaced by `ir.access` (permissions/restrictions, `operation` string, `'access'` domain operator, `ir.access.csv`) — High. `odoo/addons/base/models/ir_access.py`, `odoo/orm/models.py::_access_domain`.
2. Python >= 3.12 (<= 3.14), PEP 695 syntax, `pypdf`, removal of `xlrd/xlwt/pytz` — High. `odoo/release.py`, `requirements.txt`, `setup.py`.
3. SQL-generation API rewritten around `TableSQL`/`FieldSQL`; `Query` moved to `odoo.orm.query`; `compute_sql` field attribute; `osv.expression` removed — High. Breaks custom `_condition_to_sql`, `_read_group_*`, `_order_to_sql` overrides.
4. `read_group` dict API removed (new tuple `read_group`, keep `_read_group`/`formatted_read_group`) — High.
5. Deprecated-in-18/19 APIs removed: `check_access_rights/rule`, `_filter_access_rules`, `toggle_active`, `_check_recursion`, `api.deprecated`, `registry.clear_cache`, `config.rcfile`, `config.load`, `get_param/set_param`, `<>`/`==`/uppercase domain operators — High.
6. `http.py` -> `odoo/http/` package; default bind `127.0.0.1`; bearer scope mandatory — High.
7. Test-module consolidation (23 -> 15 test addons in core) — High.
8. `populate` addon with blueprints; `duplicate` CLI replaces old populate; `module list/--dry-run`; db helpers moved to `odoo.modules.db` — High.
9. Typed `ir.config_parameter` accessors; `CachedModel`; `user_writeable` field param; `BinaryValue` binary fields; `StoredTranslations` — High/Medium.
10. `res.bank` removed; `res.partner.bank` denormalised with `clearing.label`; additional partner identifiers (`partner_identifiers.py`) — High (removal) / Medium (successor).
11. Web: offline mode (Owl 3 plugin), Owl 3 migration (`owl3-migration.py`) — High.
12. `skills/` for AI coding agents; `test_translation_mode` — High.
13. Logging colours, `--unsafe-policy`, `--db-system`, `--gevent-workers` — High.
14. Search view `<filter date=...>` month/year attributes removed; `type="base64"` -> `type="bytes"` in XML data — High.

## 5. Removed / merged
| Removed | Successor (evidence) |
|---|---|
| `ir.model.access`, `ir.rule`, `models/ir_rule.py`, `security/base_security.xml` | `ir.access` (`ir_access.py`; `upgrade_code/19.4-00-ir-access.py`) |
| `res.bank` + `res_bank*.xml` | No successor model found; fields folded into `res.partner.bank` |
| `odoo/osv/` | `odoo.fields.Domain` (`orm/domains.py`) |
| `odoo/http.py` | `odoo/http/` package |
| `odoo/service/db.py`, `service/security.py` | `odoo/modules/db.py` (+ `http/session.py` for security parts, Medium) |
| `odoo/tools/query.py`, `cache.py`, `populate.py`, `pycompat.py`, `test_reports.py`, `_vendor/sessions.py` | `orm/query.py`, `orm/cache.py` (+`tools/cache` shim warning), `addons/populate` + `tools/duplicate.py`, `tests/reports.py` |
| `cli/populate.py` | `addons/populate/cli/populate.py`, `cli/duplicate.py` |
| `cli/templates/l10n_payroll` | none (l10n template dropped) |
| 13 test modules (`test_orm`, `test_access_rights`, `test_read_group`, ...) | `test_base`, `test_web`, `test_tests`, `test_translation`, `test_http` |

## 6. Implementation notes, risks, gotchas (19 -> 20 upgrades)
1. Run `odoo-bin upgrade_code` on all custom code; commit; then fix manually. Scripts cover: ir.access, ormcache, `t-call`, base64->bytes, `_rec_names_search`, date filters, Owl 3.
2. Review every `ir.access` warning from the migration — rules semantics (global vs group, AND/OR) were the most subtle change; test with real users per group.
3. Customisations overriding `_read_group*`, `_condition_to_sql`, `to_sql`, `_order_to_sql`, `Query` usage need manual porting.
4. Replace `get_param/set_param` with typed accessors; replace `registry.clear_cache` etc.
5. Python 3.12 runtime required; update Docker images/OS packages (Ubuntu 22.04/Jammy and Debian Bullseye are no longer supported targets), PyPDF2 -> pypdf.
6. Default bind 127.0.0.1: reverse-proxy-less deployments listening on all interfaces must set `http_interface` explicitly. `-s` no longer short for `--save`.
7. `res.partner.bank.bank_id` / `res.bank` data, partner `company_registry`, `partner_latitude/longitude` (geolocation) fields: migrate data in pre/post scripts (modules that still need them add them back; verify per module).
8. Binary fields: code that treats `record.datas`/binary values as base64 `bytes` may behave differently (BinaryValue proxy) — Medium.
9. Report/QWeb overrides that touch `_render_iterall/_get_error_info` need new `process` args.
10. `test_translation_mode` is a dev tool; never install on production.
11. Offline mode requires HTTPS/secure context; reverse proxies must serve secure context for the feature to work.
12. CI: test class names/paths changed; scripts that run `-i test_orm` must use `test_base`; default test tags use `post_install`.

## 7. Open questions / not verifiable from CE code
- Whether the "MCP / AI agent" feature exists in Enterprise or a separate repo (no CE evidence).
- Exact release-notes wording for the `ir.access` redesign and for `res.bank` removal (no web check done).
- Offline conflict resolution rules and which view types/actions are marked offline-capable by default (needs runtime test).
- Whether `res.bank` returns in another CE addon (grep of `addons/` for `'res.bank'` found only a migration script).
- Full behavioural diff of `tests/*` internals, `service/server.py`, `modules/loading.py` / `module_graph.py` (not exhaustively read).
- Partner geolocation field relocation (checked field removal from base only).
