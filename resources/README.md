# Resources

This directory contains the visual resource layer for the first-person video
narration production app. Resources should stay behavior-free: Python modules
own runtime logic, while this directory owns icons, platform app assets, and Qt
style sheets.

## Design Direction

- Use product-neutral naming. Resource files should not include legacy project
  names or internal package names.
- Keep the app icon text-free so it remains readable at dock, taskbar, tray, and
  installer sizes.
- Use a visual language tied to the workflow: first-person lens, narration
  waveform, and editing timeline.
- Keep both light and dark themes dense, quiet, and production-oriented for
  repeated script, audio, video, and export work.
- Prefer Qt-compatible HEX colors and stable QSS selectors over experimental CSS
  color functions.

## File Responsibilities

```text
resources/
├── icon.icns                 # macOS application bundle icon
├── icon.ico                  # Windows installer/application icon
├── icons/
│   ├── app_icon.png          # 512 px Linux/default application icon
│   ├── app_icon_32.png       # small toolbar/tray/title icon
│   ├── app_icon_64.png       # medium toolbar/window icon
│   ├── app_icon_128.png      # launcher icon
│   ├── app_icon_256.png      # high-density launcher icon
│   └── app_icon_512.png      # source-size application icon
└── styles/
    ├── dark_theme.qss        # dark production workspace theme
    └── light_theme.qss       # light production workspace theme
```

## Development Plan

1. Resource baseline: keep only app icons, platform bundle icons, and runtime
   QSS themes in this directory.
2. UI integration: route all application icon loading through
   `resources/icons`, and keep platform packaging targets at `resources/icon.*`.
3. Theme evolution: add new QSS selectors only when a widget has a stable
   `objectName` or a shared Qt role.
4. Asset growth: add workflow-specific media only when it is required by a
   shipped screen; avoid placeholder, duplicated, or decorative-only assets.
5. Verification: after resource updates, validate image dimensions, platform
   icon formats, old-brand text removal, and QSS compatibility.

## Maintenance Commands

```bash
python scripts/resource_assets.py generate
python scripts/resource_assets.py check
pytest tests/test_resources.py
```

`generate` refreshes PNG and Windows ICO assets on every platform. It also
refreshes `icon.icns` when macOS `iconutil` is available.
