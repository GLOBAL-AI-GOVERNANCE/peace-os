# Stable Human Validation Kit

This kit collects the human evidence that the stable-release holds in `PUBLIC_RELEASE_GATE.md` require and that `v0.3.0-rc2` does not claim. Use it with the [Real-World Evaluation Kit](REAL-WORLD-EVALUATION-KIT.md), which provides the facilitator protocol, task script, and defect record.

- **HUMAN UAT = NOT YET EVIDENCED**
- **ACCESSIBILITY HUMAN TESTING = NOT YET EVIDENCED**
- Completing a track is usability evidence for the tested build and environment. It is not WCAG conformance, certification, or a guarantee for other browsers, devices, or assistive technologies.

## Which build to test

| Build | Commit | Tree | How to open it |
|---|---|---|---|
| `v0.3.0-rc2` tag (reference baseline) | `8a40d94fcee14a6d6eb76782319bb90f0cec6202` | `d92212c36535b8e196805d24667a952bb148ccdf` | Check out the tag and serve `web/` locally, for example `python3 -m http.server --directory web 8000`, then open `http://localhost:8000/` |
| `main` on GitHub Pages | The commit in the served `deployment.json` | Not fixed | `https://global-ai-governance.github.io/peace-os/` |

GitHub Pages serves `main`, not the RC2 tag. The two web clients differ: `main` adds a cross-site navigation bar, changes the exercise boundary from a note to a labelled `aside` landmark, adds styles, and updates repository links. These changes affect keyboard order, landmarks, and screen-reader output. A result from one build therefore does not transfer to the other.

Each receipt names the exact commit it tested. The stable release decision uses only results recorded against the stable candidate commit, or results against an earlier commit together with a recorded review showing that the web client did not change between them.

## Result values

Record one value per track: `PASS`, `FAIL`, or `NOT_TESTED`. A track not attempted, or attempted without completing every check, is `NOT_TESTED`, or `FAIL` if a blocking defect was observed. No track inherits a result from another track, browser, device, or build.

## Tracks

| Track | Minimum checks | Required environment record |
|---|---|---|
| T1 Keyboard only | Full journey from start to After-Action Review with keyboard only. Logical order, visible focus, working skip link, no keyboard trap, and focus kept understandable after dynamic updates, errors, back navigation, session restore, and AAR actions. | Browser and version, OS, physical keyboard |
| T2 Screen reader | Full journey. Headings, landmarks, fieldsets, labels, status messages, errors, and result updates announced meaningfully. | Screen reader name and version, browser and version, OS, verbosity settings |
| T3 Zoom and reflow | Full journey at 200% browser zoom and at 320 CSS-pixel width, with no loss of content and no two-dimensional scrolling. | Browser, OS, display scale |
| T4 Physical mobile | Full journey on a physical phone or tablet, in portrait and landscape. | Device model, OS version, browser |
| T5 Firefox | Full journey in current Firefox. | Version, OS |
| T6 Safari/WebKit | Full journey in current Safari or another WebKit browser. | Version, OS |
| T7 Print and PDF | Print the After-Action Review and save it as PDF. The output is complete, readable, and correctly ordered. | Browser, OS, print or PDF target |
| T8 Reduced motion and forced colors | Journey with reduced-motion preference and with high-contrast or forced-colors mode where the platform supports it. | Browser, OS, settings |
| T9 Subject matter and learning | **Separate evidence class.** Independent subject-matter review and measured learning outcomes under `docs/validation/human-learning-validation-plan.md`. Usability tracks T1 to T8 do not contribute to T9. | Reviewer qualification, method, sample size |

These holds are outside this kit and need their own evidence: Godot runtime, Windows distribution, professional workshop, assessment, or certification use, operational use, and the `frame-ancestors` hosting decision.

## Evidence rules

- Evidence references are public-safe. Do not include names of participants, accounts, private URLs, or device identifiers.
- Record defects using the defect record in the Real-World Evaluation Kit.
- Each evidence set requires one [receipt](human-validation-receipt-template.json) per tester, build, and environment.

## Known visible discrepancies

- `VERIFICATION.md` and `PUBLIC_RELEASE_GATE.md` link the historical Pages run under the former repository name. Both files acknowledge this.
- The RC2 web client links to the former repository name. GitHub redirects these links, so they are not test failures.
- RC2 publication evidence names historical commit `aa6d8f75ce755fd143a4aa457eadf91b54604bd5`, which has the same tree as the current tag commit. See `VERIFICATION.md`.
