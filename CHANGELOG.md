# Changelog

## 0.2.0 (2026-04-27)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/VAIF-TECH/vaif-python/compare/v0.1.0...v0.2.0)

### Features

* realtime + storage MVP (Python parity with @vaif/client@0.3.0) ([#2](https://github.com/VAIF-TECH/vaif-python/issues/2)) ([70ca8e7](https://github.com/VAIF-TECH/vaif-python/commit/70ca8e766d5b3363de506a2975ecb527695127d6))

## 0.2.0 (2026-04-26)

### Features

* **realtime:** WebSocket realtime client (`vaif.lib.realtime.Realtime`) with
  channels, broadcasts, presence, and Postgres change feeds. Install with
  `pip install "vaif[realtime]"`.
* **storage:** Async upload helper (`vaif.lib.storage.upload`) with one-shot +
  multipart flows, concurrent chunk uploads, retries, progress callbacks, and
  cancellation. Plus `upload_to_signed_url` for direct presigned-URL uploads.
* **public:** `Realtime`, `RealtimeClient`, `upload`, `UploadHandle` re-exported
  from the top-level `vaif` package (Realtime is lazily loaded only when the
  optional `websockets` dep is installed).

### Docs

* Add `docs/realtime_quickstart.md` and `docs/storage_quickstart.md`.

## 0.1.0 (2026-04-26)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/VAIF-TECH/vaif-python/compare/v0.0.1...v0.1.0)

### Features

* add typescript/python/swift targets ([053b3b8](https://github.com/VAIF-TECH/vaif-python/commit/053b3b88884d3c030b77c27013906dbbf25bbc17))
* rename to vaif (PyPI name) ([044cf36](https://github.com/VAIF-TECH/vaif-python/commit/044cf3614014fdc5429b66d256e66a46e5a33954))


### Chores

* sync repo ([384350b](https://github.com/VAIF-TECH/vaif-python/commit/384350b7c5375d45aa70d2c9edc379c6027875ca))
