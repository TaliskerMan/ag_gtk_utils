# ag_gtk_utils

Shared PyGObject (GTK 4.0 / Libadwaita) helper classes and base interfaces for desktop utility applications.

## Included Components

- **BaseWindow (`ag_gtk_utils.window`)**: A wrapper around `Adw.ApplicationWindow` that configures layouts, titles, default window dimensions, and exposes simple theme management APIs (`set_theme`).
- **BaseListener (`ag_gtk_utils.listener`)**: An abstract background keyboard listener helper designed to interface with native events and key bindings.

## Usage

Install this package locally in editable mode before running dependent applications (e.g. Shine, Rheolwyr) from source:

```bash
pip install -e /path/to/ag_gtk_utils
```
