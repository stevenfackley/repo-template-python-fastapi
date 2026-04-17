"""Write the current OpenAPI schema to docs/api/openapi.json."""
from __future__ import annotations

import json
from pathlib import Path

from app.main import app


def main() -> None:
    out = Path("docs/api/openapi.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(app.openapi(), indent=2) + "\n")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
