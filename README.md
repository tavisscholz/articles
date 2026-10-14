# Articles

Canonical source for every article published on
[buildwithskala.com](https://buildwithskala.com) and
[tavisscholz.com](https://tavisscholz.com). One markdown file per article in
`articles/`; both sites read this repository and render each piece in their
own design system. Edit or add a file here and both sites update on their
next revalidation — no deploys.

## File format

`articles/<slug>.md` — YAML front matter followed by the markdown body:

```yaml
---
title: "Scaling Chaos: 7 Signs Growth Has Outrun Your Operating System"
slug: scaling-chaos-7-signs        # also the filename; never change after publish (it is the URL)
date: 2026-09-19                   # ISO date, ordering + display
lane: "Scaling Up"                 # topic lane, shown as the article's eyebrow/tag
laneTag: SCALE                     # SKALA's short tag (OPS / DEV / RE / FRAN / SCALE / AI)
stand: "Revenue is up. Everything else feels harder. …"   # one-line standfirst
minutes: 6                         # read time
sites: both                        # both | skala | personal — where it appears
canonical: skala                   # skala | personal — which domain owns rel=canonical
featured: false                    # SKALA homepage band
order: 5                           # position within the playbook listing
---

Body starts here. Plain markdown: ##/### headings, **bold**, *italic*,
> blockquotes (SKALA renders **bold-opening** blockquotes as pull quotes and
"**Fast Facts**" blocks as fact boxes), and lists. No H1 and no repeated
title/date/standfirst in the body — the front matter carries those and each
site renders its own header.
```

## Rules

- **Slugs are permanent.** They are live URLs on both sites.
- **`canonical` prevents a duplicate-content penalty**: the site that is NOT
  canonical for an article must render
  `<link rel="canonical" href="https://<canonical site>/…/<slug>">`.
- Site-specific furniture (author closer, CTAs, related links) belongs in the
  consuming site, not in the body. SKALA's author closer lives in
  `shared/skala-closer.md`.
- Keep claims consistent with the public record (see the public-figures
  policy in tavis-scholz-site/CLAUDE.md): no raw dollar figures, "600+
  market" not "614", no keep/close split.

## Consumers

| Site | Route | Renders |
|---|---|---|
| buildwithskala.com | `/playbook` + `/plays/<slug>` | full articles, SKALA design |
| tavisscholz.com | `/writing` (+ full pages when wired) | editorial design |
