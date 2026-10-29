from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "operating-disposition-reference.schema.json"
EXAMPLE = ROOT / "examples" / "portfolio" / "operating-disposition-reference.json"
DOC = ROOT / "docs" / "portfolio-interoperability.md"


class PortfolioInteropTests(unittest.TestCase):
    def test_handoff_is_reference_only_and_non_authorizing(self) -> None:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        example = json.loads(EXAMPLE.read_text(encoding="utf-8"))
        self.assertIs(schema["properties"]["reference_only"]["const"], True)
        self.assertEqual(schema["properties"]["authority_effect"]["const"], "NONE")
        self.assertEqual(
            schema["properties"]["simulation_use"]["const"],
            "FICTIONAL_DECISION_CONTEXT_ONLY",
        )
        self.assertIs(example["reference_only"], True)
        self.assertEqual(example["authority_effect"], "NONE")

    def test_handoff_does_not_redefine_source_disposition_state(self) -> None:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        properties = set(schema["properties"])
        forbidden = {
            "state",
            "status",
            "operating_disposition",
            "authorization",
            "approved",
            "permitted",
        }
        self.assertTrue(properties.isdisjoint(forbidden))
        self.assertIn("operating_disposition_ref", properties)

    def test_example_is_bounded_by_schema_keys(self) -> None:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        example = json.loads(EXAMPLE.read_text(encoding="utf-8"))
        self.assertTrue(set(schema["required"]).issubset(example))
        self.assertTrue(set(example).issubset(schema["properties"]))

    def test_document_preserves_release_and_claim_boundaries(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        self.assertIn("public release is `v0.3.0`", text)
        self.assertIn("does not automatically ingest", text)
        self.assertIn("remain separate and are not closed", text)


if __name__ == "__main__":
    unittest.main()
