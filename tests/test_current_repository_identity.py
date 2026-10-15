import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))

from check_naming import (  # noqa: E402
    CURRENT_PAGES_URL,
    CURRENT_REPOSITORY_URL,
    FORMER_PAGES,
    FORMER_REPOSITORY,
    SLUG,
    current_identity_violation,
)


class CurrentRepositoryIdentityTests(unittest.TestCase):
    def test_current_repository_and_pages_urls_are_accepted(self):
        text = f'Repository {CURRENT_REPOSITORY_URL} Pages {CURRENT_PAGES_URL}'
        self.assertIsNone(current_identity_violation(text, 'README.md'))

    def test_former_full_repository_url_is_rejected_on_a_current_surface(self):
        text = f'https://github.com/{FORMER_REPOSITORY}'
        self.assertIsNotNone(current_identity_violation(text, 'README.md'))

    def test_former_full_pages_url_is_rejected_on_a_current_surface(self):
        self.assertIsNotNone(current_identity_violation(FORMER_PAGES, 'web/index.html'))

    def test_allowed_historical_record_is_accepted(self):
        text = f'Historical repository {FORMER_REPOSITORY} and {FORMER_PAGES}'
        self.assertIsNone(current_identity_violation(text, 'CHANGELOG.md'))

    def test_compatibility_slug_alone_is_accepted(self):
        text = f'package {SLUG} storage {SLUG}-session-v1'
        self.assertIsNone(current_identity_violation(text, 'package.json'))


if __name__ == '__main__':
    unittest.main()
